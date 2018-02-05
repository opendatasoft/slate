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
- the `dataset_id`, that can be chosen during dataset creation or changed on an unpublished dataset. It will be used in the explore API and UI to access the dataset with a meaningful URL.

### Attributes

Attribute | Description
--------- | -----------
`dataset_id` <br> *string*       | Human readable identifier of the dataset that can be modified when the dataset is not published
`dataset_uid` <br> *string*      | Unique identifier of the dataset that will never change through the lifetime of the dataset
`status` <br> *[dataset status object](#dataset-status)* <br> <em class="expandable">expandable</em> | Current status of the object
`changes` <br> *Array of [dataset change objects](#dataset-changes)* <br> <em class="expandable">expandable</em> | List of all changes made to the current object
`metas` <br> *[metadata object](#dataset-metadata)* <br> <em class="expandable">expandable</em> | Dictionary of attributes about the dataset like a title, a description, keywords, that make it easily searchable through the portal's catalog
`last_modified` <br> *datetime*  | Date when the dataset's configuration was last edited
`visibility` <br> *string*       | Defines if the dataset is visible for anonymous visitors <br> Can be `domain` if visibility is the same as the domain's visibility, or `restricted` if access is restricted to allowed users and groups

## List datasets

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/ \
    -u username:password
```

> Example response

```json
[
    {
        "dataset_id": "my-dataset",
        "dataset_uid": "da_xlnu9n",
        "metas": {
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
`page` <br> *string* | 1 | Number of the page you want to retrieve.
`rows` <br> *string* | 10 | Number of items to return. Max value: 100
`sort` <br> *string* | None | Field on which to sort the results list
`include_app_metas` <br> *string* | false | Explicitely request application metadata for each datasets
`timezone` <br> *string* | UTC | Timezone applied on datetime fields in query and response

### Returns

Returns a list of dataset objects.


## Retrieve information about one dataset

This endpoint is for retrieving the dataset object with provided dataset_uid.

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}
```

> Example request

```shell
curl 'https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_7jgvnj?expand=metas'
```

> Example response

```json
{
    "dataset_id": "my-dataset",
    "dataset_uid": "da_7jgvnj",
    "metas": {
        "default": {
            "modified": "2017-08-27T20:17:30+00:00",
            "language": "en",
            "title": "My Dataset",
        }
    },
    "last_modified": "2017-09-12T09:55:43.952561+00:00",
    "status": {
        "name": "idle"
    },
    "changes": [],
    "visibility": "restricted",

}
```
