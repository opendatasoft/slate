# General

## Authentication

The API currently only supports basic auth for authentication.

Both username and password must be specified with each call.

```shell
curl https://mydomain.opendatasoft.com/management/api/v2/datasets/
  -u username:password
```

## Errors

> Sample error

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

While most API calls are synchronous, a few are not due to the impredictable nature of their execution time. Publishing
a dataset for example can be almost instantaneous but could also go on for hours depending on the size of the dataset
and the complexity of the processing pipeline.

These calls will return instantaneously with a job identifier that you can then use to poll for a status update. Once the
action is over, the poll's response will contain the action's response.

<aside class="important">
<p>Asynchronous URLs all end with a verb.</p>
<p>E.g. <code>/datasets/preview_resource</code></p>
</aside>

> Example asynchronous request

```HTTP
curl
```

## Expanding objects

Many objects contain the identifier of a related object in their response properties. For example, a Dataset will have associated Metadata values. Those objects can be expanded inline with the expand request parameter. Objects that can be expanded are noted in this documentation. This parameter is available on all API requests, and applies to the response of that request only.

You can nest expand requests with the dot property. For example, requesting metadata.definition on a charge will expand the each metadata value into a full Metadata object, and will then expand the definition property on that metadata value into a full Metadata Definition object.

You can expand multiple objects at once by identifying multiple items in the expand array.

> Example request

```shell
```

> Example response

```json
{

}
```

> Example request

```shell
```

> Example response

```json
{

}
```

## Datetime objects

All datetime objects returned in this API are represented in ISO 8601, that is `YYYY-MM-DDTHH:MM:SS`. They are all UTC dates.

> Example date

> July 4th 2017, 11 hours 13 minutes and 53 seconds

```text
2017-07-04T11:13:53
```