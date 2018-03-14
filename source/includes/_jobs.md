# Jobs

## The job object

> Example object

```json
{}
```

These objects are returned at each call made to an [asynchronous endpoint](#asynchronous-calls). They contain all the currently available data from the asynchronous function. You may need to poll the API multiple time to get the full result.

### Attributes

Attribute | Description
--------- | -----------
`job_uid` <br> *string* | Unique identifier for the object
`function` <br> *string* | Name of the function the job is running
`params` <br> *object* | Parameters passed to the job's function
`state` <br> *string* | Current state of the job. <br> Possible values are `started`, `running`, `done`, `error`, `waiting`
`progresses` <br> *array* |
`result` <br> *object* | The job's function's response, available if `state` is `done`

## List all jobs

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/jobs
```

Returns a list of the jobs you triggered.

### Parameters

No parameters.

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/jobs \
    -u username:password
```

### Returns

List of [job objects](#the-job-object).

> Example response

```json
{

}
```

## Retrieve a job

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/jobs/{JOB_ID}
```

Retrieves the job with the given identifier.


### Parameters

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/jobs/jo_ZEXxzA \
    -u username:password
```

Parameter | Description
--------- | -----------
job_id <br> *string* | Identifier of the job to retrieve

> Example response

```json
{}
```

### Returns

Returns a [job](#the-job-object) if a valid job ID was provided. Returns an error otherwise.
