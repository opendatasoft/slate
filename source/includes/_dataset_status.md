# Dataset status

## The dataset status object

The dataset status describes the current state of a dataset, stating if it's published or not and the running operation. It is a finite state machine, with the following properties:

* a single state at a time
* the list of possible states, fully known
* the list of all transitions, fully known, each with the actions and conditions that can trigger them

Here is the full state machine description. 

![Dataset states machine](dataset_status_states.png "Dataset states machine")

### Commons attributes

Attribute | Description
--------- | -----------
`published` <br> *boolean* | true if the dataset is available in the search API
`name` <br> *string* | One of the dataset status values
`since` <br> *datetime* | Timestamp when the dataset entered in the current status
`user` <br> *user* <br> <em class="expandable">expandable</em> | User who started the action

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
    "published": false,
    "status": "processing",
    "since": "2015-04-15T15:13:04+00:00"
}
```

Retrieves the current dataset status.

### Parameters

No parameters

### Returns

The dataset status object that applies to the given dataset. See [Dataset status](#dataset-status) for specific attributes and the list of objects.

## The `idle` dataset status

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/status?expand=records_errors \
    -u username:password
```

> Example object

```json
{
    "published": true,
    "status": "idle",
    "since": "2015-04-15T15:13:04+00:00",
    "records_errors": [
        {
            "record_id" : "442cdf84ec84de2474dfba9422b045c064c36f05",
            "processor_uid": "pr_XXXXXX",
            "field_uid": "column_1",
            "message": "Cannot convert \"a\" to \"int\"",
            "raw_message": "Cannot convert \"{value}\" to \"{type}\"",
            "raw_params": {
                "value": "a",
                "type": "int"
            }
        }
    ]
}
```

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/status \
    -u username:password
```

> Example object

```json
{
    "published": true,
    "name": "idle",
    "since": "2015-04-15T15:13:04+00:00",
    "records_errors": 45
}
```

The *idle* status means that the dataset is not currently involved in an action. It can be published or not but no job is running. A newly created dataset is in that status.

### Attributes

Attribute | Description
--------- | -----------
records_errors <br> *[records errors object](#records_errors)* <br> <em class="expandable">expandable</em> | Errors which occurred during the processing. Can be from a processor, or a type conversion. This attribute is present only if the dataset is published.

### Transitions leading to the status

Transition origin status | Transition condition 
--------- | -----------
`processing` | Processing ended successfully
`deleting` | Deleting ended successfully
`aborting_processing` | Processing aborted

### Transitions leaving the status

Transition destination status | Transition condition
--------- | -----------
`queued` | The order has been received and is waiting to be realised


## The `error` dataset status

> Example object

```json
{
    "published": true,
    "name": "error",
    "since": "2015-04-15T15:13:04+00:00",
    "message": "Processor pr_XXXXXX is misconfigured for field address: invalid type",
    "raw_message": "Processor {processor_id} is misconfigured for field {field}: {msg}",
    "raw_params": {
        "processor_id": "pr_XXXXXX",
        "field": "address",
        "msg": "invalid type"
    }
    
}
```

The *error* status means that the action failed. It can be an error from the source or a pipeline misconfiguration.

### Attributes

Attribute | Description
--------- | -----------
raw_message | Template for the error message, parameters are not replaced
raw_params | Parameters values, to be injected in the raw_message
message | English message with the replaced parameter

### Transitions leading to the status

Status | Condition
--------- | -----------
`processing` | Processing ended with an error
`deleting` | Deleting ended with an error

### Transitions leaving the status

Status | Condition
--------- | -----------
`queued` | The order has been received and is waiting to be realised

## The `limit_reached` dataset status

> Example object

```json
{
    "published": true,
    "name": "limit_reached",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *limit_reached* status means that the dataset stopped processing records because it reached the maximum of authorized records in the license.

### Attributes

No specific attribute

### Transitions leading to the status

Status | Condition
--------- | -----------
`processing` | Processing stopped because of too many records in the dataset

### Transitions leaving the status

Status | Condition
--------- | -----------
`queued` | The order has been received and is waiting to be realised

## The `queued` dataset status

> Example object

```json
{
    "published": true,
    "name": "queued",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *queued* status means that the action has been received and is waiting to be performed.

### Attributes

No specific attribute

## The `processing` dataset status

> Example object

```json
{
    "published": true,
    "name": "processsing",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *processing* status means that dataset's metadata or data (with the extraction, transformation ...) are being made available to the search API.

### Transitions leading to the status

Status | Condition
--------- | -----------
`queued` | A worker is available

### Transitions leaving the status

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
    "published": true,
    "name": "deleting",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *deleting* status means that the dataset's metadata and data are being removed from the search API.

### Attributes

No specific attribute

### Transitions leading to the status

Status | Condition
--------- | -----------
`queued` | A worker is available

### Transitions leaving the status

Status | Condition
--------- | -----------
`processing` | Records are currently processing
`idle` | The processing ended successfully
`error` | The processing ended with an error
`limit_reached` | The processing stopped because it reached the maximum number of records allowed in the license

## The `aborting_processing` dataset status

> Example object

```json
{
    "published": true,
    "name": "aborting_processing",
    "since": "2015-04-15T15:13:04+00:00"
}
```

The *aborting_processing* status means that the order to stop the processing has been received and the processing will stop shortly

### Attributes

No specific attribute

### Transitions leading to the status

Status | Condition
--------- | -----------
`processing` | The abort order is received

### Transitions leaving the status

Status | Condition
--------- | -----------
`idle` | The processing ended successfully
`error` | The processing ended with an error
