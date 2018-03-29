# Pages security

The page security is the set of rules that defines who (which users / groups) can explore or edit a given page.

It is defined through 2 variables:

* a page restriction through the `restricted` attribute in [the page object](#the-page-object), which defines if a page is visible to every user who can explore the portal
* specific rulesets for users and groups

If the page is set as restricted, then the page will only appear in the portal for users who have a ruleset declared for them, either directly or through a group. Other users won't have any access to the page.

Rulesets can also give users permission to edit the page and manage its security.

### The page security API in a nutshell

#### User level page security ruleset

`/pages/{PAGE_SLUG}/security/users`

* `GET` [Retrieve all user level page security rulesets](#retrieve-all-user-level-page-security-rulesets)
* `POST` [Create a new user level page security ruleset](#create-a-user-level-page-security-ruleset)

`/pages/{PAGE_SLUG}/security/users/{USERNAME}`

* `GET` [Retrieve a user level page security ruleset](#retrieve-a-user-level-page-security-ruleset)
* `PUT` [Update a user level page security ruleset](#update-a-user-level-page-security-ruleset)
* `DELETE` [Delete a user level page security ruleset](#delete-a-user-level-page-security-ruleset)

#### Group level page security ruleset

`/pages/{PAGE_SLUG}/security/groups`

* `GET` [Retrieve all group level page security rulesets](#retrieve-all-group-level-page-security-rulesets)
* `POST` [Create a new group level page security ruleset](#create-a-group-level-page-security-ruleset)

`/pages/{PAGE_SLUG}/security/groups/{GROUP_ID}`

* `GET` [Retrieve a group level page security ruleset](#retrieve-all-group-level-page-security-rulesets)
* `PUT` [Update a group level page security ruleset](#update-a-group-level-page-security-ruleset)
* `DELETE` [Delete a group level security ruleset](#delete-a-group-level-page-security-ruleset)

## The page security ruleset object

> Example object

```json
{
    "permissions": [],
    "created_at": "2018-03-28T13:17:13.302632+00:00",
    "updated_at": "2018-03-28T13:17:13.302632+00:00",
    "user": {
        "username": "john.doe"
    },
    "group": {
        "group_id": "your.group"
    },
    "page": {
        "domain": {
            "domain_id": "yourdomain"
        },
        "slug": "my-page"
    }
}
```
### Attributes

Attribute | Description
--------- | -----------
`permissions` <br> *array of strings* | List of special permissions granted to the target. Possible values are `edit_page` and `manage_page`
`created_at` <br> *datetime*  | Date when the ruleset was created
`updated_at` <br> *datetime*  | Date when the ruleset was last edited
`page` <br> *[page object](#the-page-object)* <br> <em class="expandable">expandable</em> | The page targeted by this ruleset
`user` <br> *[user object](#the-user-object)* <br> <em class="expandable">expandable</em> | The user targeted by this ruleset. <br> Only available for user-level rulesets
`group` <br> *[group object](#the-group-object)* <br> <em class="expandable">expandable</em> | The group targeted by this ruleset. <br> Only available for group-level rulesets

## Retrieve all user level page security rulesets

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/users
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/users \
    -u username:password
```

> Example response

```json
[
    {
      "permissions": [],
      "created_at": "2018-03-28T13:17:13.302632+00:00",
      "updated_at": "2018-03-28T13:17:13.302632+00:00",
      "user": {
          "username": "john.doe"
      },
      "page": {
          "domain": {
              "domain_id": "yourdomain"
          },
          "slug": "my-page"
      }
    },
    {...},
    {...}
]
```

This endpoint is for retrieving all rulesets defined for the page with provided `slug`.

### Parameters

No parameters.

### Returns

Returns a list of [page security ruleset objects](#the-page-security-ruleset-object).

## Retrieve a user level page security ruleset

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/users/{USERNAME}
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/users/john.doe \
    -u username:password
```

> Example response

```json
{
    "permissions": [],
    "created_at": "2018-03-28T13:17:13.302632+00:00",
    "updated_at": "2018-03-28T13:17:13.302632+00:00",
    "user": {
        "username": "john.doe"
    },
    "page": {
        "domain": {
            "domain_id": "yourdomain"
        },
        "slug": "my-page"
    }
}
```

This endpoint is for retrieving the user level security ruleset object with provided `username`.

### Parameters

No parameters.

### Returns

Returns the user level [page security ruleset object](#the-page-security-ruleset-object).

## Create a user level page security ruleset

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/users
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/users \
    -X POST \
    -u username:password \
    -d '{"permissions": ["edit_page"], "user": {"username": "john.doe"}}'
```

> Example response

```json
{
    "permissions": ["edit_page"],
    "created_at": "2018-03-28T13:17:13.302632+00:00",
    "updated_at": "2018-03-28T13:17:13.302632+00:00",
    "user": {
        "username": "john.doe"
    },
    "page": {
        "domain": {
            "domain_id": "yourdomain"
        },
        "slug": "my-page"
    }
}
```

This endpoint is for creating a new user level security ruleset.

### Parameters

No parameters

### Body

Parameter | Description
--------- | -----------
`permissions` <br> *array of strings* | List of special permissions granted to the user. Possible values are `edit_page` and `manage_page`
`user` <br> *[user object](#the-user-object)* <br> <em class="expandable">expandable</em> | The user targeted by this ruleset

### Returns

Returns the created user level [page security ruleset object](#the-page-security-ruleset-object).

## Update a user level page security ruleset

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/users/{USERNAME}
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/users/john.doe \
    -X PUT \
    -u username:password \
    -d '{"permissions": ["manage_page"]}'
```

> Example response

```json
{
    "permissions": ["manage_page"],
    "created_at": "2018-03-28T13:17:13.302632+00:00",
    "updated_at": "2018-03-28T13:17:13.302632+00:00",
    "user": {
        "username": "john.doe"
    },
    "page": {
        "domain": {
            "domain_id": "yourdomain"
        },
        "slug": "my-page"
    }
}
```

This endpoint is for updating an existing user level page security ruleset object with provided `username`

### Parameters

No parameters

### Body

Parameter | Description
--------- | -----------
`permissions` <br> *array of strings* | List of special permissions granted to the user. Possible values are `edit_page` and `manage_page`

### Returns

Returns the updated user level [page security ruleset object](#the-page-security-ruleset-object).

## Delete a user level page security ruleset

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/users/{USERNAME}
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/users/john.doe \
    -X DELETE \
    -u username:password
```

This endpoint is for deleting an existing user level security ruleset with provided `username`.

### Parameters

No parameters.

### Returns
A HTTP response with no content and status code 204.

## Retrieve all group level page security rulesets

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/groups
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/groups \
    -u username:password
```

> Example response

```json
[
    {
      "permissions": [],
      "created_at": "2018-03-28T13:17:13.302632+00:00",
      "updated_at": "2018-03-28T13:17:13.302632+00:00",
      "group": {
          "group_id": "your.group"
      },
      "page": {
          "domain": {
              "domain_id": "yourdomain"
          },
          "slug": "my-page"
      }
    },
    {...},
    {...}
]
```

This endpoint is for retrieving all rulesets defined for the page with provided `slug`.

### Parameters

No parameters.

### Returns

Returns a list of [page security ruleset objects](#the-page-security-ruleset-object).

## Create a group level page security ruleset

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/groups
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/groups \
    -X POST \
    -u username:password \
    -d '{"permissions": ["edit_page"], "group": {"group_id": "your.group"}}'
```

> Example response

```json
{
    "permissions": ["edit_page"],
    "created_at": "2018-03-28T13:17:13.302632+00:00",
    "updated_at": "2018-03-28T13:17:13.302632+00:00",
    "group": {
        "group_id": "your.group"
    },
    "page": {
        "domain": {
            "domain_id": "yourdomain"
        },
        "slug": "my-page"
    }
}
```

This endpoint is for creating a new group level security ruleset.

### Parameters

No parameters.

### Body

Parameter | Description
--------- | -----------
`permissions` <br> *array of strings* | List of special permissions granted to the group. Possible values are `edit_page` and `manage_page`
`group` <br> *[group object](#the-group-object)* <br> <em class="expandable">expandable</em> | The group targeted by this ruleset

### Returns

Returns the created group level [page security ruleset object](#the-page-security-ruleset-object).

## Update a group level page security ruleset

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/groups/{GROUP_ID}
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/groups/your.group \
    -X PUT \
    -u username:password \
    -d '{"permissions": ["manage_page"]}'
```

> Example response

```json
{
    "permissions": ["manage_page"],
    "created_at": "2018-03-28T13:17:13.302632+00:00",
    "updated_at": "2018-03-28T13:17:13.302632+00:00",
    "group": {
        "group_id": "your.group"
    },
    "page": {
        "domain": {
            "domain_id": "yourdomain"
        },
        "slug": "my-page"
    }
}
```

This endpoint is for updating an existing group level page security ruleset object with provided `group_id`.

### Parameters

No parameters.

### Body

Parameter | Description
--------- | -----------
`permissions` <br> *array of strings* | List of special permissions granted to the group. Possible values are `edit_page` and `manage_page`

### Returns

Returns the updated group level [page security ruleset object](#the-page-security-ruleset-object).

## Delete a group level page security ruleset

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/security/groups/{GROUP_ID}
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/security/groups/your.group \
    -X DELETE \
    -u username:password
```

This endpoint is for deleting an existing group level security ruleset with provided `group_id`.

### Parameters

No parameters.

### Returns
A HTTP response with no content and status code 204.
