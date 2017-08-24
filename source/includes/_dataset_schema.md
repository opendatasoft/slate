# Dataset schema

The dataset schema is composed of the following parts:

* the source fields: the fields structure after the extraction (add a link)
* the output fields: the fields structure in the resulting API
* the record_id fields: the list of field which defined the record_id

## Source fields

Source field specifies the fields structure when records are extracted from the resource (a file, an api ...).

The configuration is boostrapped from the first resource and cannot be changed afterwards.

### The source field object


### Attributes

> Example object

```json
{
    "name": "column1",
    "type": "double",
    "options": [],
    "deleted": false
}
```

Attribute | Description
--------- | -----------
`name` <br> *string* | The name of the field, used in the processing configuration
`type` <br> *[Field types](#field-types)* | The type of the field
`options` <br> *[Field options](#field-options)* | The definition of the metadata type and widget
`deleted` | True if the field is deleted, else False.

### List all fields

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/
```

> Example request

```shell
curl https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/ \
    -u username:password
```

> Example response

```json
[
    {
        "name": "column1",
        "type": "double",
        "options": [],
        "deleted": false
    },
    {
        "name": "column2",
        "type": "text",
        "options": [],
        "deleted": true
    },
    {...},
]
```

This endpoint lists all the dataset source fields.

#### Parameters

No parameters.

#### Returns

The full list of *[source field objects](#the-source-field-object)*.

### Retrieve a source field

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/{FIELD_NAME}/
```

> Example request

```shell
curl https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/{FIELD_NAME}/ \
    -u username:password
```

> Example response

```json
{
    "name": "column1",
    "type": "double",
    "options": [],
    "deleted": false
}
```

This endpoint returns the source field.

#### Parameters

No parameters.

#### Returns

A *[source field objects](#the-source-field-object)*.


### Update a source field

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/{FIELD_NAME}/
```

> Example request

```shell
curl https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/{FIELD_NAME}/ \
    -X PUT \
    -u username:password 
```

> Example response

```json
{
    "name": "column1",
    "type": "double",
    "options": [],
    "deleted": false
}
```

This endpoint update a source field.

#### Parameters

A *[source field objects](#the-source-field-object)*.

#### Returns

A *[source field objects](#the-source-field-object)*.

### Delete a source field

> Definition
```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/{FIELD_NAME}/
```

> Example request

```shell
curl https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/{FIELD_NAME}/ \
    -X DELETE \
    -u username:password 
```

> Example response

```json
{
    "name": "column1",
    "type": "double",
    "options": [],
    "deleted": false
}
```

This endpoint deletes a source field.

#### Parameters

A *[source field objects](#the-source-field-object)*.

#### Returns

An http 200.


### Add a source field

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/
```

> Example request

```shell
curl https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/source_fields/ \
    -X POST \
    -u username:password 
```

> Example response

```json
{
    "name": "column1",
    "type": "double",
    "options": [],
    "deleted": false
}
```

This endpoint returns the source field.

#### Parameters

A *[source field objects](#the-source-field-object)*.

#### Returns

A *[source field objects](#the-source-field-object)*.


## Output fields

Output field specifies the fields structure in the resulting API.

## Record_id fields

Record_if fields define the list of field which take action in the record_id computation. We identify a record with a unique built-in field named record_id. During the processing, if two records have the same record_id, the first one is replaced by the second.

### Retrieve the record_id fields list

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/record_id_fields/
```

> Example request

```shell
curl https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/record_id_fields/ \
    -u username:password
```

> Example response

```json
[ "column1", "column2", "column3"]
```

This field name which take action in the record_id computation.

#### Parameters

No parameters.

#### Returns

A list of field name.

### Update the record_id fields list

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/record_id_fields/
```

> Example request

```shell
curl https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/record_id_fields/ \
    -x PUT
    -u username:password
```

> Example response

```json
[ "column1", "column2", "column3"]
```

This field name which take action in the record_id computation.

#### Parameters

A list of field name.

#### Returns

A list of field name.
