__author__ = 'Sahana Pandurangi Raghavendra'

import requests
from urllib import *
import warnings
import json
import time
import logging
import unittest

default_headers = {'Content-type': 'application/json', 'Accept': 'application/json'}


class Apimethods:
    def post(self, request_url, json_val=None, params=None, files=None, headers=None):
        if headers is None:
            headers = default_headers
        if files is None:
            response = requests.post(request_url, data=json.dumps(json_val), params=params, files=files,
                                     headers=headers, verify=True)
        else:
            response = requests.post(request_url, params=params, files=files,
                                     verify=True)
        return response

    def get(self, request_url, params=None, headers=None):
        if headers is None:
            headers = default_headers
        response = requests.request("GET", request_url, params=params, headers=headers, verify=True)
        return response

    def put(self, request_url, json_val=None, params=None, headers=None, files=None):
        if headers is None:
            headers = default_headers
        if json_val is None:
            response = requests.put(request_url, params=params, headers=headers, verify=True, files=files)
        else:
            response = requests.put(request_url, data=json.dumps(json_val), params=params, headers=headers, verify=True,
                                    files=files)
        return response

    def delete(self, request_url, json_val=None, headers=None, params=None):
        if headers:
            response = requests.delete(request_url, data=json.dumps(json_val), headers=headers, params=params,
                                       verify=True)
        else:
            headers = default_headers
            response = requests.delete(request_url, data=json.dumps(json_val), headers=headers, params=params,
                                       verify=True)
        return response
