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
`metas` <br> *[metadata object](#dataset-metadata)* | Dictionary of attributes about the dataset like a title, a description, keywords, that make it easily searchable through the portal's catalog
`last_modified` <br> *datetime*  | Date when the dataset's configuration was last edited
`published` <br> *boolean*       | Flag indicating whether the dataset is published or not
`default_security` <br> *object* |
`visibility` <br> *string*       | Defines if the dataset is visible for anonymous visitors <br> Can be `domain` if visibility is the same as the domain's visibility, or `restricted` if access is restricted to allowed users and groups
`dataset_processing_status` <br> *[dataset processing status object](#dataset-processing-status)* <br> <em class="expandable">expandable</em> | Keyword indicating if the dataset is waiting to be published, currently being published or if it encountered errors during last publishing

## The dataset status object

A dataset is a finite state machine.

* It is in a single state at a time
* The list of possible states is fully known
* The list of all transitions is fully known, each with the actions and conditions that can trigger them

Here is the full state machine description.

### Statuses

Status | Descriptions
------ | ------------
`idle` |
`queued` |
`processing_dataset` |
`processing_resource_records` |
`processing_all_dataset_data` |
`processing_realtime` |
`deleting_dataset` |
`deleting_resource_records` |
`deleting_all_dataset_data` |
`saving_dataset_version` |
`error` |
`aborting_processing` |
`limit_reached` |
`recovering_realtime_records` |
`scratching_realtime_recover_data` |

### Attributes

Attribute | Description
--------- | -----------
`status` <br> *string* | <br> Possible values are `idle`, `queued`, `processing_dataset`, `processing_resource_records`, `processing_all_dataset_data`, `processing_realtime`, `deleting_dataset`, `deleting_resource_records`, `deleting_all_dataset_data`, `saving_dataset_version`, `error`, `aborting_processing`, `limit_reached`, `recovering_realtime_records`, `scratching_realtime_recover_data`
`timestamp` <br> *datetime* |
`params` <br> *object* |


## Publish a dataset

Publishes a dataset.

This is an asynchronous call since the it may entail processing all records from the sources of the dataset.

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

### Parameters

No parameters

### Returns

Returns a [job object](#the-job-object).


## Unpublish a dataset

## Abort an ongoing publish