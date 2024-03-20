import typing_extensions

from visier_model_query_python_sdk.paths import PathValues
from visier_model_query_python_sdk.apis.paths.v1alpha_search_simple_document_headers import V1alphaSearchSimpleDocumentHeaders

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1ALPHA_SEARCH_SIMPLE_DOCUMENTHEADERS: V1alphaSearchSimpleDocumentHeaders,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1ALPHA_SEARCH_SIMPLE_DOCUMENTHEADERS: V1alphaSearchSimpleDocumentHeaders,
    }
)
