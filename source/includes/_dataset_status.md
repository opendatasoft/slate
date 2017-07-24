# Dataset status

## The dataset status object

A dataset status describe the current state of a dataset, if it's published or not and the running operation. It is a finite state machine, with the following properties:

* It is in a single state at a time
* The list of possible states is fully known
* The list of all transitions is fully known, each with the actions and conditions that can trigger them

Here is the full state machine description. 

![Dataset states machine](dataset_status_states.png "Dataset states machine")


## Retrieve the current dataset status

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/status
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/status \
    -u username:password
```

> Example response

```json
{
    "published": True,
    "status": "processing",
    "since": "2015-04-15T15:13:04+00:00"
}
```

Retrieves the current dataset status.

### Parameters

No parameters

### Returns

The dataset status object that applies to the given dataset. See [Dataset status](#dataset-status) for specific attributes and the list of objects. The commons attributes are:

Attribute | Description
--------- | -----------
`published` <br> *boolean*       | True if the dataset is available in the search API.
`status` <br> *string*      | One of the dataset status values
`since` <br> *datetime* | Timestamp writed the dataset entered in the current status
`username` <br> *user* <br> <em class="expandable">expandable</em> | User who started the action


## The `idle` dataset status

> Example object

```json
{
    "published": True,
    "status": "idle",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *idle* status means that the dataset does not performed a specific action. It can be published or not but no job is running. A newly created dataset is in that status.


### Status leading to an `idle`status

Status | Condition
--------- | -----------
`processing` | Processing ended successfully
`deleting` | Deleting ended successfully
`saving_version` | Version successfully saved
`aborting_processing` | Processing aborted
`recovering_realtime_records` | Realtime records recovered
`scratching_realtime_recover_data` | Recover data deleted

### Status possible after the `idle` status

Status | Condition
--------- | -----------
`queued` | The order has been received and is waiting to be realised


## The `error` dataset status

> Example object

```json
{
    "published": True,
    "status": "error",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *error* status means that the action failed. It can be an error from the source or a pipeline misconfiguration.

### Status leading to an `error` status

Status | Condition
--------- | -----------
`processing` | Processing ended with an error
`deleting` | Deleting ended with an error
`saving_version` | Version save failed
`recovering_realtime_records` | Recovery failed

### Status possible after the `error` status

Status | Condition
--------- | -----------
`queued` | The order has been received and is waiting to be realised

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `limit_reached` dataset status

> Example object

```json
{
    "published": True,
    "status": "limit_reached",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *limit_reached* status means that the dataset stop adding records because it reached the maximum of authorized records in the license.

### Status leading to an `limit_reached` status

Status | Condition
--------- | -----------
`processing` | Processing stopped because of too many records in the dataset
`recovering_realtime_records` | Recovery stopped because of too many records in the dataset

### Status possible after the `error` status

Status | Condition
--------- | -----------
`queued` | The order has been received and is waiting to be realised

### Attributes

Attribute | Description
--------- | -----------
todo | todo


## The `queued` dataset status

> Example object

```json
{
    "published": True,
    "status": "queued",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *queue* status means that the action has been received and is waiting to be performed.

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `processing` dataset status

> Example object

```json
{
    "published": True,
    "status": "processsing",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *processing* status means that dataset's metadata or data (with the extraction, transformation ...) are made available to the search API.

### Status leading to an `processing` status

Status | Condition
--------- | -----------
`queued` | A worker is available

### Status possible after the `processing` status

Status | Condition
--------- | -----------
`idle` | The processing ended successfully
`error` | The processing ended with an error
`limit_reached` | The processing stopped because it reached the maximum number of records allowed in the license
`aborting_processing` | The processing is aborting


## The `deleting` dataset status

> Example object

```json
{
    "published": True,
    "status": "deleting",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *deleting* status means that the dataset's metadata and data are made unavailable from the search API.

### Status leading to an `deleting` status

Status | Condition
--------- | -----------
`queued` | A worker is available

### Status possible after the `deleting` status

Status | Condition
--------- | -----------
`processing` | Records are currently processing
`idle` | The processing ended successfully
`error` | The processing ended with an error
`limit_reached` | The processing stopped because it reached the maximum number of records allowed in the license

## The `saving_version` dataset status

> Example object

```json
{
    "published": True,
    "status": "saving_version",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *saving_version* status means that a new version of the dataset is being saved.

### Status leading to an `saving_version` status

Status | Condition
--------- | -----------
`queued` | A worker is available

### Status possible after the `saving_version` status

Status | Condition
--------- | -----------
`idle` | The processing ended successfully
`error` | The processing ended with an error


## The `aborting_processing` dataset status

> Example object

```json
{
    "published": True,
    "status": "aborting_processing",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *aborting_processing* status means that the order to stop the processing has been received and the processing will stopped shortly

### Status leading to an `aborting_processing` status

Status | Condition
--------- | -----------
`processing` | The abort order is received

### Status possible after the `aborting_processing` status

Status | Condition
--------- | -----------
`idle` | The processing ended successfully
`error` | The processing ended with an error


## The `recovering_realtime_records` dataset status

> Example object

```json
{
    "published": True,
    "status": "recovering_realtime_records",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *recovering_realtime_records* status means that the realtime dataset process the saved records.

### Status leading to an `recovering_realtime_records` status

Status | Condition
--------- | -----------
`queued` | A worker is available

### Status possible after the `recovering_realtime_records` status

Status | Condition
--------- | -----------
`idle` | The recovery ended successfully
`error` | The recovery ended with an error


## The `scratching_realtime_recover_data` dataset status

> Example object

```json
{
    "published": True,
    "status": "scratching_realtime_recover_data",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *scratching_realtime_recover_data* status means that all saved records are being deleting from the realtime dataset.


### Status leading to an `scratching_realtime_recover_data` status

Status | Condition
--------- | -----------
`queued` | A worker is available

### Status possible after the `scratching_realtime_recover_data` status

Status | Condition
--------- | -----------
`idle` | The recovery ended successfully
`error` | The recovery ended with an error