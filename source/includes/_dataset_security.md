# Dataset security

The dataset security is defined through 3 variables:

* a global accessibility policy
* specific rulesets for users and groups
* a default ruleset that applies to anybody else

### Restricted datasets

If the dataset is [set as restricted](#set-the-global-accessibility-policy), then the dataset will only appear in the catalog for users who have a ruleset declared for them, either directly or through a group. Other users won't have any access to the dataset.

As a result, the default security ruleset has no meaning for restricted datasets.

### Unrestricted datasets

All people having access to the domain will be able to see the dataset in the catalog.

If a user has at least ruleset declared for him/her (directly, through a group or both), he/she will be able to see the union of everything each of the rulesets grants access to.

Otherwise, if nothing has been declared for him/her (neither directly nor through a group), he/she will be able to see what the default ruleset grants access to.

## The ruleset object

A set of rules defining what the target can see.

The target can be:

* anyone having access to the portal (the default ruleset)
* a specific user
* a specific group

> Example object

```json
{
    "is_data_visible": true,
    "visible_fields": ["field1", "field2"],
    "filter_query": "",
    "api_calls_quota": {
        "limit": 10000,
        "unit": "day"
    },
    "permissions": [],
    "user": {
        "username": "username"
    }
}
```

### Attributes

Attribute | Description
--------- | -----------
`visible_fields` <br> *array of field names (string)* | The target will only have access to the fields from this list. <br> `['*']` means that the target has access to all fields. <br> An empty list means that the target won't see any field (empty dataset schema).
`is_data_visible` <br> *boolean* | Flag indicating whether the target will have access the dataset's records or not.
`filter_query` <br> *string* | The target will only have access to the records matching this query. An empty query means that all records are accessible.
`permissions` <br> *array of strings* | List of special permissions granted to the target. <br> Only available for user and group-level rulesets. <br> Possible values are `edit_dataset`, `publish_dataset`, `manage_dataset`
`api_calls_quota` <br> *[quota object](#the-quota-object)* | Upper limit set on the number of api calls the target can make to this dataset in a given timeframe. <br> Can be set to null for no specific quota.
`user` <br> *[user object](#the-user-object)* <br> <em class="expandable">expandable</em> | The user targeted by this ruleset. <br> Only available for user-level rulesets.
`group` <br> *[group object](#the-group-object)* <br> <em class="expandable">expandable</em> | The group targeted by this ruleset. <br> Only available for group-lebel rulesets.

<aside>
    Setting <code>is_data_visible</code> to <code>false</code> will void the effect of the <code>filter_query</code> value. No data at all will be visible by the target.
</aside>

## Retrieve the global accessibility policy

GET `datasets/<dataset_uid>/security/is_access_restricted`

## Set the global accessibility policy

PUT `datasets/<dataset_uid>/security/is_access_restricted`

## Retrieve the default security ruleset

Retrieves the default security ruleset, that is the ruleset that applies when no more specific ruleset is declared for the user.

> Definition

```http
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/security/default
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/security/default \
    -u username:password
```

> Example response

```json
{
    "is_data_visible": false,
    "visible_fields": ["field1", "field2"],
    "filter_query": "",
    "api_calls_quota": null,
    "permissions": []
}
```

## Update the default security ruleset

PUT `datasets/<dataset_uid>/security/default`

## Reset the default security ruleset

DELETE `datasets/<dataset_uid>/security/default`

## Retrieve all user level security rulesets

Retrieves all rulesets defined for specific users. The rulesets are ordered by ascending username.

> Definition

```http
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/security/users
```

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
        "is_data_visible": false,
        "visible_fields": ["field1", "field2"],
        "filter_query": "",
        "api_calls_quota": null,
        "permissions": []
    },
    {...},
    {...}
]
```

## Create a new user level security ruleset

POST `datasets/<dataset_uid>/security/users/`

## Retrieve a user level security ruleset

Retrieves the ruleset defined for a specific user. Returns an error if no ruleset is defined for the user.


> Definition

```http
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/security/users/{USERNAME}
```

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
    "is_data_visible": false,
    "visible_fields": ["field1", "field2"],
    "filter_query": "",
    "api_calls_quota": null,
    "permissions": []
}
```

## Update a user level security ruleset

Updates the ruleset defined for the given user. Returns an error if no such ruleset is defined.

> Definition

```http
PUT https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/datasets/{DATASET_UID}/security/users/{USERNAME}
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/datasets/da_XXXXXX/security/users/username \
    -u username:password
    -X PUT \
    -d '{"user": {"username": "username"}, "is_data_visible": true, "visible_fields": [], "filter_query": "", "api_calls_quota": null, "permissions": []}'
```

> Example response

```json
{
    "user": {
        "username": "username"
    },
    "is_data_visible": true,
    "visible_fields": [],
    "filter_query": "",
    "api_calls_quota": null,
    "permissions": []
}
```

## Delete a user level security ruleset

DELETE `datasets/<dataset_uid>/security/users/<username>`

## Retrieve all group level security rulesets

GET `datasets/<dataset_uid>/security/groups/`

## Create a group level security ruleset

POST `datasets/<dataset_uid>/security/groups`

## Retrieve a group level security ruleset

GET `datasets/<dataset_uid>/security/groups/<group_id>`

## Update a group level security ruleset

PUT `datasets/<dataset_uid>/security/groups/<group_id>`

## Delete a new group level security ruleset

DELETE `datasets/<dataset_uid>/security/groups/<username>`
