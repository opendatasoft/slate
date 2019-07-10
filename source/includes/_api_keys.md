# API keys

API keys are randomly generated passwords that can be used as an authentication method to access a protected API endpoint as an authorized user.

Through the management API, it is possible to list, create, lookup, update and delete API keys for one's own user.

## The API key object

> Example object

```json
{
    "key": "7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3",
    "label": "My first API key",
    "permissions": [
        "edit_dataset",
        "explore_restricted_dataset"
    ]
}
```

Attribute | Description
--------- | -----------
`key` <br> *string*        | The API key
`label` <br> *string*      | A label describing this key
`permissions` <br> *array* | The list of permissions granted to this API key

## List API keys

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/apikeys/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/apikeys/ \
    -u username:password
```

> Example response

```json
[
    {
        "key": "7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3",
        "label": "My first API key",
        "permissions": [
            "edit_dataset",
            "explore_restricted_dataset"
        ]
    },
    {...},
    {...}
]
```

This endpoint lists all the API keys belonging to the user.

If the request is made with an API key, only this API key will be present in the response.

### Returns

Returns a list of API keys objects.

## Create an API key

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/apikeys/
```

> Example request for an empty API key

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/apikeys/ \
    -X POST \
    -u username:password \
    -d '{}'
```

> Example response for an empty API key

```json
{
    "key": "7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3",
    "label": null,
    "permissions": [
        "explore_restricted_dataset"
    ]
}
```

> Example request providing a label

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/apikeys/ \
    -X POST \
    -u username:password
    -d '{"label": "My own label"}'
```

> Example response with the provided label

```json
{
    "key": "7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3",
    "label": "My own label",
    "permissions": [
        "explore_restricted_dataset"
    ]
}
```

> Example request providing a label and permissions

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/apikeys/ \
    -X POST \
    -u username:password \
    -d '{"label": "My own label", "permissions": ["edit_dataset", "publish_dataset"]}'
```

> Example response with the provided label

```json
{
    "key": "7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3",
    "label": "My own label",
    "permissions": [
        "edit_dataset",
        "publish_dataset"
    ]
}
```

Creates a new API key.

This endpoint can not be accessed with an API key.

### Body

Parameter | Description
--------- | -----------
`label` <br> *string*      | **optional** A label describing this key
`permissions` <br> *array* | **optional** The list of permissions granted to this API key

### Returns

Returns an API key object.

## Retrieve an API key

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/apikeys/<KEY>
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/apikeys/7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3/ \
    -u username:password
```

> Example response

```json
{
    "key": "7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3",
    "label": "My first API key",
    "permissions": [
        "edit_dataset",
        "explore_restricted_dataset"
    ]
}
```

This endpoint retrieves the requested API key.

If the request is made with an API key, only this API key can be retrieved.

### Returns

Returns an API key object.

## Update an API key

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/apikeys/7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3/
```

> Example request providing a label

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/apikeys/7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3/ \
    -X PUT \
    -u username:password \
    -d '{"label": "My own label"}'
```

> Example response with the provided label

```json
{
    "key": "7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3",
    "label": "My own label",
    "permissions": [
        "edit_dataset",
        "explore_restricted_dataset"
    ]
}
```

> Example request providing a label and permissions

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/apikeys/7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3/ \
    -X PUT \
    -u username:password \
    -d '{"label": "My own label", "permissions": ["edit_dataset", "publish_dataset"]}'
```

> Example response with the provided label

```json
{
    "key": "7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3",
    "label": "My own label",
    "permissions": [
        "edit_dataset",
        "publish_dataset"
    ]
}
```

> Example request for an empty API key (invalid)

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/apikeys/7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3/ \
    -X PUT \
    -u username:password \
    -d '{}'
```

> Example response for an empty API key

```json
{
    "status_code": 400,
    "message": "'permissions' or 'label' must be provided to update an API key",
    "raw_params": {},
    "raw_message": "'permissions' or 'label' must be provided to update an API key",
    "error_key": "PermissionsOrLabelMissingFromAPIKeyUpdateException"
}
```

Update an existing API key.

This endpoint can not be accessed with an API key.

### Body

Parameter | Description
--------- | -----------
`label` <br> *string*      | **optional** A label describing this key
`permissions` <br> *array* | **optional** The list of permissions granted to this API key

### Returns

Returns an API key object.

## Delete an API key

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/apikeys/7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/apikeys/7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3/ \
    -X DELETE \
    -u username:password
```

Delete an existing API key.

This endpoint can not be accessed with an API key.

### Returns

Returns an empty response (code: 204).
