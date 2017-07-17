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

Datasets are identified by 2 kinds of identifiers:

- the `dataset_uid` that is automatically set, and will never change through the dataset's lifetime
- the `dataset_id`, that can be chosen during dataset creation or changed on an unpublished dataset

### Attributes

Attribute | Description
--------- | -----------
`dataset_id` <br> *string*       | Human readable identifier of the dataset that can be modified when the dataset is not published
`dataset_uid` <br> *string*      | Unique identifier of the dataset that will never change through the dataset's lifetime
`metadata` <br> *Array of [metadata objects](#dataset-metadata)* | Dictionary of attributes about the dataset like a title, a description, keywords, that make it easily searchable through the portal's catalog
`status` <br> *[dataset status object](#dataset-status)* <br> <em class="expandable">expandable</em> | Current status of the object
`changes` <br> *Array of [dataset change objects](#dataset-changes)* <br> <em class="expandable">expandable</em> | List of all changes made to the current object

## Publish a dataset

> Definition

```http
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/publish
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/publish \
    -X PUT \
    -u username:password
```

> Example response

```json
```

Publishes a dataset.

This is an asynchronous call since the it may entail processing all records from the sources of the dataset.

### Parameters

No parameters

### Returns

Returns a [job object](#the-job-object).


## Unpublish a dataset

> Definition

```http
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/unpublish
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/unpublish \
    -X PUT \
    -u username:password
```

> Example response

```json
```

Unpublishes a dataset.

This will delete all currently indexed records for the dataset and make the dataset disappear from the explore catalog. Unpublishing a dataset does not delete the dataset, it merely acts on the exposed part of the data.


### Parameters

No parameters

### Returns

Returns a [job object](#the-job-object).