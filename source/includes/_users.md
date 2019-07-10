# Users

A user is a person who authentifies themself to utilize the platform.

Most of the times, users are invited on a domain via an e-mail:

- if the user doesn't have an Opendatasoft account, the e-mail provides them a link to create their account and choose a password,

- this invitation links the new user or existing user to this domain, allowing domain administrator to grant them permissions to perform specific actions.

In other words, user accounts are shared between all Opendatasoft domains, but a user must be linked to a specific domain via an invitation before being granted specific permissions on this domain.

Through the management API, it is possible to:

- list users linked to the domain,
- lookup a specific user,
- invite users on the domain (via an e-mail address),
- grant users permissions, quotas and limits on the domain,
- add or remove them from groups,
- delete users from the domain.

## The User object

> Example object

```json
{
    "username": "louise.von-data",
    "first_name": "Louise",
    "last_name": "Von Data",
    "email": "louise.von-data@opendatasoft.com",
    "account_type": "global",
    "display_name": "louise.von-data",
    "auth_provider_types": [],
    "permissions": [
        "explore_restricted_dataset",
        "edit_dataset"
    ],
    "groups": [
        {
            "user_count": 1,
            "limits": {},
            "title": "Example Group",
            "quotas": {},
            "group_id": "example-group",
            "permissions": ["create_dataset"]
        }
    ],
    "is_active": true,
    "date_joined": "2018-05-02T09:36:30.531746+00:00",
    "limits": {},
    "is_ods": false,
    "quotas": {},
    "datasets_index_filters": [
        "publishing.published",
        "publishing.status",
        "visibility"
    ],
    "last_seen": "2018-05-03T12:51:50.250382+00:00"
}
```

Attribute | Description
--------- | -----------
`username` <br> *string*        | The user's username
`first_name` <br> *string*      | The user's first name
`last_name` <br> *string*       | The user's last name
`email` <br> *string*           | The user's e-mail address
`account_type` <br> *string*    | The user's account type.<br> Possible values are `global`, `linked` and `local`
`display_name` <br> *string*    | The user's display name<br>simplified version of the `username`
`auth_provider_types` <br> *array of string*    | The list of authentification providers type for this user.<br> Currently `saml` is the only available provider.
`permissions` <br> *array*      | A list of permissions granted to this user
`groups` <br> *array*           | A list of groups the user belongs to
`is_active` <br> *boolean*      | True if the user can connect to their account
`date_joined` <br> *date*       | The date when the user joined the domain
`is_ods` <br> *boolean*         | True if the user belongs to the Opendatasoft organization
`quotas` <br> *[quotas object](#the-quotas-object)*   | An object holding the user's quotas on this domain
`limits` <br> *[limits object](#the-limits-object)*   | An object holding the user's limits on this domain
`datasets_index_filters` <br> *string*     | The user's filter preferences on the dataset index
`last_seen` <br> *string*       | The date when the user used their account for the last time

## List users

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/users/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/users/ \
    -u username:password
```

> Example response

```json
[
    {
        "username": "louise.von-data",
        "first_name": "Louise",
        "last_name": "Von Data",
        "email": "louise.von-data@opendatasoft.com",
        "account_type": "global",
        "display_name": "louise.von-data",
        "auth_provider_types": [],
        "permissions": [
            "explore_restricted_dataset",
            "edit_dataset"
        ],
        "groups": [
            {
                "user_count": 1,
                "limits": {},
                "title": "Example Group",
                "quotas": {},
                "group_id": "example-group",
                "permissions": ["create_dataset"]
            }
        ],
        "is_active": true,
        "date_joined": "2018-05-02T09:36:30.531746+00:00",
        "limits": {},
        "is_ods": false,
        "quotas": {},
        "datasets_index_filters": [
            "publishing.published",
            "publishing.status",
            "visibility"
        ],
        "last_seen": "2018-05-03T12:51:50.250382+00:00"
    },
    {...},
    {...}
]
```

This endpoint lists all the users linked to the domain.

### Returns

Returns a list of User objects.

## Invite users to the domain

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/users/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/users/ \
    -X POST \
    -u username:password \
    -d '{"emails": ["louise.von-data@opendatasoft.com", "bruce.von-data@opendatasoft.com"]}'
```

> Example response (no error)

```json
{
    "louise.von-data@opendatasoft.com": "success: louise.von-data",
    "bruce.von-data@opendatasoft.com": "success: bruce.von-data"
}
```

> Example request (with errors)

```shell
curl http://yourdomain.opendatasoft.com/api/management/v2/users/ \
    -X POST \
    -u username:password
    -d '{"emails": ["louise.von-data@opendatasoft.com", "bruce.von-data"]}'
```

> Example response (with errors)

```json
{
    "bruce.von-data": "invalid-email",
    "louise.von-data@opendatasoft.com": "already-member"
}
```

Sends an invitation e-mail to a list of e-mail addresses.

### Body

Parameter | Description
--------- | -----------
`emails` <br> *array*      | A list of e-mail addresses to invite on the domain

### Returns

Returns a JSON object with requested e-mail addresses as keys and a status for the corresponding e-mail address as values.

Status    | Description
--------- | -----------
`success: <username>` | The invitation was successfully sent, and the newly invited user will have `<username>` as a username. The mentioned username can either correspond to a user that already exists to a newly created user if they did not have an Opendatasoft account yet.
`already-member`   | The provided e-mail address corresponds to a user already linked to the domain
`invalid-email`    | The provided e-mail address is invalid
`forbidden-email`  | The provided e-mail address can not be invited on an Opendatasoft domain
`license-users-exceeded` | The domain license does not allow to invite more users

## Retrieve a user

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/users/<username>/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/users/louise.von-data/ \
    -u username:password
```

> Example response

```json
{
    "username": "louise.von-data",
    "first_name": "Louise",
    "last_name": "Von Data",
    "email": "louise.von-data@opendatasoft.com",
    "account_type": "global",
    "display_name": "louise.von-data",
    "auth_provider_types": [],
    "permissions": [
        "explore_restricted_dataset",
        "edit_dataset"
    ],
    "groups": [
        {
            "user_count": 1,
            "limits": {},
            "title": "Example Group",
            "quotas": {},
            "group_id": "example-group",
            "permissions": ["create_dataset"]
        }
    ],
    "is_active": true,
    "date_joined": "2018-05-02T09:36:30.531746+00:00",
    "limits": {},
    "is_ods": false,
    "quotas": {},
    "datasets_index_filters": [
        "publishing.published",
        "publishing.status",
        "visibility"
    ],
    "last_seen": "2018-05-03T12:51:50.250382+00:00"
}
```

This endpoint retrieves the requested user.

### Returns

Returns a User object.

## Update an user

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/users/<username>/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/users/louise.von-data/ \
    -X PUT \
    -u username:password \
    -d '{"group_ids": ["another-group"], "permissions": ["publish_dataset"]}'
```

> Example response

```json
{
    "username": "louise.von-data",
    "first_name": "Louise",
    "last_name": "Von Data",
    "email": "louise.von-data@opendatasoft.com",
    "account_type": "global",
    "display_name": "louise.von-data",
    "auth_provider_types": [],
    "permissions": [
        "publish_dataset"
    ],
    "groups": [
        {
            "user_count": 1,
            "limits": {},
            "title": "Another group",
            "quotas": {},
            "group_id": "another-group",
            "permissions": ["edit_page"]
        }
    ],
    "is_active": true,
    "date_joined": "2018-05-02T09:36:30.531746+00:00",
    "limits": {},
    "is_ods": false,
    "quotas": {},
    "datasets_index_filters": [
        "publishing.published",
        "publishing.status",
        "visibility"
    ],
    "last_seen": "2018-05-03T12:51:50.250382+00:00"
}
```

Update an existing user.

### Body

Parameter | Description
--------- | -----------
`group_ids` <br> *array*    | **optional** A list of group identifiers to add the user to
`permissions` <br> *array*  | **optional** A list of permissions to grant the user
`quotas` <br> *[quotas object](#the-quotas-object)* | **optional** An object holding the quotas to grant the user
`limits` <br> *[limits object](#the-limits-object)* | **optional** An object holding the limits to grant the user

### Returns

Returns a User object.

## Remove a user from the domain

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/users/<username>/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/users/louise.von-data/ \
    -X DELETE \
    -u username:password
```

This endpoint removes the requested user from the domain.

### Returns

On success the endpoint returns an empty 204 HTTP response. If the user is the only domain administrator left, the call will fail and an error specifying that a removal of the only domain administrator is unallowed will be returned.