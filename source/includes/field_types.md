# Field types

Record's values are typed and one of the following:

* text
* int
* double
* datetime
* date
* geo_point
* geo_shape
* file

## Text

> Example value

```json
I am a text value
```

Anything.

## Int

> Example value

```json
123
```

An integer value, between - (2 ** 63) and (2 ** 63) - 1 # FIXME

## Double

> Example value

```json
3.14
```

A decimal value.


## Datetime

> Example value

```json
2015/02/11-08:09:10
```

A datetime value, like 2015/02/11-08:09:10 or 2015-02-11T08:09:10 or 02/11/2015 08:09:10 ... 

## Date

> Example value

```json
2015/02/11
```

A datetime value, like 2015/02/11 or 2015-02-11 or 02/11/2015 ... 

## Geo Point

> Example value

```json
45.8, 2.5
```

A single geographical location expressed in the format <LAT>,<LON>.

## Geo Shape

> Example value

```json
{
    "type": "LineString",
    "coordinates": [ [100.0, 0.0], [101.0, 1.0] ]
}
```

A valid geo shape expressed in GeoJSON.

## File

A file. Created from a File processor or a specific extractor.
