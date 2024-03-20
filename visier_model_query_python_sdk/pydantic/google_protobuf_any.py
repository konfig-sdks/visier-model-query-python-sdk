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


class GoogleProtobufAny(BaseModel):
    # The type of the serialized message.
    @type_: typing.Optional[str] = Field(None, alias='@type')
    class Config:
        arbitrary_types_allowed = True
