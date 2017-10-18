# Dataset Attachments

Dataset attachments are files that are exposed along with a dataset that can help making sense of the data.A

## The attachment object

The attachment object contains information about the file

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
`attachment_id` <br> *string* | A string that define an attachment
`url` <br> *URL of file* | The backing file's url

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

This endpoint is used to upload a new attachment

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

This endpoint is for retrieving information about one attachment by ID.

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
    "attachment_uid": "file_csv",
    "url": "odsfile://file.csv"
}
```

### Parameters

Parameter | Description
--------- | -----------
`attachment_id` | id of the attachment to retrieve.

### Returns

The [attachment objects](#the-attachment-object) corresponding to the attachment ID.

## Delete an attachment

This endpoint is for deleting a dataset attachment

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

On success, a HTTP 200 is returned


## Download an attachment

This endpoint is for downloading a file attached to a dataset

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
