# coding: utf-8

"""
    Visier Document Search API

    Visier API for searching for Visier documents

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import visier_model_query_python_sdk
from visier_model_query_python_sdk.paths.v1alpha_search_simple_document_headers import get
from visier_model_query_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1alphaSearchSimpleDocumentHeaders(ApiTestMixin, unittest.TestCase):
    """
    V1alphaSearchSimpleDocumentHeaders unit test stubs
        Perform a simple search for Visier document headers
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()