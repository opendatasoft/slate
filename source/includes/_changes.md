# Dataset Changes

The changes of a dataset describe subsequent changes of states that affected the different sections of a dataset. Every action taken on any resource through POST, PUT or DELETE creates a change object that can be retrieved and acted upon.

## The change object

> Example object

```json
{
    "change_uid": 125,
    "dataset": {
        "dataset_uid": "dataset",
        "domain": "domain"
    },
    "user": {
        "username": "john_smith"
    },
    "timestamp": "2017-06-07T15:16:05.701266+00:00",
    "diff": {
        "metadata": [{
            "path": ["default", "description"],
            "old_value": null,
            "new_value": "dataset title",
            "operation_type": "create"
        }]
    },
    "sections": [
        "metadata"
    ]
}
```

The change object contains:

* a unique identifier
* a reference to the dataset that changed
* a reference to the user who created the new state
* the day and time at which the change occured
* the difference between the old and the new state of the dataset
* the sections in which the change happened

### Attributes

Attribute | Description
--------- | -----------
`change_uid` <br> *string* | Unique identifier for the change
`dataset` <br> *[dataset object](#the-dataset-object)* <br> <em class="expandable">expandable</em> | Dataset targeted by the change <br> *expandable*
`user` <br> *[user object](#the-user-object)* <br> <em class="expandable">expandable</em> | User who made the change <br> *expandable*
`timestamp` <br> *string* | Time at which the change was made
`diff` <br> *string* | Difference between the state before and after the change
`sections` <br> *array* | Sections modified by this change

## List all changes

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_ID}/changes/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/changed_dataset/changes/ \
    -u username:password
```

> Example response

```json
[
    {
        "change_uid": 126,
        "dataset": {
            "dataset_uid": "changed_dataset",
            "domain": "domain"
        },
        "user": {
            "username": "john_smith"
        },
        "timestamp": "2017-06-07T15:16:05.701266+00:00",
        "diff": {
            "security": [{
                "path": ["user", "jane_doe"],
                "old_value": null,
                "new_value": {
                    "data_visible": true
                },
                "operation_type": "create"
            }]
        },
        "sections": [
            "security"
        ]
    },
    {...},
    {...}
]
```

This endpoint lists all changes made to a dataset.

### Parameters

Parameter | Description
--------- | -----------
dataset_uid <br> *string* | Identifier of the dataset whose changes are to be listed

### Returns

Returns a list of changes for this datasets.

## Restore a change

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_ID}/restore_change/
```

> Example request

```shell
curl -XPUT https://yourdomain.opendatasoft.com/api/management/v2/restore_change/ \
    -u username:password -d '{ "change_uid": 126 }'
```

> Example response

```http
HTTP/2 200
```

Restores a dataset to the state it was before the selected change happened. Restoring a change will not erase the change history, but rather create a new change encapsulating the restoration.

### Parameters

Parameter | Description
--------- | -----------
`dataset_uid` <br> *string* | Identifier of the dataset to restore to a previous change
`change_uid` <br> *string* | Identifier of the change to restore. This parameter must be sent in the json format, inside a json object

### Returns

On success, a HTTP 200 is returned.
