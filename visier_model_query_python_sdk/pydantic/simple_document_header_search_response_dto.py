# coding: utf-8

"""
    Visier Document Search API

    Visier API for searching for Visier documents

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from visier_model_query_python_sdk.pydantic.simple_document_header_search_result_dto import SimpleDocumentHeaderSearchResultDTO

class SimpleDocumentHeaderSearchResponseDTO(BaseModel):
    # The ordered collection of document header search results. The results are sorted according to their relevance in a descending order.
    document_headers: typing.Optional[typing.List[SimpleDocumentHeaderSearchResultDTO]] = Field(None, alias='documentHeaders')
    class Config:
        arbitrary_types_allowed = True