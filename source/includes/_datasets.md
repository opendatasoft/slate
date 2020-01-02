# Datasets

Datasets are at the core of the platform. A dataset is composed of:

- the actual data available on the portal (not available via the management API)
- metadata like a title, a description and keywords describing the data, so users can discover it in the portal's catalog
- configurations for processors, visualisation and security, which define the way data will be processed by the platform and made visible to users

Through the management API, it is possible to:

- create datasets
- attach resources to datasets
- configure datasets processing pipeline, visualisations and security attributes
- publish datasets

## The dataset object

> Example object

```json
{
    "dataset_id": "my-dataset",
    "dataset_uid": "da_xlnu9n",
    "metas": {
        "default": {
            "modified": "2017-08-27T20:17:30+00:00",
            "language": "en",
            "title": "My Dataset"
        },
        "publishing": {
            "published": false
        }
    },
    "last_modified": "2017-09-12T09:55:43.952561+00:00",
    "status": {
        "name": "idle"
    }
}
```

Datasets are identified by 2 kinds of identifiers:

- the `dataset_uid` that is automatically set, and will never change through the lifetime of the dataset.
- the `dataset_id`, that can be chosen during dataset creation or changed on an unpublished dataset

### Attributes

Attribute | Description
--------- | -----------
`dataset_id` <br> *string*       | Human readable identifier of the dataset that can be modified when the dataset is not published
`dataset_uid` <br> *string*      | Unique identifier of the dataset that will never change through the lifetime of the dataset
`status` <br> *[dataset status object](#dataset-status)* <br> <em class="expandable">expandable</em> | Current status of the object
`changes` <br> *Array of [dataset change objects](#dataset-changes)* <br> <em class="expandable">expandable</em> | List of all changes made to the current object
`metas` <br> *[metadata object](#dataset-metadata)* | Dictionary of attributes about the dataset like a title, a description, keywords, that make it easily searchable through the portal's catalog
`last_modified` <br> *datetime*  | Date when the dataset's configuration was last edited
`visibility` <br> *string*       | Defines if the dataset is visible for anonymous visitors <br> Can be `domain` if visibility is the same as the domain's visibility, or `restricted` if access is restricted to allowed users and groups
`status` <br> *[dataset status object](#dataset-status)* <br> <em class="expandable">expandable</em> | Keyword indicating if the dataset is waiting to be published, currently being published or if it encountered errors during last publishing

## List datasets

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets \
    -u username:password
```

> Example response

```json
[
    {
        "dataset_id": "my-dataset",
        "dataset_uid": "da_xlnu9n",
        "metas": {
            "default": {
                "modified": "2017-08-27T20:17:30+00:00",
                "language": "en",
                "title": "My Dataset"
            },
            "publishing": {
                "published": false
            }
        },
        "last_modified": "2017-09-12T09:55:43.952561+00:00",
        "status": {
            "name": "idle"
        }
    },
    {...},
    {...}
]
```

This endpoint lists all the datasets that can be edited by this user.

### Parameters

Parameter | Default | Description
--------- | ------- | -----------
`where` <br> *string* | None | Filter expression used to restrict returned datasets ([ODSQL documentation](https://docs.opendatasoft.com/api/explore/v2.html#where-clause))
`rows` <br> *string* | 10 | Number of items to return per page. Max value: 100
`page` <br> *string* | 1 | Request a specific page of results
`sort` <br> *string* | None | Field on which to sort the results list
`include_app_metas` <br> *string* | false | Explicitely request application metadata for each datasets
`timezone` <br> *string* | UTC | Timezone applied on datetime fields in query and response

### Returns

Returns a list of dataset objects.

## Create a dataset

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/
```

> Example request for an empty dataset

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/ \
    -X POST \
    -u username:password
    -d '{}'
```

> Example response for an empty dataset

```json
{
    "dataset_id": "da_eb353e",
    "dataset_uid": "da_eb353e",
    "metas": {
        "default": {
            "modified": "2018-01-25T13:12:17+00:00"
        }
    },
    "last_modified": "2018-01-25T13:12:17+00:00",
    "status": {
        "name": "idle"
    }
}
```

> Example request providing a title

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/datasets/ \
    -X POST \
    -u username:password
    -d '{"metas": {"default": {"title": "My dataset title"}}}'
```

> Example response with the provided title

```json
{
    "dataset_id": "my-dataset-title",
    "dataset_uid": "da_7qtcc3",
    "metas": {
        "default": {
            "modified": "2018-01-25T14:52:30+00:00",
            "title": "My dataset title"
        }
    },
    "last_modified": "2018-01-25T14:52:30+00:00",
    "status": {
        "name": "idle"
    }
}
```

> Example request in strict mode

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/datasets/?strict=true \
    -X POST \
    -u username:password
    -d '{}'
```

> Example response in strict mode

```json
{
    "status_code": 400,
    "message": "Dataset identifier (dataset_id) is mandatory",
    "raw_params": {},
    "raw_message": "Dataset identifier (dataset_id) is mandatory",
    "error_key": "ODSException"
}
```

Creates a new dataset.

### Parameters

Parameter | Description
--------- | -----------
`strict` <br> *boolean* | **Optional** Flag preventing the application from generating a `dataset_id` if missing or altering it if already taken. Defaults to `false`.

### Body

Parameter | Description
--------- | -----------
`dataset_id` <br> *string* | **optional unless in strict mode** Human readable identifier that will be used to retrieve the dataset in the explore API. <br> If not specified, will be auto-generated (from the `title` metadata if available).
`metas` <br> *object* | **optional** Object providing a title to the new dataset.
