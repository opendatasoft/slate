# Fields specifications

Dataset field configuration can be specified using a variety of options. These options include their type, their label, whether they are a filter or not, whether they should be discarded, or even how fields are order. These configuration options are accessed using [processor-like objects](#the-processor-object).

## Available configuration

Here is a list of the different possible configuration options. Example usage for each one can be found in their dedicated section

Configuration name | Description
------------------ | -----------
[`rename`](#rename) | changes the name of the field and sets its label
[`type`](#type) | sets the field type
[`annotate`](#annotate) | annotates the field
[`description`](#description) | describes the field
[`order`](#order) | reorders fields
[`delete`](#delete) | deletes a field

## Rename

> change the field named "original_field_id" to "new_field_id", and sets its label to "desired_label"

```
{
    "name": "rename",
    "args": {
        "from_name": "original_field_id",
        "to_name": "new_field_id",
        "label": "desired_label"
    }
}
```

Fields have a unique ID, as well as a human-friendly label, both of which are editable using this configuration option.

## Type

> change the type of the field named "field_id" to a geo shape

```
{
    "name": "type",
    "args": {
        "field": "field_id",
        "type": "geo_shape"
    }
}
```

Types are the most basic way of qualifying fields. Different types unlock different kinds of visualizations and agregations. Below is the list of types sypported by the platform.

Type name | Description
--------- | -----------
`text` | textual data
`int` | integers
`double` | floating point numbers
`geo_point_2d` | 2D geographical point
`geo_shape` | geographical shape
`date` | date
`datetime` | date and time data
`image` | image
`file` | file

## Annotate

> mark the `unique_field` as the unique ID for the records

```
{
    "name": "annotate",
    "args": {
        "field": "unique_field",
        "annotation": "id"
    }
}
```

> mark the `category_field` as a facet

```
{
    "name": "annotate",
    "args": {
        "field": "category_field",
        "annotation": "facet"
    }
}
```

> make the `facetted_field` facet be sorted by descending count

```
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

```
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

```
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

```
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

```
{
    "name": "annotate",
    "args": {
        "field": "multivalued_field",
        "annotation": "multivalued",
        "args": [","]
    },
}
```

Annotation are a mean to configure special behavior for the fields. Some annotations are only available for certain field types. Setting the facet annotation unlocks other annotations for the fields.

Annotation name | Field type | Description
--------------- | ---------- | ----------
`id`|all field types | Whether this field should constitute one of the keys of the records unique IDs. If no field has this annotation, all fields contribute to the creation of the records unique ID.
`facet` | `date`, `datetime`, `int`, `decimal`, `text` | Whether the field can serve as a filter
`facetsort` | all fields type, facet only | How to sort the facets. Possible arguments are `count` and `-count` for all field types, `alphanum` and `-alphanum` for `date`, `datetime` and `text`, `num` and `-num` for `decimal` and `int`
`disjunctive` | `decimal`, `int` and `text`, facet only | Whether multiple values can be selected for the facet
`timeseries_precision` | `date` and `datetime` | precision of the field when used in a timeseries query. Possible arguments are `year`, `month` and `day` for `date`, `hour` and `minute` for `datetime` 
`timerangeFilter` | `date` and `datetime`, facet only | Whether to active the timerange filter 
`unit` | `int` and `decimal` | The unit of the field possible argument values are given [in the dedicated chapter](#units)
`decimals` | `decimal only` | The argument is the number of digits to appear after the decimal point
`sortable` | `text` | whether the field should be sortable in table view
`multivalued` | `text` | whether the field contains multiple values serparated by a character. The separator must be given as the argument
`hierarchical` | `text`, facet only | whether the field is hierarchical. The separator must be given as the argument

## Description

> give the `complicated_field` an elegant description

```
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

```
{
    "name": "order",
    "args": [
        "third_field",
        "second_field",
        "first_field"
    ]
}
```

Fields are processed and displayed in a definite order, this configuration options can be used to change that order.

## Delete

> discard the `useless_field`

```
{
    "name": "delete",
    "args": {
        "field": "useless_field"
    }
}
```

Some fields present in the data source are not useful or redundant. This configuration option allows to discard these.

## Units

Units are a way to describe the numeric values contained in a field. If a unit is set for a field, values are augmented with their symbol in the table view. See the [annotation](#annotate) chapter to learn how to set a unit for a field.

Below is a list of units supported by the platform.

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
`μg/m3` | "Microgram per cubic meter
`g/L` | Gram per liter
`kg/m3` | Kilogram per cubic meter
`%` | Percent
`°` | Degree
