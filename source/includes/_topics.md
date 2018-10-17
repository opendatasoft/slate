# General

## Authentication

The management API supports API keys and basic auth for authentication.

API keys are recommended for any endpoint that supports them since they do not require using a user's password, which would provide unlimited access to the corresponding account if stolen. API keys are a way to mitigate this risk since they can be revoked easily and can be configured to provide only the necessary permissions for a given usage.

### API key

> Example authenticated request with an API key

```shell
curl https://mydomain.opendatasoft.com/api/management/v2/datasets?apikey=7f5e144f079444b20fd360cf77e9fcbe6d10b10a378d995c208796e3
```

After being generated and given appropriate permissions with the [corresponding endpoints](#api-keys), an API key can be used for every management API endpoint (unless specified in this documentation).

An API key must be passed with every authenticated request as the query parameter `apikey`.

### Basic auth

> Example authenticated request with Basic Auth

```shell
curl https://mydomain.opendatasoft.com/api/management/v2/datasets
  -u username:password
```

Basic auth credentials can be passed as the `Authorization` header, or via the authentication option any API client (e.g: curl, Postman, Python Requests, etc.) implements.

The Authorization field is constructed as follows ([Wikipedia](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side)):

- the username and password are combined with a single colon (`:`)
- the resulting string is encoded using a variant of Base64
- the authorization method and a space (e.g. "Basic ") is then prepended to the encoded string

For example, if the user has `Aladdin` as the username and `OpenSesame` as the password, then the field's value is the base64-encoding of `Aladdin:OpenSesame`, or `QWxhZGRpbjpPcGVuU2VzYW1l`.

The Authorization header will appear as:

`Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l`

Please note that this header can easily be decoded back to the original username and password, so it must never be shared with anyone.

## Errors

> Example error

```json
{
  "status_code": 404,
  "error_key": "UnknownUsernameException",
  "message": "Unknown username: toto",
  "raw_message": "Unknown username: {username}",
  "raw_params": {
    "username": "toto"
  }
}
```

All errors raised by the platform follow a common pattern. They will be rendered as an HTTP response with the proper
HTTP status code (400, 404 etc.) and with a body describing the error.

> Wrapped errors

```json
{
  "status_code": 400,
  "error_key": "InvalidManagementAPIRequestException",
  "message": "Invalid management API request",
  "raw_message": "Invalid management API request",
  "raw_params": {},
  "errors": [
	]
}
```

When updating a resource, you may get multiple errors because multiple properties of the object you provided in the
payload have issues. In this case, these errors will be returned together, wrapped with a meta error.

## Asynchronous calls

> Example asynchronous request

```HTTP
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXX/publish \
    -X PUT \
    -u username:password
```

> Example response

```json
{
  "job_id": "86a5eaf857201d3e11e67427b205121e7d19d77d"
}
```

While most API calls are synchronous, a few are not due to the impredictable nature of their execution time.

For example, publishing a dataset can be almost instantaneous but could also go on for hours depending on the size of the dataset and the complexity of the processing pipeline.

These calls will return instantaneously with a job identifier that you can then use to poll for a status update. Once the
action is over, the poll's response will contain the action's response.

<aside class="important">
<p>Asynchronous URLs all end with a verb.</p>
<p>E.g. <code>/datasets/preview_resource</code></p>
</aside>


## Expanding objects

> Example non-expand request

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXX/security/users
```

> Example response

```json
[
  {
    "is_data_visible": true,
    "visible_fields": [],
    "filter_query": "",
    "api_calls_quota": null,
    "permissions": [
      "explore_restricted_dataset",
      "edit_dataset",
      "publish_dataset"
    ],
    "user": {
      "username": "myuser"
    }
  },
  {...},
  {...}
]
```

> Example expand request

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXX/security/users?expand=user
```

> Example response

```json
[
  {
    "is_data_visible": true,
    "visible_fields": [],
    "filter_query": "",
    "api_calls_quota": null,
    "permissions": [
      "explore_restricted_dataset",
      "edit_dataset",
      "publish_dataset"
    ],
    "user": {
      "username": "myuser",
      "first_name": "First name",
      "last_name": "Last name",
      "email": "myuser@example.com",
      "is_active": true,
      "is_ods": false
    }
  },
  {...},
  {...}
]
```

Many objects contain the identifier of a related object in their response properties. For example, a dataset security user ruleset will have an associated user. This object can be expanded inline with the expand request parameter. Objects that can be expanded are noted in this documentation. This parameter is available on all API requests, and applies to the response of that request only.

## Datetime objects

> Example date

> July 4th 2017, 11 hours 13 minutes and 53 seconds

```text
2017-07-04T11:13:53
```

All datetime objects returned in this API are represented in ISO 8601, that is `YYYY-MM-DDTHH:MM:SS`. They are all UTC dates.

## Required parameters

Unless explicity declared as optional, all API parameters are required.
