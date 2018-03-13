# Dataset attachments

Dataset attachments are files that are exposed along with a dataset. These files help make sense of the data.

## The attachment object

The attachment object contains information about the file.

### Attributes

> Example object

```json
{
    "attachment_uid": "file_csv",
    "url": "odsfile://file.csv"
}
```

Attribute | Description
--------- | -----------
`attachment_uid` <br> *string* | A string that defines an attachment
`url` <br> *URL of file* | URL of the backing file

## List attachments

This endpoint is for listing all attachments to a dataset.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments
    -u username:password
```

> Example response

```json
[{
    "attachment_uid": "file_csv",
    "url": "odsfile://file.csv"
},{
    "attachment_uid": "file2_csv",
    "url": "odsfile://file2.csv"
}]
```

### Parameters

No parameters

### Returns

A list of [attachment objects](#the-attachment-object).

## Create an attachment

This endpoint is for attaching a file to a dataset.

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments
```

> Example request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments
    -u username:password \
    -d {
        "file": {
            "file_id": "attached_spreadsheet.xlsx"
        }
    }
```

### Parameters

Parameter | Description
--------- | -----------
`file` <br> File to attach to the dataset

### Returns

The [attachment objects](#the-attachment-object) for the newly created attachment.

## Retrieve information about one attachment

This endpoint is for retrieving information about an attachment with its UID.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/{ATTACHMENT_UID}
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments/file_csv
    -u username:password
```

> Example response

```json
{
    "attachment_uid": "file_csv",
    "url": "odsfile://file.csv"
}
```

### Parameters

Parameter | Description
--------- | -----------
`attachment_uid` | Identifier of the attachment to retrieve

### Returns

The [attachment objects](#the-attachment-object) corresponding to the attachment ID.

## Delete an attachment

This endpoint is for deleting a dataset attachment.

> Definition

```HTTP
DELETE https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/{ATTACHMENT_UID}
```

> Example request

```HTTP
curl -XDELETE https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments/file_csv
    -u username:password
```

### Parameters

No parameters

### Returns

On success, an HTTP 200 is returned


## Download an attachment

This endpoint is for downloading a file attached to a dataset.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/download_attachment/{ATTACHMENT_UID}
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/download_attachment/file_csv
    -u username:password
```

### Parameters

No parameters

### Returns

The attached file
