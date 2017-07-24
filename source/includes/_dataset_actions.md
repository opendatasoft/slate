# Dataset actions

A state of a dataset can be changed by triggering actions. An action can make the dataset available through the search API or remove it from the search API.


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
{
    "job_id": "e0f8a9cf495a0ee617b0828da35f349bbb62ad43"
}
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
{
    "job_id": "e0f8a9cf495a0ee617b0828da35f349bbb62ad43"
}
```

Unpublishes a dataset.

This will delete all currently indexed records for the dataset and make the dataset disappear from the explore catalog. Unpublishing a dataset does not delete the dataset, it merely acts on the exposed part of the data.


### Parameters

No parameters

### Returns

Returns a [job object](#the-job-object).


## Abort a dataset processing

> Definition

```http
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/abort_processing
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/abort_processing \
    -X PUT \
    -u username:password
```

> Example response

```json
{
    "job_id": "e0f8a9cf495a0ee617b0828da35f349bbb62ad43"
}
```

Abort a dataset processing

It will stopped the current processing job and let the processed records available in the search API.


### Parameters

No parameters

### Returns

Returns a [job object](#the-job-object).

## Save a dataset version

> Definition

```http
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/save_version
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/save_version \
    -X PUT \
    -u username:password
```

> Example response

```json
{
    "job_id": "e0f8a9cf495a0ee617b0828da35f349bbb62ad43"
}
```

Save a dataset version

It will create a version from the current data of the dataset.

### Parameters

No parameters

### Returns

Returns a [job object](#the-job-object).
