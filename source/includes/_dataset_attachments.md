# Dataset Attachments

Dataset attachments are files that are exposed along with a dataset that can help making sense of the data.A

## The attachment object

The attachment object contains information about the file

### Attributes

> Example object

```json
{            
    "attachment_uid": "at_safkew",
    "file": {
        "file_id": "attached_file"
    }
}
```

Attribute | Description
--------- | -----------
`attachment_uid` <br> *string* | A string that uniquely define an attachment
`file` <br> *Expandable object* | The backing file

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
    "attachment_uid": "at_safkew",
    "file": {
        "file_id": "attached_file.pdf",
    }
},{
    "attachment_uid": "at_tiewkq",
    "file": {
        "file_id": "attached_text.txt",
    }
}]
```

### Parameters

No parameters

### Returns

A list of [attachment objects](#the-attachment-object).

## Create an attachment

In order to create an attachment for a dataset, the corresponding file must have been previously uploaded

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/
```

> Example request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments/
    -u username:password \
    -d {
        "file" {
            "file_id": "attached_spreadsheet.xlsx"
        }
    }
```

### Parameters

Parameter | Description
--------- | -----------
`file` <br> *[file object](#the-file-object)*| File to attach to the dataset

### Returns

On success, a HTTP 200 is returned

## Retrieve information about one attachment

This endpoint is for retrieving information about one attachment by UID.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/{ATTACHMENT_UID}/
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments/at_safkew/
    -u username:password
```

> Example response

```json
{
    "attachment_uid": "at_safkew",
    "file": {
        "file_id": "attached_file.pdf",
}
```

### Parameters

Parameter | Description
--------- | -----------
`attachment_uid` | uid of the attachment to retrieve.

### Returns

The [attachment objects](#the-attachment-object) corresponding to the attachment UID.

## Delete an attachment

This endpoint is for deleting a dataset attachment

> Definition

```HTTP
DELETE https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/attachments/{ATTACHMENT_UID}/
```

> Example request

```HTTP
curl -XDELETE https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/attachments/at_safkew/
    -u username:password
```

### Parameters

No parameters

### Returns

On success, a HTTP 200 is returned
