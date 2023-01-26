# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tagbase_server.models.base_model_ import Model
from tagbase_server import util


class Event200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(
        self,
        event_category=None,
        event_id=None,
        event_name=None,
        event_notes=None,
        event_status=None,
        time_start=None,
        time_end=None,
        duration=None,
        submission_id=None,
        tag_id=None,
    ):  # noqa: E501
        """Event200 - a model defined in OpenAPI

        :param event_category: The event_category of this Event200.  # noqa: E501
        :type event_category: str
        :param event_id: The event_id of this Event200.  # noqa: E501
        :type event_id: int
        :param event_name: The event_name of this Event200.  # noqa: E501
        :type event_name: str
        :param event_notes: The event_notes of this Event200.  # noqa: E501
        :type event_notes: str
        :param event_status: The event_status of this Event200.  # noqa: E501
        :type event_status: str
        :param time_start: The time_start of this Event200.  # noqa: E501
        :type time_start: str
        :param time_end: The time_end of this Event200.  # noqa: E501
        :type time_end: str
        :param duration: The duration of this Event200.  # noqa: E501
        :type duration: str
        :param submission_id: The submission_id of this Event200.  # noqa: E501
        :type submission_id: int
        :param tag_id: The tag_id of this Event200.  # noqa: E501
        :type tag_id: int
        """
        self.openapi_types = {
            "event_category": str,
            "event_id": int,
            "event_name": str,
            "event_notes": str,
            "event_status": str,
            "time_start": str,
            "time_end": str,
            "duration": str,
            "submission_id": int,
            "tag_id": int,
        }

        self.attribute_map = {
            "event_category": "event_category",
            "event_id": "event_id",
            "event_name": "event_name",
            "event_notes": "event_notes",
            "event_status": "event_status",
            "time_start": "time_start",
            "time_end": "time_end",
            "duration": "duration",
            "submission_id": "submission_id",
            "tag_id": "tag_id",
        }

        self._event_category = event_category
        self._event_id = event_id
        self._event_name = event_name
        self._event_notes = event_notes
        self._event_status = event_status
        self._time_start = time_start
        self._time_end = time_end
        self._duration = duration
        self._submission_id = submission_id
        self._tag_id = tag_id

    @classmethod
    def from_dict(cls, dikt) -> "Event200":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The event200 of this Event200.  # noqa: E501
        :rtype: Event200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event_category(self):
        """Gets the event_category of this Event200.

        ...  # noqa: E501

        :return: The event_category of this Event200.
        :rtype: str
        """
        return self._event_category

    @event_category.setter
    def event_category(self, event_category):
        """Sets the event_category of this Event200.

        ...  # noqa: E501

        :param event_category: The event_category of this Event200.
        :type event_category: str
        """

        self._event_category = event_category

    @property
    def event_id(self):
        """Gets the event_id of this Event200.

        Unique numeric event ID associated with the ingested tag data file  # noqa: E501

        :return: The event_id of this Event200.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Event200.

        Unique numeric event ID associated with the ingested tag data file  # noqa: E501

        :param event_id: The event_id of this Event200.
        :type event_id: int
        """

        self._event_id = event_id

    @property
    def event_name(self):
        """Gets the event_name of this Event200.

        ...  # noqa: E501

        :return: The event_name of this Event200.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this Event200.

        ...  # noqa: E501

        :param event_name: The event_name of this Event200.
        :type event_name: str
        """

        self._event_name = event_name

    @property
    def event_notes(self):
        """Gets the event_notes of this Event200.

        Free-form text field where details of the event can be optionally entered by the client  # noqa: E501

        :return: The event_notes of this Event200.
        :rtype: str
        """
        return self._event_notes

    @event_notes.setter
    def event_notes(self, event_notes):
        """Sets the event_notes of this Event200.

        Free-form text field where details of the event can be optionally entered by the client  # noqa: E501

        :param event_notes: The event_notes of this Event200.
        :type event_notes: str
        """

        self._event_notes = event_notes

    @property
    def event_status(self):
        """Gets the event_status of this Event200.

        Free-form text field where details of the event can be optionally entered by the client  # noqa: E501

        :return: The event_status of this Event200.
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this Event200.

        Free-form text field where details of the event can be optionally entered by the client  # noqa: E501

        :param event_status: The event_status of this Event200.
        :type event_status: str
        """
        allowed_values = [
            "failed",
            "finished",
            "killed",
            "migration",
            "postmigration",
            "premigration",
        ]  # noqa: E501
        if event_status not in allowed_values:
            raise ValueError(
                "Invalid value for `event_status` ({0}), must be one of {1}".format(
                    event_status, allowed_values
                )
            )

        self._event_status = event_status

    @property
    def time_start(self):
        """Gets the time_start of this Event200.

        Local datetime stamp at the time of the event start  # noqa: E501

        :return: The time_start of this Event200.
        :rtype: str
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """Sets the time_start of this Event200.

        Local datetime stamp at the time of the event start  # noqa: E501

        :param time_start: The time_start of this Event200.
        :type time_start: str
        """

        self._time_start = time_start

    @property
    def time_end(self):
        """Gets the time_end of this Event200.

        Local datetime stamp at the time of the event end  # noqa: E501

        :return: The time_end of this Event200.
        :rtype: str
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """Sets the time_end of this Event200.

        Local datetime stamp at the time of the event end  # noqa: E501

        :param time_end: The time_end of this Event200.
        :type time_end: str
        """

        self._time_end = time_end

    @property
    def duration(self):
        """Gets the duration of this Event200.

        The event duration e.g. different between 'time_start' and 'time_end'  # noqa: E501

        :return: The duration of this Event200.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Event200.

        The event duration e.g. different between 'time_start' and 'time_end'  # noqa: E501

        :param duration: The duration of this Event200.
        :type duration: str
        """

        self._duration = duration

    @property
    def submission_id(self):
        """Gets the submission_id of this Event200.

        Unique numeric ID assigned upon submission of a tag eTUFF data file for ingest/importation into Tagbase  # noqa: E501

        :return: The submission_id of this Event200.
        :rtype: int
        """
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id):
        """Sets the submission_id of this Event200.

        Unique numeric ID assigned upon submission of a tag eTUFF data file for ingest/importation into Tagbase  # noqa: E501

        :param submission_id: The submission_id of this Event200.
        :type submission_id: int
        """

        self._submission_id = submission_id

    @property
    def tag_id(self):
        """Gets the tag_id of this Event200.

        Unique numeric tag ID associated with the ingested tag data file  # noqa: E501

        :return: The tag_id of this Event200.
        :rtype: int
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this Event200.

        Unique numeric tag ID associated with the ingested tag data file  # noqa: E501

        :param tag_id: The tag_id of this Event200.
        :type tag_id: int
        """

        self._tag_id = tag_id
