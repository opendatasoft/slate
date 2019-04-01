# Dataset alternative exports

Dataset alternative exports are custom dataset exports made outside of the platform but available for end users to download like a normal export in the export menu. Alternative exports are userful to expose exports in formats not supported by the platform, or in a specific geographic coordinate system. Since alternative exports are static files instead of dynamic exports, they tend to be very fast to download for end users and can be useful to offer a very large dataset export.

## The alternative export object

The alternative export object contains information about the file.

### Attributes

> Example object

```json
{
    "export_uid": "ae_bab015",
    "url": "odsfile://file.csv"
}
```

Attribute | Description
--------- | -----------
`export_uid` <br> *string* | A string that defines an alternative export
`url` <br> *URL of file* | URL of the backing file

## List alternative exports

This endpoint is for listing all alternative exports of a dataset.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/alternative_exports
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/alternative_exports
    -u username:password
```

> Example response

```json
[{
    "export_uid": "ae_bab015",
    "url": "odsfile://file.csv"
},{
    "export_uid": "ae_6539f8",
    "url": "odsfile://file2.csv"
}]
```

### Parameters

No parameters

### Returns

A list of [alternative export objects](#the-alternative-export-object).

## Create an alternative export

This endpoint is for attaching a file to a dataset.

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/alternative_exports
```

> Example request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/alternative_exports
    -u username:password \
    -d {"url": "odsfile://sorted_export.csv"}
```

### Parameters

Parameter | Description
--------- | -----------
`url` <br> The URL of the export. This can be a odsfile.

### Returns

The [alternative export objects](#the-alternative-export-object) for the newly created alternative export.

## Retrieve information about one alternative export

This endpoint is for retrieving information about an alternative export with its UID.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/alternative_exports/{EXPORT_UID}
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/alternative_exports/ae_XXXXXX
    -u username:password
```

> Example response

```json
{
    "export_uid": "ae_bab015",
    "url": "odsfile://sorted_export.csv"
}
```

### Parameters

Parameter | Description
--------- | -----------
`export_uid` | Identifier of the alternative export to retrieve

### Returns

The [alternative export objects](#the-alternative-export-object) corresponding to the alternative export ID.

## Delete an alternative export

This endpoint is for deleting a dataset alternative export.

> Definition

```HTTP
DELETE https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/alternative_exports/{EXPORT_UID}
```

> Example request

```HTTP
curl -XDELETE https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/alternative_exports/ae_XXXXXX
    -u username:password
```

### Parameters

No parameters

### Returns

On success, an HTTP 200 is returned


## Download an alternative export

This endpoint is for downloading a file attached to a dataset.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/download_alternative_export/{EXPORT_UID}
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/download_alternative_export/ae_XXXXXX
    -u username:password
```

### Parameters

No parameters

### Returns

The attached file
