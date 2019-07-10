# Quotas and limits

Users and API keys can be limited in their usage in two ways:

- **quotas** are the maximum number of requests a user or API key can perform each day,
- **limits** are the maximum number of datasets a user can create, and the maximum number of records that can be published by the user.

## The quotas object

> Example object

```json
"quotas": {
    "limit": 1000,
    "unit": "day"
}
```

Attribute             | Description
--------------------- | -----------
`limit` <br> *number* | The number of requests that can be performed by the user in the specified time period
`unit`  <br> *string* | The time period of the limit (only `day` is supported)

## The limits object

> Example object

```json
"limits": {
    "max_datasets": 500,
    "max_records_by_dataset": 1000000
}
```

Attribute             | Description
--------------------- | -----------
`max_datasets` <br> *number*           | The maximum number of datasets that can be created by the user
`max_records_by_dataset` <br> *number* | The maximum number of records that can be published by the user
