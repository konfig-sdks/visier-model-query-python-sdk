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


class Status(BaseModel):
    # Error classification.
    error_code: typing.Optional[str] = Field(None, alias='errorCode')

    # Error message describing the root cause of the error.
    message: typing.Optional[str] = Field(None, alias='message')
    class Config:
        arbitrary_types_allowed = True