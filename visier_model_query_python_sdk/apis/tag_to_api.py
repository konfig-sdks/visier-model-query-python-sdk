import typing_extensions

from visier_model_query_python_sdk.apis.tags import TagValues
from visier_model_query_python_sdk.apis.tags.document_search_api import DocumentSearchApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DOCUMENT_SEARCH: DocumentSearchApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DOCUMENT_SEARCH: DocumentSearchApi,
    }
)
