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

If a user has at least a ruleset declared for them (directly, through a group or both), they will be able to see the union of everything each of the rulesets grants access to.

Otherwise, if nothing has been declared for them (neither directly nor through a group), they will be able to see what the default ruleset grants access to.

### The dataset security API in a nutshell

#### General security policy

`/dataset/{DATASET_UID}/security/is_access_restricted`

* `GET` [retrieve general security policy](#retrieve-the-general-accessibility-policy)
* `PUT` [set general security policy](#set-the-general-accessibility-policy)

#### Default security ruleset

`/dataset/{DATASET_UID}/security/default`

* `GET` [retrieve the default security ruleset](#retrieve-the-default-security-ruleset)
* `PUT` [update the default security ruleset](#update-the-default-security-ruleset)
* `DELETE` [reset the default security ruleset](#reset-the-default-security-ruleset)

#### User level security ruleset

`/dataset/{DATASET_UID}/security/users`

* `GET` [Retrieve all user level security rulesets](#retrieve-all-user-level-security-rulesets)
* `POST` [Create a new user level security ruleset](#create-a-new-user-level-security-ruleset)

`/dataset/{DATASET_UID}/security/users/{USERNAME}`

* `GET` [Retrieve a user level security ruleset](#retrieve-a-user-level-security-ruleset)
* `PUT` [Update a user level security ruleset](#update-a-user-level-security-ruleset)
* `DELETE` [Delete a user level security ruleset](#delete-a-user-level-security-ruleset)

#### Group level security ruleset

`/dataset/{DATASET_UID}/security/groups`

* `GET` [Retrieve all group level security rulesets](#retrieve-all-group-level-security-rulesets)
* `POST` [Create a new group level security ruleset](#create-a-new-group-level-security-ruleset)

`/dataset/{DATASET_UID}/security/groups/{group_id}`

* `GET` [Retrieve a group level security ruleset](#retrieve-a-group-level-security-ruleset)
* `PUT` [Update a group level security ruleset](#update-a-group-level-security-ruleset)
* `DELETE` [Delete a group level security ruleset](#delete-a-group-level-security-ruleset)


## The ruleset object

A set of rules defining what the target can see.

The target can be:

* a specific user
* a specific group
* anyone having access to the portal (the default ruleset) and not being affected by a user/group ruleset

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

## Retrieve the general accessibility policy

GET `datasets/<dataset_uid>/security/is_access_restricted`

## Set the general accessibility policy

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

## Create a new group level security ruleset

POST `datasets/<dataset_uid>/security/groups`

## Retrieve a group level security ruleset

GET `datasets/<dataset_uid>/security/groups/<group_id>`

## Update a group level security ruleset

PUT `datasets/<dataset_uid>/security/groups/<group_id>`

## Delete a group level security ruleset

DELETE `datasets/<dataset_uid>/security/groups/<username>`
