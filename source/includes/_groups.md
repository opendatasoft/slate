# Groups

A group is an entity comprising several users. When users are added to a group, they benefit from the permissions, quotas and limits of this group.

Through the management API, the following can be performed on the current domain:

- list groups,
- lookup a specific group,
- create groups,
- grant groups permissions, quotas and limits,
- list, add and delete users in groups,
- delete groups

## The Group object

> Example object

```json
{
    "title": "My Users",
    "group_id": "my-users",
    "user_count": 1,
    "permissions": [
        "publish_dataset",
        "edit_dataset"
    ],
    "limits": {
        "max_records_by_dataset": 1000000,
        "max_datasets": 500
    },
    "quotas": {
        "limit": 1000,
        "unit": "day"
    }
}
```

Attribute | Description
--------- | -----------
`title` <br> *string*      | The group title
`group_id` <br> *string*   | The group identifier
`user_count` <br> *number* | The count of users in the group
`permissions` <br> *array* | A list of permissions granted to these group members
`quotas` <br> *[quotas object](#the-quotas-object)* | An object holding the group's quotas on this domain
`limits` <br> *[limits object](#the-limits-object)* | An object holding the group's limits on this domain

## List groups

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/groups/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/groups/ \
    -u username:password
```

> Example response

```json
[
    {
        "title": "My Users",
        "group_id": "my-users",
        "user_count": 1,
        "permissions": [
            "publish_dataset",
            "edit_dataset"
        ],
        "limits": {
            "max_records_by_dataset": 1000000,
            "max_datasets": 500
        },
        "quotas": {
            "limit": 1000,
            "unit": "day"
        }
    },
    {...},
    {...}
]
```

This endpoint lists all the groups linked to the domain.

### Returns

Returns a list of Group objects.

## Create a group on the domain

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/groups/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/groups/ \
    -X POST \
    -u username:password \
    -d '{"title": "An API group"}'
```

> Example response

```json
{
    "user_count": 0,
    "limits": {},
    "title": "An API group",
    "quotas": {},
    "group_id": "an-api-group",
    "permissions": []
}
```

Creates a new empty group with a title on the domain.

### Body

Parameter | Description
--------- | -----------
`title` <br> *string* | The group title

### Returns

Returns the newly created Group object.

## Retrieve a group

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/groups/<group_id>/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/groups/my-users/ \
    -u username:password
```

> Example response

```json
{
    "title": "My Users",
    "group_id": "my-users",
    "user_count": 1,
    "permissions": [
        "publish_dataset",
        "edit_dataset"
    ],
    "limits": {
        "max_records_by_dataset": 1000000,
        "max_datasets": 500
    },
    "quotas": {
        "limit": 1000,
        "unit": "day"
    }
}
```

This endpoint retrieves the requested group.

### Returns

Returns a Group object.

## Update a group

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/groups/<group_id>/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/groups/my-users/ \
    -X PUT \
    -u username:password \
    -d '{"title": "My favorite users", "permissions": ["publish_dataset"]}'
```

> Example response

```json
{
    "title": "My favorite users",
    "group_id": "my-users",
    "user_count": 1,
    "permissions": [
        "publish_dataset"
    ],
    "limits": {
        "max_records_by_dataset": 1000000,
        "max_datasets": 500
    },
    "quotas": {
        "limit": 1000,
        "unit": "day"
    }
}
```

Update an existing group.

### Body

Parameter | Description
--------- | -----------
`title` <br> *string*       | **optional** The group title
`permissions` <br> *array*  | **optional** A list of permissions to grant the group
`quotas` <br> *[quotas object](#the-quotas-object)* | **optional** An object holding the quotas to grant the group
`limits` <br> *[limits object](#the-limits-object)* | **optional** An object holding the limits to grant the group

### Returns

Returns a Group object.

## Delete a group

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/groups/<group_id>/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/groups/my-users/ \
    -X DELETE \
    -u username:password
```

> Example response

```json
{}
```

Delete a group.

### Returns

Returns an empty object.


## List users in a group

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/groups/<group_id>/users/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/groups/my-users/users/\
    -u username:password
```

> Example response

```json
{
    "users": [
        {
            "username": "louise.von-data",
            "first_name": "Louise",
            "last_name": "Von Data",
            "is_ods": false,
            "is_active": true,
            "email": null
        }
    ],
    "rows": 10,
    "page": 1,
    "nhits": 1
}
```

This endpoint lists all the users in a group.

### Returns

Returns a paginated list of partial User objects (see [The User object](#the-user-object)).

## Add users in a group

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/groups/<group_id>/users/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/groups/my-users/users/ \
    -X POST \
    -u username:password \
    -d '{"usernames":["bruce.von-data", "louise.von-data"]}'
```

> Example response

```json
{
    "bruce.von-data": "success",
    "louise.von-data": "duplicate"
}
```

Adds a list of users (identified by their username) in a group.

### Body

Parameter | Description
--------- | -----------
`usernames` <br> *array* | A list of usernames that identify domain users

### Returns

Returns a JSON object with requested usernames as keys and a status for the corresponding username as values.

Status    | Description
--------- | -----------
`success`     | The user was successfully added to the group
`duplicate`   | The user has not been added to the group because they were already a member
`error`       | The user has not been added to the group because of an error

## Remove a user from a group

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/groups/<group_id>/users/<username>
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/groups/my-users/users/bruce.von-data \
    -X DELETE \
    -u username:password \
```

Removes a user from a group

### Returns

Returns an empty response.
