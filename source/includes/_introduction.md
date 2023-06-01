# Introduction

> API endpoint

```text
https://mydomain.opendatasoft.com/api/management/v2
```

<aside class="warning">
  <span>
    The Management API will be deprecated in the coming months. You can now use the <a href="/apis/ods-automation-v1/">Automation API</a> (more details to come).
    <br/>
    <i>Contact your CSM or the support team if you need help to activate the feature.</i>
  </span>
</aside>

The Opendatasoft management API is organized around REST. Our API has predictable, resource-oriented URLs, and uses
HTTP response codes to indicate API errors. We use built-in HTTP features, like HTTP authentication and HTTP verbs,
which are understood by off-the-shelf HTTP clients. JSON is returned by all API responses, including errors. If not
otherwise specified, all parameters to GET calls are expected to be in the query string, and all parameters to calls
made with other verbs are expected to be sent inside a JSON object in the body of the request.
