# coding: utf-8

"""
    Visier Document Search API

    Visier API for searching for Visier documents

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_model_query_python_sdk import schemas  # noqa: F401


class DocumentSearchLinkDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Defines the attributes of a web request to reference documents in the search results.
    """


    class MetaOapg:
        
        class properties:
            href = schemas.StrSchema
            verb = schemas.StrSchema
            __annotations__ = {
                "href": href,
                "verb": verb,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verb"]) -> MetaOapg.properties.verb: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["href", "verb", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verb"]) -> typing.Union[MetaOapg.properties.verb, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["href", "verb", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        href: typing.Union[MetaOapg.properties.href, str, schemas.Unset] = schemas.unset,
        verb: typing.Union[MetaOapg.properties.verb, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentSearchLinkDTO':
        return super().__new__(
            cls,
            *args,
            href=href,
            verb=verb,
            _configuration=_configuration,
            **kwargs,
        )
