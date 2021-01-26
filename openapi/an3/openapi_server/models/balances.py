# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.balance import Balance
from openapi_server import util

from openapi_server.models.balance import Balance  # noqa: E501

class Balances(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, balances=None):  # noqa: E501
        """Balances - a model defined in OpenAPI

        :param balances: The balances of this Balances.  # noqa: E501
        :type balances: List[Balance]
        """
        self.openapi_types = {
            'balances': List[Balance]
        }

        self.attribute_map = {
            'balances': 'balances'
        }

        self._balances = balances

    @classmethod
    def from_dict(cls, dikt) -> 'Balances':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Balances of this Balances.  # noqa: E501
        :rtype: Balances
        """
        return util.deserialize_model(dikt, cls)

    @property
    def balances(self):
        """Gets the balances of this Balances.


        :return: The balances of this Balances.
        :rtype: List[Balance]
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this Balances.


        :param balances: The balances of this Balances.
        :type balances: List[Balance]
        """

        self._balances = balances