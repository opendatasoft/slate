# Dataset resources

## The resource object

The resource object describes a resource on the Opendatasoft platform. It is composed of a URL, a title, a type, and a parameter object. The URL is where data will be pulled to populate the dataset. Resources urls can (and often do!) point to [files](#files) uploaded to the platform using the `odsfile://` url scheme.

### Attributes

> Example object

```json
{
    "resource_uid": "re_abcdef",
    "url": "odsfile://resource.csv",
    "title": "My Awesome Data File",
    "type": "csvfile",
    "params": {
        "headers_first_row": false,
        "separator": ";"
    }
}
```

Attribute | Description
--------- | -----------
`resource_uid` <br> *string* | Unique identifier for the resource
`url` <br> *string* | URL of the resource
`title` <br> *string* | friendly title
`type` <br> *[extractor](#extractors)* | extractor type that should handle this resource
`params` <br> *object* | parameters passed to the extractor

## List dataset resources

This endpoint is meant to list all resources that are linked to a dataset.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/resources/
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/resources/
    -u username:password
```

> Example response

```json
[{
    "resource_uid": "re_abcdef",
    "url": "odsfile://resource.csv",
    "title": "My Awesome Data File",
    "type": "csvfile",
    "params": {
        "headers_first_row": false,
        "separator": ";"
    }
}, {...}]
```

### Returns
This API call returns the list of [resource objects](#the-resource-object) linked to the dataset.


## Create a new resource

This endpoint is for creating a new resource for the dataset

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/resources/
```

> Example request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/resources/
    -u username:password \
    -d '{ "url": "odsfile://resource.csv", "title": "My Awesome Data File", "type": "csvfile", "params": {"headers_first_row": false, "separator": ";"}}'
```

> Example response

```json
{
    "resource_uid": "re_abcdef",
    "url": "odsfile://resource.csv",
    "title": "My Awesome Data File",
    "type": "csvfile",
    "params": {
        "headers_first_row": false,
        "separator": ";"
    }
}
```

A new resource is created using the resource object sent in the body, and echoes back the object, with its newly generated resource_uid on success.

### Parameters

The payload must be a valid resource object without any uid.

### Returns

The newly created [resource object](#the-resource-object) with its newly created resource uid.

## Retrieve a resource object

This endpoint is for retrieving one resource object using its resource uid

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/resources/{RESOURCE_UID}
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/resources/{RESOURCE_UID}
    -u username:password
```

> Example response

```json
{
    "resource_uid": "re_abcdef",
    "url": "odsfile://resource.csv",
    "title": "My Awesome Data File",
    "type": "csvfile",
    "params": {
        "headers_first_row": false,
        "separator": ";"
    }
}
```

This API endpoint takes in its URL path a resource uid and returns the associated object.

### Returns

The [resource object](#the-object) with the given resource uid.

## Delete a resource

This endpoint is meant to delete a resource specified by its uid.

> Definition

```HTTP
DELETE https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/resources/{RESOURCE_UID}
```

> Example request

```HTTP
curl -XDELETE https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/{RESOURCE_UID}
    -u username:password
```

This API endpoint takes a resource UID in its URL path and deletes the resource associated to it. On success it returns a bare 204 HTTP response.

## Update a resource

This API endpoint is meant to update a resource specified with its uid.

> Definition

```HTTP
PUT https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/resources/{RESOURCE_UID}
```

> Example request

```HTTP
curl -XPUT https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/resources/{RESOURCE_UID}
    -u username:password \
    -d '{ "url": "odsfile://resource.csv", "title": "My Awesome Data File", "type": "csvfile", "params": {"headers_first_row": false, "separator": ";"}}'

```

> Example response

```json
{
    "resource_uid": "re_abcdef",
    "url": "odsfile://resource.csv",
    "title": "My Awesome Data File",
    "type": "csvfile",
    "params": {
        "headers_first_row": false,
        "separator": ";"
    }
}
```

This endpoint takes a resource uid in its url path and a resource object in its payload and updates the associated resource with the content of the payload.

### Parameters

The payload must be a valid resource object without any uid.

### Returns

The newly updated [resource object](#the-resource-object).

## Download a resource

This API endpoint is meant to download a resource specified with its UID.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/resources/{RESOURCE_UID}/download
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/resources/{RESOURCE_UID}/download
    -u username:password \

```

The resource must be a file uploaded to the platform: its URL uses the `odsfile://` URL scheme.

This endpoint takes a resource UID in its URL path.

### Parameters

No parameters

### Returns

The resource with the specified UID

## Preview the first few rows of the extracted resource

In order to test a resource configuration, it can be useful to preview the data. There are two ways of doing this, one uses the configuration of an existing resource to generate a preview, and the other one uses the configuration passed in the payload.

> Payload-based call definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/resource_preview
```

> UID-based call definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/resources/{RESOURCE_UID}/preview
```

> Example payload-based request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/resource_preview
    -u username:password \
    -d '{ "url": "odsfile://resource.csv", "title": "My Awesome Data File", "type": "csvfile", "params": {"headers_first_row": false, "separator": ";"}}'
```

> Example UID-based request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/resources/re_abcdef/preview
    -u username:password
```

> Example response

```json
{
    "fields": [{
        "description": null,
        "original_name": "column_1",
        "label": "Column 1",
        "type": "text",
        "annotations": [],
        "name": "column_1"
    }],
    "records": [
        {"column_1": "Hello"},
        {"column_1": "World"}
    ]
}
```

The payload-based call is sent in POST with a resource object in its body from which the endpoint takes its configuration to generate its preview. The resource_uid-based call uses an actual resource of the dataset by uid to generate a preview. The preview is composed of the fields definitions and the content of the first records up to 20.

### Parameters

For the payload-based call, the payload must be a valid resource object without any uid.

### Returns

The fields definitions and first few records extracted from the resource.
