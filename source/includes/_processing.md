# Processing

The Opendatasoft platform allows you to apply one or more processors to a dataset. These processors are units of data transformation and other processing. Each processor represents a configurable operation that will be applied to all rows of a dataset. Examples of what you can do with a processor include replacing text with a regex, geocoding an address into geographical coordinates, creating a new column that contains the result of a substraction between two existing columns and much more. A general-purpose presentation of processors and their capabilities is available on the [data processing documentation](https://docs.opendatasoft.com/en/sourcing_and_processing_data/processing_data.html).

## The processor object

The processor object is composed of a unique ID for the processor, the processor name and the processor configuration. The configuration is a JSON object whose keys are dependent of the processor itself.

### Attributes

> Example object

```json
{
    "processor_uid": "pr_abcdef",
    "name":"regexp_replace",
    "args": {
        "field": "text_field",
        "regexp": ".*",
        "new": "Hello World"
    }
}
```

> Example object with label

```json
{
    "processor_uid": "pr_mgnlcn",
    "name":"expression",
    "label":"my_column > or < 0",
    "args": {
        "output_field": "result",
        "expression": "{{my_column > 0 ? 'positive' : 'negative'}}"
    }
}
```

Attribute | Description
--------- | -----------
`name` <br> *string* | Name of the processor
`args` <br> *object* | Processor configuration
`processor_uid` <br> *string* | Unique identifier for the processor
`label` <br> *string* | (optional) Label of the processor


## List all available processors

This endpoint allows the caller to find out what processors are available to them

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/processors/
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/processors/
    -u username:password
```

> Example response

```json
[
    "regexp_replace",
    "transform_coordinates",
    "string_extractor",
    "skip_record",
    "create_geopoint",
    "split",
    "delete_record",
    "set_timezone",
    "string_replace",
    "date_normalizer",
    "geojoin",
    "concat",
    "geo_distance",
    "expression",
    "unicode_normalize",
    ...
]
```

The endpoint returns a list of all processors available on the domain.

### Returns

The list of all available processor names.

## List dataset processors

This endpoint is meant to return the list of configured processors for a dataset.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/processors/
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_abcdef/processors/
    -u username:password
```

> Example response

```json
[{
    "processor_uid": "pr_abcdef",
    "name":"regexp_replace",
    "args": {
        "field": "text_field",
        "regexp": ".*",
        "new": "Hello World"
    }
}, {
    "processor_uid": "pr_zyxwvu",
    "name": "string_replace",
    "args": {
        "field": "text_field",
        "all_fields": false,
        "old": "World",
        "new": "World!"
    }
}]
```

The payload lists the processing stack of the dataset. Please note that it reads in the order in which processors are applied.


### Returns
The list of [processor objects](#the-processor-object).

## Append a new processor to a dataset

This endpoint is for creating a new processor for the dataset. The processor will be appended to the end of the processing stack.

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/da_abcdef/processors/
```

> Example request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/processors/
    -u username:password \
    -d '{"name": "string_extractor", "args": {"field": "text_field", "regexp": "(?P<planet>^World)"}'
```

> Example response

```json
{
    "processor_uid": "pr_newnew",
    "name": "string_extractor",
    "args": {
        "field": "text_field",
        "regexp": "(?P<planet>^World)"
    }
}
```

The endpoint takes a processor object (without its processor_uid, which will be automatically generated), creates a processor with the provided configuration and appends it at the end of the processing chain.

### Parameters

Parameter | Description
--------- | -----------
`name` <br> *string* | name of the processor
`args` <br> *object* | processor-dependent parameters


### Returns
The newly created [processor object](#the-processor-object).


## Retrieve informations about a processor

This endpoint is meant to retrieve a processor object in a dataset processing stack from its uid.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/processors/{PROCESSOR_UID}
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_abcdef/processors/pr_newnew
    -u username:password
```

> Example response

```json
{
    "processor_uid": "pr_newnew",
    "name": "string_extractor",
    "args": {
        "field": "text_field",
        "regexp": "(?P<planet>^World)"
    }
}
```

### Returns
The requested [processor object](#the-processor-object).

## Update a processor

This endpoint is meant to update a processor in place within the processing stack of a dataset.

> Definition

```
PUT https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/processors/{PROCESSOR_UID}
```

> Example request

```HTTP
curl -XPUT https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_abcdef/processors/pr_abcdef
    -u username:password \
    -d '{"name":"regexp_replace", "args": {"field": "text_field", "regexp": ".*", "new": "Bonjour Monde"}'
```

> Example response

```json
{
    "processor_uid": "pr_abcdef",
    "name":"regexp_replace",
    "args": {
        "field": "text_field",
        "regexp": ".*",
        "new": "Bonjour Monde"
    }
}
```

### Parameters

Parameter | Description
--------- | -----------
`name` <br> *string* | name of the processor
`args` <br> *object* | processor-dependent parameters

### Returns
The newly updated [processor object](#the-processor-object).

## Delete a processor

This endpoint is meant to delete a processor from the processing stack of a dataset

> Definition

```HTTP
DELETE https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/processors/{PROCESSOR_UID}
```

> Example request

```HTTP
curl -XDELETE https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_abcdef/processors/pr_newnew
    -u username:password
```

### Returns

On successful deletion, the endpoint returns a HTTP 204 without any content.


## Retrieve possible processor parameters from processor name

For some processors and some processors parameters, the Opendatasoft platform has a way to suggest values for the processor parameters. It can for instance figure out the list of fields the processor could operate on.

This endpoint is meant to expose this feature, by taking a processor name and returning the set of possible values for each parameter.

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/guess_processor_params
```

> Example request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/guess_processor_params
    -u username:password \
    -d '{"name": "expand_json_array"}'
}
```

> Example response

```json
{
    "json_array_field": {
        "text_field": {
            "annotations": [],
            "description": null,
            "label": "text_field",
            "name": "text_field",
            "original_name": "text_field",
            "type": "text"
        }
    }
}
```

The endpoint takes the name of a processor and suggest relevant configuration values as if a processor of that type was appended to the processing stack. The parameters are returned in an object structure, that is as key values pair. The values in these pairs are any extra relevant information, such as the dataset field specification. Please note that some parameters cannot be guessed and will simply be returned empty.

### Parameters

Parameter | Description
--------- | -----------
`name` <br> *string* | name of the processor

### Returns
The endpoint returns an object whose keys are the names of the processor parameters, and whose values are objects containing the guessed values. These values have their name as keys and specifications as value.
