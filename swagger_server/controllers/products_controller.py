import connexion
import os
import psycopg2
import re
import six
import pytz
from datetime import datetime
from time import time

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server import util

# Needed Python 2/3 urllib compatability
try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode
    from urllib2 import urlopen

from werkzeug.exceptions import InternalServerError


def ingest_etuff_get(dmas_granule_id, file):
    """Get eTUFF file and execute ingestion.

    The etuff endpoint associates an eTUFF file with a given DMAS identifier before splitting the file, populating mappings to the Tagbase DB structure and executing ingestion.  # noqa: E501

    :param dmas_granule_id: Corresponding PO.DAAC DMAS identifier for the eTUFF file.
    :type dmas_granule_id: str
    :param file: Location of a network accessible (file, ftp, http, https) eTUFF file.
    :type file: str

    :rtype: Success
    """
    start = time()
    variable_lookup = {}
    dmas_granule_id = dmas_granule_id
    # Check if file exists locally, if not download it to /tmp
    data_file = file
    local_data_file = data_file[re.search("[file|ftp|http|https]:\/\/[^\/]*", data_file).end():]
    #app.logger.info("Locating %s" % local_data_file)
    if os.path.isfile(local_data_file):
        data_file = local_data_file
    else:
        # Download data file
        filename = "/tmp/" + data_file[data_file.rindex('/') + 1:]
        response = urlopen(data_file)
        chunk_size = 16 * 1024
        with open(filename, 'wb') as f:
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)

        data_file = filename
    submission_filename = data_file[data_file.rindex('/') + 1:]

    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' port=%d password='%s'" %
                                ('tagbase', 'tagbase', 'localhost', 5432, ''))
    except:
        #app.logger.error("Unable to connect to the database")
        raise InternalServerError("Unable to connect to the Tagbase database")

    cur = conn.cursor()

    cur.execute("INSERT INTO submission (tag_id, filename, dmas_granule_id) VALUES ((SELECT COALESCE(MAX(tag_id), NEXTVAL('submission_tag_id_seq')) FROM submission WHERE filename = %s), %s, %s)", (submission_filename, submission_filename, dmas_granule_id))
    cur.execute("SELECT currval('submission_submission_id_seq')")
    submission_id = cur.fetchone()[0]

    if data_file.endswith(".gz"):
        filename = "/tmp/" + data_file[data_file.rindex('/') + 1:-3]
        with gzip.open(data_file, 'rb') as f_in:
            with open(filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                data_file = filename

    metadata = []
    proc_obs = []
    with open(data_file, 'r') as data:
        lines = data.readlines()
        etag = False
        for line in lines:

            if line.startswith('//'):
                if 'etag' in line:
                    etag = True
                else:
                    etag = False
            elif line.strip().startswith(':'):
                if etag:
                    # Parse global attributes
                    tokens = line.strip()[1:].split(' = ')
                    cur.execute("SELECT attribute_id FROM metadata_types WHERE attribute_name = %s", (tokens[0],))
                    rows = cur.fetchall()
                    if len(rows) == 0:
                        #app.logger.warning("Unable to locate attribute_name = %s in metadata_types" % tokens[0])
                        continue
                    else:
                        str_submission_id = str(submission_id)
                        str_row = str(rows[0][0])
                        metadata.append((str_submission_id, str_row, tokens[1]))
            elif not line.startswith('"'):
                # Parse variable values
                tokens = line.split(',')

                variable_name = tokens[3]
                if variable_name in variable_lookup:
                    variable_id = variable_lookup[variable_name]
                else:
                    cur.execute("SELECT variable_id FROM observation_types WHERE variable_name = %s", (variable_name,))
                    row = cur.fetchone()
                    if row:
                        variable_id = row[0]
                    else:
                        # TODO Log error if variable_name doesn't already exist in observation_types
                        cur.execute(
                            "INSERT INTO observation_types(variable_name, variable_units) VALUES (%s, %s) ON CONFLICT (variable_name) DO NOTHING",
                            (variable_name, tokens[4].strip()))
                        cur.execute("SELECT currval('observation_types_variable_id_seq')")
                        variable_id = cur.fetchone()[0]
                    variable_lookup[variable_name] = variable_id
                date_time = None
                if tokens[0] != "":
                    print(tokens[0])
                    date_time = pytz.utc.localize(datetime.strptime(tokens[0], '%Y-%m-%d %H:%M:%S'))

                proc_obs.append((date_time, variable_id, tokens[2], submission_id))

                #app.logger.info(line.strip())
    for x in metadata:
        a = x[0]
        b = x[1]
        c = x[2]
        mog = cur.mogrify("(%s, %s, %s)", (a, b, c))
        cur.execute("INSERT INTO metadata (submission_id, attribute_id, attribute_value) VALUES " + mog.decode("utf-8"))

    for x in proc_obs:
        a = x[0]
        b = x[1]
        c = x[2]
        d = x[3]
        mog = cur.mogrify("(%s, %s, %s, %s)", (a, b, c, d))
        cur.execute("INSERT INTO proc_observations (date_time, variable_id, variable_value, submission_id) VALUES " + mog.decode("utf-8"))

    conn.commit()

    cur.close()
    conn.close()

    end = time()
    #app.logger.info("Time took to ingest file: %f" % (end - start))

    return "Data file %s has been ingested into tagbase. Time took to ingest file: %s s" % (data, (end - start))


def ingest_ncingester_get(profile, file):  # noqa: E501
    """Get netCDF file and execute specific profile ingestion.

    The ningester endpoint associates a netCDF file with a given in-situ profile before splitting the file, populating mappings to the Tagbase DB structure and executing ingestion.  # noqa: E501

    :param profile: Profile to map the ingestion to. Options include ACDD, CF
    :type profile: str
    :param file: Location of a network accessible netCDF file.
    :type file: str

    :rtype: Success
    """
    return 'do some magic!'
