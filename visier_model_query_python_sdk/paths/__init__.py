# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_model_query_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1ALPHA_SEARCH_SIMPLE_DOCUMENTHEADERS = "/v1alpha/search/simple/document-headers"
