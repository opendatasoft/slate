# Dataset metadata

Metadata is data describing the dataset itself. This is a set of fields describing the data, such as a title, a description, a list of keywords, a modification date, or whether the dataset is compliant to a specific geospatial norm. Adding metadata on a dataset is important to make sure it can be found, understood, and reused by users. In some cases, it can also be important for interoperability, to make sure other systems can understand the content of the dataset.

Dataset metadata are grouped within metadata templates that you can think of as namespaces. On top of the `default` metadata template, you may also find (depending on your domain's configuration) the `inspire`, `dcat` or `citadeljson` templates. Many other templates also exist and you can contact the support to define your own templates.

## The metadata object

This object stores both the definition and the value of a given metadata.

### Attributes

> Example object

```json
{
    "name": "title",
    "template": {
        "name": "default",
        "label": "Default metadata",
        "type:": "basic"
    },
    "definition": {},
    "value": "My agenda",
    "remote_value": "agendav2",
    "override_remote_value": true
}
```

Attribute | Description
--------- | -----------
`name` <br> *string* | Identifier for the object (inherited from the [definition](#the-metadata-definition-object)'s name)
`template` <br> *[metadate template object](#the-metadata-template-object)* | Group of the current object
`definition` <br> *[form object](#the-form-object)* <br> <em class="expandable">expandable</em> | The definition of the metadata type and widget
`value` | The object's value (may not be the indexed value, see below)
`remote_value` | The remote object's metadata value (see below)
`override_remote_value` <br> *boolean* | Flag indicating whether the indexed value is `value` or `remote_value`

In the case of federated and harvested datasets, metadata values are automatically collected from the remote source, showing up in the object as `remote_value`. You can however override this value with your own, specifying it in `value` and setting the `override_remote_value` flag to `True`. This flag determines which value will show up in the explore API output.

## The metadata template object

> Example object

```json
{
    "name": "default",
    "label": "Default metadata",
    "type:": "basic"
}
```

This object describes a category of metadata, a group. It has a type property, which describes the purpose of the object, with the following meaning.

### Types

Type | Description
---- | -----------
`basic` | Standard metadata values, their purpose is to describe the dataset to the end user.
`interop` | Sets of metadata values following an explicit norm for interoperability purposes.<br> Examples of such norms: DCAT, INSPIRE.
`admin` | Metadata values only meant for data publisher. These values will never show up in the explore APIs and are only visible in this management API by people having the permission to edit the dataset.

### Attributes

Attribute | Description
--------- | -----------
`name` <br> *string* | Identifier for the object
`label` <br> *string* | Plain text label of the object
`type` <br> *string* | Purpose of the object. <br> Possible values are `basic`, `interop` and `admin`

## List all metadata

Returns a list of metadata for the dataset with the given UID.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_ID}/metadata/
```

### Parameters

No parameters.

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/metadata/ \
    -u username:password
```

### Returns

The full list of [metadata objects](#the-metadata-object).

> Example response

```json
[
    {
        "name": "title",
        "template": {
            "name": "default",
            "label": "Default metadata",
            "type:": "basic"
        },
        "definition": {},
        "value": "My agenda",
        "remote_value": "agendav2",
        "override_remote_value": true
    },
    {...},
    {...}
]
```

## Retrieve a metadata

Retrieves the metadata with the given name within the given template.

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/metadata/{TEMPLATE_NAME}/{METADATA_NAME}/
```

### Parameters

No parameters.

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/metadata/default/title/ \
    -u username:password
```


### Returns

A [metadata object](#the-metadata-object).

> Example response

```json
{
    "name": "title",
    "template": {
        "name": "default",
        "label": "Default metadata",
        "type:": "basic"
    },
    "definition": {},
    "value": "My agenda",
    "remote_value": "agendav2",
    "override_remote_value": true
}
```

## Update a metadata value

> Definition

```HTTP
PUT https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/{TEMPLATE_NAME}/{METADATA_NAME}/
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/metadata/default/title/ \
    -u username:password \
    -X PUT \
    -d '{"value": "The best agenda", "override_remote_value": true}'
```

> Example response

```json
{
    "name": "title",
    "template": {
        "name": "default",
        "label": "Default metadata",
        "type:": "basic"
    },
    "definition": {},
    "value": "The best agenda",
    "remote_value": "agendav2",
    "override_remote_value": true
}
```

Updates the value of a metadata.

### Parameters

A json object passed in the request's body.

#### General case

Parameter | Description
--------- | -----------
`value` | The new metadata value. <br> Must conform to the metadata definition's type. Can be `null`.

#### For federated and harvested datasets

Parameter | Description
--------- | -----------
`value` | The new metadata value. <br> Must conform to the metadata definition's type. Can be `null`.
`override_remote_value` <br> *boolean* | Flag indicating whether the indexed value is `value` or `remote_value

### Returns

The updated [metadata object](#the-metadata-object).


## Reset a metadata value

> Definition

```HTTP
DELETE https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/{TEMPLATE_NAME}/{METADATA_NAME}/
```

> Example request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/metadata/default/title/ \
    -u username:password \
    -X DELETE
```

> Example response

```json
{
    "name": "title",
    "template": {
        "name": "default",
        "label": "Default metadata",
        "type:": "basic"
    },
    "definition": {},
    "value": null,
    "remote_value": "agendav2",
    "override_remote_value": false
}
```

Resets a metadata value by deleting the `value` property.

For federated and harvested datasets, it also sets the `override_remote_value` flag to `false`.

As a result, the metadata value won't show up in the explore API output anymore. Unless it is a federated or harvested dataset with a `remote_value` set.

### Parameters

No parameters.

### Returns

The reset [metadata object](#the-metadata-object).
