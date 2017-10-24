# Dataset attachments

Dataset attachments are files that are exposed along with a dataset. These files help making sense of the data.

## The attachment object

The attachment object contains information about the file.

### Attributes

> Example object

```json
{            
    "attachment_id": "file_csv",
    "url": "odsfile://file.csv"
}
```

Attribute | Description
--------- | -----------
`attachment_id` <br> *string* | A string that defines an attachment
`url` <br> *URL of file* | URL of the backing file

## List attachments

This endpoint is for listing all attachments to a dataset. 

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments
    -u username:password
```

> Example response

```json
[{
    "attachment_id": "file_csv",
    "url": "odsfile://file.csv"
},{
    "attachment_id": "file2_csv",
    "url": "odsfile://file2.csv"
}]
```

### Parameters

No parameters

### Returns

A list of [attachment objects](#the-attachment-object).

## Create an attachment

This endpoint is for uploading a new attachment to a dataset.

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/
```

> Example request

```HTTP
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@test.csv" -u user:password https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments/
```

### Parameters

Parameter | Description
--------- | -----------
`file` <br> File to attach to the dataset

### Returns

The [attachment objects](#the-attachment-object) corrsponding to the file which was posted.

## Retrieve information about one attachment

This endpoint is for retrieving information about the attachment, which identifier has been provided in the request.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/{ATTACHMENT_ID}/
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments/file_csv/
    -u username:password
```

> Example response

```json
{
    "attachment_id": "file_csv",
    "url": "odsfile://file.csv"
}
```

### Parameters

Parameter | Description
--------- | -----------
`attachment_id` | Identifier of the attachment to retrieve

### Returns

The [attachment objects](#the-attachment-object) corresponding to the attachment ID.

## Delete an attachment

This endpoint is for deleting a dataset attachment.

> Definition

```HTTP
DELETE https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/{ATTACHMENT_ID}/
```

> Example request

```HTTP
curl -XDELETE https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments/file_csv/
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
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/download_attachments/{ATTACHMENT_ID}/
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/download_attachments/file_csv/
    -u username:password
```

### Parameters

No parameters

### Returns

The attached file
