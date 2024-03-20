<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier API for searching for Visier documents


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visiermodelquery.document_search.simple_search_document_headers`](#visiermodelquerydocument_searchsimple_search_document_headers)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=ModelQuery&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_model_query_python_sdk import VisierModelQuery, ApiException

visiermodelquery = VisierModelQuery(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Perform a simple search for Visier document headers
    simple_search_document_headers_response = visiermodelquery.document_search.simple_search_document_headers(
        q="string_example",
        limit=1,
        offset=1,
    )
    print(simple_search_document_headers_response)
except ApiException as e:
    print("Exception when calling DocumentSearchApi.simple_search_document_headers: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from visier_model_query_python_sdk import VisierModelQuery, ApiException

visiermodelquery = VisierModelQuery(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Perform a simple search for Visier document headers
        simple_search_document_headers_response = await visiermodelquery.document_search.asimple_search_document_headers(
            q="string_example",
            limit=1,
            offset=1,
        )
        print(simple_search_document_headers_response)
    except ApiException as e:
        print("Exception when calling DocumentSearchApi.simple_search_document_headers: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_model_query_python_sdk import VisierModelQuery, ApiException

visiermodelquery = VisierModelQuery(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Perform a simple search for Visier document headers
    simple_search_document_headers_response = visiermodelquery.document_search.raw.simple_search_document_headers(
        q="string_example",
        limit=1,
        offset=1,
    )
    pprint(simple_search_document_headers_response.body)
    pprint(simple_search_document_headers_response.body["document_headers"])
    pprint(simple_search_document_headers_response.headers)
    pprint(simple_search_document_headers_response.status)
    pprint(simple_search_document_headers_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentSearchApi.simple_search_document_headers: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visiermodelquery.document_search.simple_search_document_headers`<a id="visiermodelquerydocument_searchsimple_search_document_headers"></a>

Perform a simple search for Visier document headers, such as analysis titles. Simple search doesn't support keywords, Boolean expressions, or any other advanced search features.
 Example: `GET /v1alpha/search/simple/document-headers?q=My+Query&limit=10` returns the first 10 document headers that best match the query string `My Query`.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
simple_search_document_headers_response = visiermodelquery.document_search.simple_search_document_headers(
    q="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The search query string.

##### limit: `int`<a id="limit-int"></a>

The maximum number of results to return. Defaults to 100.

##### offset: `int`<a id="offset-int"></a>

The index to start retrieving results from, also known as offset. Defaults to 0.

#### 🔄 Return<a id="🔄-return"></a>

[`SimpleDocumentHeaderSearchResponseDTO`](./visier_model_query_python_sdk/pydantic/simple_document_header_search_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/search/simple/document-headers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
