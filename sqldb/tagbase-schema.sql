CREATE ROLE tagbase WITH SUPERUSER;

CREATE USER tagbase;

CREATE DATABASE tagbase WITH OWNER = 'tagbase';

\connect tagbase

CREATE TABLE submission
(
    submission_id   BIGSERIAL                     PRIMARY KEY,
    tag_id          bigint                        NOT NULL,
    dmas_granule_id bigint,
    date_time       timestamp(6) with time zone   DEFAULT current_timestamp,
    filename        character varying(255),
    version         character varying(50)
);

CREATE TABLE observation_types
(
    variable_id     BIGSERIAL               PRIMARY KEY,
    variable_name   character varying(255)  UNIQUE NOT NULL,
    standard_name   character varying(255),
    variable_source character varying(255),
    variable_units  character varying(255),
    notes           text
);

CREATE TABLE proc_observations
(
    date_time           timestamp(6) with time zone,
    variable_id         bigint                        NOT NULL  REFERENCES observation_types (variable_id),
    variable_value      double precision              NOT NULL,
    submission_id       bigint                        NOT NULL  REFERENCES submission (submission_id) ON DELETE CASCADE
);

CREATE TABLE metadata_types
(
   attribute_id     bigint                    PRIMARY KEY,
   category         character varying(1024)   NOT NULL,
   attribute_name   character varying(1024)   NOT NULL,
   type             character varying(1024)   NOT NULL,
   description      text                      NOT NULL,
   example          text,
   comments         text,
   necessity        character varying(1024)  NOT NULL
);

CREATE TABLE metadata
(
    submission_id     bigint    NOT NULL  REFERENCES submission (submission_id) ON DELETE CASCADE,
    attribute_id      bigint    NOT NULL  REFERENCES metadata_types (attribute_id),
    attribute_value   text      NOT NULL
);

CREATE TABLE data_time_series
(
    date_time           timestamp(6) with time zone,
    variable_id         bigint                        NOT NULL  REFERENCES observation_types (variable_id),
    variable_value      double precision              NOT NULL,
    submission_id       bigint                        NOT NULL  REFERENCES submission (submission_id) ON DELETE CASCADE,
    tag_id              bigint                        NOT NULL,
    position_date_time  timestamp(6) with time zone
);

CREATE TABLE data_position
(
    date_time           timestamp(6) with time zone,
    lat                 double precision,
    lon                 double precision,
    lat_err             double precision,
    lon_err             double precision,
    submission_id       bigint                        NOT NULL  REFERENCES submission (submission_id) ON DELETE CASCADE,
    tag_id              bigint                        NOT NULL
);

CREATE TABLE data_histogram_bin_unit
(
    bin_id     BIGSERIAL                    PRIMARY KEY,
    tag_id     bigint                       NOT NULL,
    units      character varying(255)       NOT NULL,
    type       character varying(255)       NOT NULL
);

CREATE TABLE data_histogram_bin_info
(
    bin_id          bigint                        NOT NULL  REFERENCES data_histogram_bin_unit (bin_id) ON DELETE CASCADE,
    bin_class       integer                       NOT NULL,
    min_value       double precision,
    max_value       double precision,
    UNIQUE (bin_id, bin_class)
);

CREATE TABLE data_histogram_bin_data
(
    submission_id     bigint    NOT NULL  REFERENCES submission (submission_id) ON DELETE CASCADE,
    tag_id            bigint    NOT NULL,
    bin_id            bigint    NOT NULL  REFERENCES data_histogram_bin_unit (bin_id) ON DELETE CASCADE,
    bin_class         integer    NOT NULL,
    date_time         timestamp(6) with time zone,
    frequency         double precision              NOT NULL,
    position_date_time  timestamp(6) with time zone
);


CREATE TABLE data_profile
(
    submission_id     bigint    NOT NULL  REFERENCES submission (submission_id) ON DELETE CASCADE,
    tag_id            bigint    NOT NULL,
    bin_id            bigint    REFERENCES data_histogram_bin_unit (bin_id) ON DELETE CASCADE,
    bin_class         integer   NOT NULL,
    date_time         timestamp(6) with time zone,
    depth             double precision,
    min_value         double precision,
    max_value         double precision,
    position_date_time  timestamp(6) with time zone
);

CREATE SEQUENCE submission_tag_id_seq;

CREATE INDEX data_position_date_time_index ON data_position(date_time);
CREATE INDEX data_time_series_date_time_index ON data_time_series(date_time);
CREATE INDEX data_time_series_pos_date_time_index ON data_time_series(position_date_time);
CREATE INDEX data_histogram_bin_data_date_time_index ON data_histogram_bin_data(date_time);
CREATE INDEX data_histogram_bin_data_pos_date_time_index ON data_histogram_bin_data(position_date_time);
CREATE INDEX data_profile_date_time_index ON data_profile(date_time);
CREATE INDEX data_profile_pos_date_time_index ON data_profile(position_date_time);
