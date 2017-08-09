# Dataset actions

The state of a dataset can be changed by triggering actions. An action can make the dataset available through the search API or remove it from the search API. Available actions are:
- publish a dataset
- unpublish a dataset
- abort a processing


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

Make the dataset modifications available through the search API. It may entail the processing of all the records.

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

Remove the dataset from the search API. Unpublishing a dataset does not delete the dataset.


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

Stop the current processing job and keep the processed records available in the search API.


### Parameters

No parameters

### Returns

Returns a [job object](#the-job-object).
