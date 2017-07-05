# Misc objects

## The quota object

The quota object defines an upper limit within a given timeframe.

> Example object

> 10000 api calls per day

```json
{
    "limit": 10000,
    "unit": "day"
}
```

### Attributes

Attribute | Description
--------- | -----------
`limit` <br> *integer* | Upper limit
`unit` <br> *string* | Timeframe. <br> Possibile values are `hour`, `day`, `month`