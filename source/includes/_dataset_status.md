# Dataset status

## The dataset status object

A dataset is a finite state machine.

* It is in a single state at a time
* The list of possible states is fully known
* The list of all transitions is fully known, each with the actions and conditions that can trigger them

Here is the full state machine description.

todo: include state machine graph and make the transitions explicit (what triggers the transition)

## The `idle` dataset status

> Example object

```json
{}
```

todo:
* description of the meaning of the status and of the conditions that led there.
* If the status references a job, make sure the job is an expandable relationship.
* Explain each time that the job should be polled for more details.
* Include a `since` datetime in each object

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `queued` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `processing_dataset` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `processing_resource_records` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `processing_all_dataset_data` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `processing_realtime` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `deleting_dataset` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `deleting_resource_records` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `deleting_all_dataset_data` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `saving_dataset_version` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `error` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `aborting_processing` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `limit_reached` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `recovering_realtime_records` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

## The `scratching_realtime_recover_data` dataset status

> Example object

```json
{}
```

todo: description of the meaning of the status and of the conditions that led there

### Attributes

Attribute | Description
--------- | -----------
todo | todo

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
{}
```

Retrieves the current dataset status.

### Parameters

No parameters

### Returns

The dataset status object that applies to the given dataset. See [Dataset status](#dataset-status) for the full list of objects and their attributes.
