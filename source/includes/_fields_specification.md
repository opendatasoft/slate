# Fields specification

Dataset fields can be configured using a variety of options. These options include their type, their label, whether they are a filter or not, whether they should be discarded, or even how fields are ordered. These configuration options, collectively refered to as fields specification, are accessed using [processor-like objects](#the-processor-object).

## Available configuration items

Here is a comprehensive list of the available configuration items. Example usage for each one can be found in their dedicated section.

Configuration name | Description
------------------ | -----------
[`rename`](#rename) | changes the name of the field and sets its label
[`type`](#type) | sets the field type
[`annotate`](#annotate) | annotates the field
[`description`](#description) | describes the field
[`order`](#order) | reorders fields
[`delete`](#delete) | deletes a field

## Rename

> change the field named "original_field_id" to "new_field_id", and set its label to "desired_label"

```json
{
    "name": "rename",
    "args": {
        "from_name": "original_field_id",
        "to_name": "new_field_id",
        "label": "desired_label"
    }
}
```

Fields are identified by a technical name, and have a human-friendly label; both are editable using this configuration item.

## Type

> change the type of the field named "field_id" to a geo shape

```json
{
    "name": "type",
    "args": {
        "field": "field_id",
        "type": "geo_shape"
    }
}
```

Types are the most basic way of qualifying fields. Different types unlock different kinds of visualizations and agregations. Below is the list of types supported by the platform.

Type name | Description
--------- | -----------
`text` | text
`int` | integer
`double` | floating point
`geo_point_2d` | geographical location (2 dimensions)
`geo_shape` | geographical shape
`date` | date
`datetime` | date and time
`file` | file (blob)

## Annotate

> mark the `unique_field` as the unique ID for the records

```json
{
    "name": "annotate",
    "args": {
        "field": "unique_field",
        "annotation": "id"
    }
}
```

> mark the `category_field` as a facet

```json
{
    "name": "annotate",
    "args": {
        "field": "category_field",
        "annotation": "facet"
    }
}
```

> make the `facetted_field` facet be sorted by descending count

```json
{
    "name": "annotate",
    "args": {
        "field": "facetted_field",
        "annotation": "facetsort",
        "args": ["-count"]
    },
}
```

> make the `datetime_field` have an hourly precision when used in timeseries

```json
{
    "name": "annotate",
    "args": {
        "field": "datetime_field",
        "annotation": "timeseries_precision",
        "args": ["hour"]
    },
}
```

> mark the `nondescript_number` field as representing square kilometers

```json
{
    "name": "annotate",
    "args": {
        "field": "nondescript_number",
        "annotation": "unit",
        "args":["km2"]
    },
}
```

> force the `decimal_field` precision to 5 digits after the decimal point

```json
{
    "name": "annotate",
    "args": {
        "field": "decimal_field",
        "annotation": "decimals",
        "args": [5]
    },
}
```

> mark the `multivalued_field` as multivalued, with a comma as the values separator

```json
{
    "name": "annotate",
    "args": {
        "field": "multivalued_field",
        "annotation": "multivalued",
        "args": [","]
    },
}
```

Annotation are a mean to configure special behavior for the fields. Some annotations are only available for certain field types. Setting the facet annotation on a field unlocks other annotations for the field.

Annotation name | Field type | Description
--------------- | ---------- | ----------
`id`|all field types | Whether this field should constitute one of the keys of the records unique IDs. If no field has this annotation, all fields contribute to the creation of the records unique ID.
`facet` | `date`, `datetime`, `int`, `decimal`, `text` | Whether the field can serve as a filter
`facetsort` | all field types, facet only | How to sort the facets. Possible arguments are `count` and `-count` for all field types, `alphanum` and `-alphanum` for `date`, `datetime` and `text`, `num` and `-num` for `decimal` and `int`
`disjunctive` | `decimal`, `int` and `text`, facet only | Whether multiple values can be selected for the facet
`timeseries_precision` | `date` and `datetime` | display precision of the field. Possible arguments are `year`, `month` and `day` for `date`, `hour` and `minute` for `datetime`
`timerangeFilter` | `date` and `datetime`, facet only | Whether to activate the timerange filter
`unit` | `int` and `decimal` | The unit of the field. Supported units are listed [in the dedicated chapter](#units)
`decimals` | `decimal only` | The argument is the number of digits to appear after the decimal point
`sortable` | `text` | whether the field should be sortable in table view
`multivalued` | `text` | whether the field contains multiple values serparated by a character. The separator must be given as the argument
`hierarchical` | `text`, facet only | whether the field is hierarchical. The separator must be given as the argument

## Description

> give the `complicated_field` an elegant description

```json
{
    "name": "description",
    "args": {
        "field": "complicated_field",
        "description": "Elegant description"
    }
}
```

Description are a mean to qualify and give some extra details about the content of the field. Descriptions are available when consulting the data.

## Order

> reorder the 3 fields `first_field`, `second_field` and `third_field` to be in the reverse order

```json
{
    "name": "order",
    "args": [
        "third_field",
        "second_field",
        "first_field"
    ]
}
```

Fields are processed and displayed in a definite order, this configuration item can be used to change that order.

## Delete

> discard the `useless_field`

```json
{
    "name": "delete",
    "args": {
        "field": "useless_field"
    }
}
```

Some fields present in the data source are not useful or redundant. This configuration item allows to discard these.

## Units

Units are a way to describe the numeric values contained in a field. If a unit is set for a field, values are augmented with their symbol in the table view. See the [annotation](#annotate) chapter to learn how to set a unit for a field.

Below is a comprehensive list of units supported by the platform.

Unit name | Description
--------- | -----------
`g` | Gram
`kg` | Kilogram
`t` | Tonne
`oz` | Ounce
`lb` | Pound
`mm` | Millimeter
`cm` | Centimeter
`m` | Meter
`km` | Kilometer
`in` | Inch
`ft` | Foot
`mi` | Mile
`mm2` | Square millimeter
`cm2` | Square centimeter
`m2` | Square meter
`km2` | Square kilometer
`ha` | Hectare
`sqft` | Square feet
`acre` | Acre
`€` | Euro
`k€` | Kilo Euro
`$` | Dollar
`SAR` | SAR
`£` | British Pound
`MXN` | Mexican Peso
`seconds` | Seconds
`minutes` | Minutes
`hours` | Hours
`days` | Days
`months` | Months
`years` | Years
`Wh` | Watt hour
`kWh` | Kilowatt hour
`MWh` | Megawatt hour
`GWh` | Gigawatt hour
`TWh` | Terawatt hour
`Toe` | Tonne of oil equivalent
`bar` | Bar
`mbar` | Millibar
`Pa` | Pascal
`db` | Decibel
`W` | Watt
`kW` | Kilowatt
`MW` | Megawatt
`GW` | Gigawatt
`kVA` | Kilovolt-Ampere
`A` | Ampere
`kA` | Kiloampere
`V` | Volt
`kV` | Kilovolt
`m/s` | Meter per second
`km/s` | Kilometer per second
`km/h` | Kilometer per hour
`°C` | Celsius
`°F` | Fahrenheit
`cm3` | Cubic centimeter
`m3` | Cubic meter
`l` | Liter
`hl` | Hectoliter
`m3/s` | Cubic meter per second
`L/s` | Liter per second
`m3/h` | Cubic meter per hour
`L/h` | Liter per hour
`m3/d` | Cubic meter per day
`L/d` | Liter per day
`ppm` | Part per million
`µg/L` | Microgram per liter
`mg/L` | Milligram per liter
`μg/m3` | Microgram per cubic meter
`g/L` | Gram per liter
`kg/m3` | Kilogram per cubic meter
`%` | Percent
`°` | Degree

## Display a dataset fields specification stack

This endpoint is meant to return the list of field configuration items for a dataset. Since field configurations are exposed as [processor objects](#the-processor-object), their unique identifiers are `processor_uid`s.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/fields_specifications/
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/datasets/da_abcdef/fields_specifications/
    -u username:password
```

> Example response

```json
[{
    "name": "type",
    "args": {
        "field": "badly_named_field",
        "type": "double"
    }
}, {
    "name": "rename",
    "args": {
        "from_name": "badly_named_field",
        "to_name": "right_name",
        "label": "Super easy to understand label"
    }
}, {
    "name": "annotate",
    "args": {
        "field": "right_name",
        "annotation": "decimals",
        "args": [5]
    }
}]
```

The payload lists the fields specification stack of the dataset. Please note that it reads in the order in which the configuration is applied.

### Returns

The list of field configuration items, exposed as [processor objects](#the-processor-object).

## Add a field configuration item to a dataset

This endpoint is for adding a field configuration item for the dataset.

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/da_abcdef/fields_specifications/
```

> Example request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/fields_specifications/
    -u username:password \
    -d '{"name": "annotate", "args": {"field": "right_name", "annotation": "facet"}'
```

> Example response

```json
{
    "processor_uid": "pr_abcdfe",
    "name": "annotate",
    "args": {
        "field": "right_name",
        "annotation": "facet"
    }
}
```

The endpoint takes a processor object (without its `processor_uid`, which will be automatically generated), creates a new field configuration item with the provided arguments and appends it at the end of the fields specification chain.

### Parameters

Parameter | Description
--------- | -----------
`name` <br> *string* | name of the field configuration item
`args` <br> *object* | parameters

### Returns

The newly created field configuration item, exposed as a [processor object](#the-processor-object).

## Retrieve a field configuration item

This endpoint is meant to retrieve a field configuration item from a dataset, using its processor_uid.

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/fields_specifications/{PROCESSOR_UID}
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_abcdef/fields_specifications/pr_abcdfe
    -u username:password
```

> Example response

```json
{
    "processor_uid": "pr_abcdfe",
    "name": "annotate",
    "args": {
        "field": "right_name",
        "annotation": "facet"
    }
}
```

### Returns

The requested field configuration item, exposed as a [processor object](#the-processor-object).

## Update a field configuration item

This endpoint is meant to update a field configuration item in place within the fields specification stack.

> Definition

```
PUT https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/fields_specifications/{PROCESSOR_UID}
```

> Example request

```HTTP
curl -XPUT https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_abcdef/fields_specifications/pr_abcdfe
    -u username:password \
    -d '{"name": "annotate", "args": {"field": "other_field", "annotation": "facet"}}'
}

```

> Example response

```json
{
    "processor_uid": "pr_abcdfe",
    "name": "annotate",
    "args": {
        "field": "other_field",
        "annotation": "facet"
    }
}
```

### Parameters

Parameter | Description
--------- | -----------
`name` <br> *string* | name of the field configuration item
`args` <br> *object* | parameters

### Returns

The newly updated field configuration item, exposed as a [processor object](#the-processor-object).

## Delete a field configuration item

This endpoint is meant to delete a field configuration item from the fields specification stack of a dataset

> Definition

```HTTP
DELETE https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/fields_specifications/{PROCESSOR_UID}
```

> Example request

```HTTP
curl -XDELETE https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_abcdef/fields_specifications/pr_abcdfe
    -u username:password
```

### Returns

On successful deletion, the endpoint returns a HTTP 204 without any content.
