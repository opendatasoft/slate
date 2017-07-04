# Dataset security

## The security object

A set of rules defining what the target can see.

The target can be:

* anyone having access to the portal (the default ruleset)
* a specific user
* a specific group

<aside>
    <p>Only the most specific defined ruleset applies!</p>
    <p>User level rulesets are the most specific, followed by the group level rulesets and the default ruleset is the less specific.</p>
</aside>

### Attributes

Attribute | Description
--------- | -----------
`metadata_only` <br> *boolean* | Flag indicating whether the target will have access the dataset's metadata values
`fields` <br> *array of field names (string)* | The target will only have access to the fields from this list. An empty list means that all fields are accessible.
`filter_query` <br> *string* | The target will only have access to the records matching this query. An empty query means that all records are accessible.
`user` <br> *[user object](#the-user-object)* <br> <em class="expandable">expandable</em> | The user targeted by this ruleset. Only available for user-level rulesets.
`group` <br> *[group object](#the-group-object)* <br> <em class="expandable">expandable</em> | The group targeted by this ruleset. Only available for group-lebel rulesets.

<aside>
    Setting `metadata_only` to `true` will void the effect of the `fields` and `filter_query` value.

    -> TODO: access to data schema with metadata_only=true ? yes or no ? I'd say no (leaking information).
</aside>

* `datasets/<dataset_uid>/security/is_private` GET / PUT
* `datasets/<dataset_uid>/security/default` GET / PUT / DELETE
* `datasets/<dataset_uid>/security/users` GET / POST
* `datasets/<dataset_uid>/security/users/<username>` GET / PUT / DELETE
* `datasets/<dataset_uid>/security/groups` GET / POST
* `datasets/<dataset_uid>/security/groups/<group_id>` GET / PUT / DELETE

## Retrieve the default security ruleset

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/security/default \
    -u username:password
```

> Example response

```json
{
    "metadata_only": false,
    "fields": ["field1", "field2"],
    "filter_query": ""
}
```

## Retrieve all user level security rulesets

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/security/users \
    -u username:password
```

> Example response

```json
[
    {
        "user": {
            "username": "username"
        },
        "metadata_only": false,
        "fields": ["field1", "field2"],
        "filter_query": ""
    },
    {...},
    {...}
]
```

## Retrieve a user level security ruleset

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/security/users/username \
    -u username:password
```

> Example response

```json
{
    "user": {
        "username": "username"
    },
    "metadata_only": false,
    "fields": ["field1", "field2"],
    "filter_query": ""
}
```

## Update a user level security ruleset

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/security/users/username \
    -u username:password
    -X PUT \
    -d '{"user": {"username": "username"}, "metadata_only": true, "fields": [], "filter_query": ""}'
```

> Example response

```json
{
    "user": {
        "username": "username"
    },
    "metadata_only": true,
    "fields": [],
    "filter_query": ""
}
```
