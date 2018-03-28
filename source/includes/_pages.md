# Pages

Pages can be used to write editorial content directly on the platform, build advanced dashboards and organize 
data portals.

Through the management API, it is possible to list, create, edit and delete pages as well as to configure pages'
visiblity on the portal. 


## The page object

> Example object

```json
{
    "slug": "my-page",
    "title": {
        "fr": "Titre de la page",
        "en": "Page title"
    },
    "description": "The page description",
    "layout": "single-main.html",
    "content": {
        "main": {
            "text": {
                "fr": "Contenu de la page",
                "en": "Page content"
            }
        }
    },
    "tags": [
        "tag1",
        "tag2"
    ],
    "restricted": true,
    "pushed_by_parent": false,
    "has_subdomain_copies": false,
    "created_at": "2018-02-20T16:30:35+00:00",
    "last_modified": "2018-02-20T16:30:35+00:00",
    "last_modified_user": {
        "username": "john.doe"
    },
    "author": {
        "username": "john.doe"
    }
}
```
### Attributes

Attribute | Description
--------- | -----------
`slug` <br> *string* | Human readable identifier used to generate the page's URL
`title` <br> *object* | Internationalized page title
`description` <br> *string* | Page description
`layout` | The HTML layout to use for this page. Possible values are `single-main.html`, `main-left-col-right.html`, `homepage-searchbox.html`, `single-main-contact.html`, `dataset-catalog-overview.html`, `dataset-of-datasets.html`, `reuses.html`, `custom.html`
`content` <br> *object* | Internationalized page content. The shape of the object depends on the chosen layout 
`tags` <br> *array of strings*  | List of string used to classify and sort pages
`restricted` <br> *boolean* | Defines if the page is visible to every user who can explore the portal
`created_at` <br> *datetime*  | Date when the page was created
`last_modified` <br> *datetime*  | Date when the page was last edited
`last_modified_user` <br> *object* <br> <em class="expandable">expandable</em> | The user who last modified the page
`author` <br> *object* <br> <em class="expandable">expandable</em> | The user who created the page
`pushed_by_parent` <br> *boolean* | Inform if the page has been distributed by a parent domain.
`has_subdomain_copies` <br> *boolean* | Inform if the page been distributed to any subdomain.

## List pages

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/ \
    -u username:password
```

> Example response

```json
{
    "items": [
        {
            "slug": "my-page",
            "title": {
                "fr": "Titre de la page",
                "en": "Page title"
            },
            "description": "The page description",
            "layout": "single-main.html",
            "content": {
                "main": {
                    "text": {
                        "fr": "Contenu de la page",
                        "en": "Page content"
                    }
                }
            },
            "tags": [
                "tag1",
                "tag2"
            ],
            "restricted": true,
            "pushed_by_parent": false,
            "has_subdomain_copies": false,
            "created_at": "2018-02-20T16:30:35+00:00",
            "last_modified": "2018-02-20T16:30:35+00:00",
            "last_modified_user": {
                "username": "john.doe"
            },
            "author": {
                "username": "john.doe"
            }
        },
        {...},
        {...}
    ],
    "rows": 10,
    "page": 1,
    "nhits": 42
}
```

This endpoint returns a paginated list of all the pages that can be edited by this user.

### Parameters

Parameter | Default | Description
--------- | ------- | -----------
`search` <br> *string* | None | Performs a full text search on the `title`, `slug`, `description` and `tags` attributes to filter the pages
`rows` <br> *string* | 10 | Number of items to return per page. Max value: 100
`page` <br> *string* | 1 | The list's page to return
`sort` <br> *string* | None | Field on which to sort the results list

### Returns

Returns a paginated list of pages objects.

## Retrieve a page

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/ \
    -u username:password
```

> Example response

```json
{
    "slug": "my-page",
    "title": {
        "fr": "Titre de la page",
        "en": "Page title"
    },
    "description": "The page description",
    "layout": "single-main.html",
    "content": {
        "main": {
            "text": {
                "fr": "Contenu de la page",
                "en": "Page content"
            }
        }
    },
    "tags": [
        "tag1",
        "tag2"
    ],
    "restricted": true,
    "pushed_by_parent": false,
    "has_subdomain_copies": false,
    "created_at": "2018-02-20T16:30:35+00:00",
    "last_modified": "2018-02-20T16:30:35+00:00",
    "last_modified_user": {
        "username": "john.doe"
    },
    "author": {
        "username": "john.doe"
    }
}
```

This endpoint is for retrieving the page object with provided `slug`

### Parameters

No parameters

### Returns

Returns the page object.

## Create a page

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/ \
    -X POST \
    -u username:password \
    -d '{"slug": "my-page", "title": {"fr": "Titre de la page", "en": "Page title"}, "description": "The page description", "layout": "single-main.html", "content": {"main": {"text": {"fr": "Contenu de la page", "en": "Page content"}}}, "tags": ["tag1", "tag2"], "restricted": true}'
```

> Example response

```json
{
    "slug": "my-page", 
    "title": {
        "fr": "Titre de la page", 
        "en": "Page title"
    }, 
    "description": "The page description", 
    "layout": "single-main.html", 
    "content": {
        "main": {
            "text": {
                "fr": "Contenu de la page", 
                "en": "Page content"
            }
        }
    },
    "tags": [
        "tag1", 
        "tag2"
    ], 
    "restricted": true, 
    "pushed_by_parent": false, 
    "has_subdomain_copies": false, 
    "created_at": "2018-03-28T09:37:30.704488+00:00", 
    "last_modified": "2018-03-28T09:37:30.704488+00:00", 
    "last_modified_user": {
        "username": "john.doe"
    }, 
    "author": {
        "username": "john.doe"
    }
}
```

This endpoint is for creating a new page.

### Parameters

No parameters

### Body

Parameter | Description
--------- | -----------
`slug` <br> *string* | Human readable identifier used to generate the page's URL
`title` <br> *object* | Internationalized page title
`description` <br> *string* | Page description
`layout` | The HTML layout to use for this page. Possible values are `single-main.html`, `main-left-col-right.html`, `homepage-searchbox.html`, `single-main-contact.html`, `dataset-catalog-overview.html`, `dataset-of-datasets.html`, `reuses.html`, `custom.html`
`content` <br> *object* | Internationalized page content. The shape of the object depends on the chosen layout 
`tags` <br> *array of strings*  | List of string used to classify and sort pages
`restricted` <br> *boolean* | Defines if the page is visible to every user who can explore the portal. This parameter is only available if you have the permission to manage the pages' security

### Returns

Returns the created page object.

## Update a page

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/ \
    -X PUT \
    -u username:password \
    -d '{"title": {"fr": "Nouveau titre de la page", "en": "New page title"}, "description": "The page description", "layout": "single-main.html", "content": {"main": {"text": {"fr": "Contenu de la page", "en": "Page content"}}}, "tags": ["tag1", "tag2"], "restricted": true}'
```

> Example response

```json
{
    "slug": "my-page", 
    "title": {
        "fr": "Titre de la page", 
        "en": "Page title"
    }, 
    "description": "The page description", 
    "layout": "single-main.html", 
    "content": {
        "main": {
            "text": {
                "fr": "Contenu de la page", 
                "en": "Page content"
            }
        }
    },
    "tags": [
        "tag1", 
        "tag2"
    ], 
    "restricted": true, 
    "pushed_by_parent": false, 
    "has_subdomain_copies": false, 
    "created_at": "2018-03-28T09:37:30.704488+00:00", 
    "last_modified": "2018-03-28T09:37:30.704488+00:00", 
    "last_modified_user": {
        "username": "john.doe"
    }, 
    "author": {
        "username": "john.doe"
    }
}
```

This endpoint is for updating an existing page object with provided `slug`

### Parameters

No parameters

### Body

Parameter | Description
--------- | -----------
`title` <br> *object* | Internationalized page title
`description` <br> *string* | Page description
`layout` | The HTML layout to use for this page. Possible values are `single-main.html`, `main-left-col-right.html`, `homepage-searchbox.html`, `single-main-contact.html`, `dataset-catalog-overview.html`, `dataset-of-datasets.html`, `reuses.html`, `custom.html`
`content` <br> *object* | Internationalized page content. The shape of the object depends on the chosen layout 
`tags` <br> *array of strings*  | List of string used to classify and sort pages
`restricted` <br> *boolean* | Defines if the page is visible to every user who can explore the portal. This parameter is only available if you have the permission to manage the pages' security

## Delete a page

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/{PAGE_SLUG}/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/my-page/ \
    -X DELETE \
    -u username:password
```

This endpoint is for deleting an existing page object with provided `slug`

### Parameters

No parameters

### Returns
A HTTP response with no content and status code 204

## Delete multiple pages

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/pages/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/pages/ \
    -X DELETE \
    -u username:password \
    -d '[{"slug": "my-page"}, {...}, , {...}]'
```

> Example response

```json
[
    {
        "slug": "my-page",
        "title": {
            "fr": "Titre de la page",
            "en": "Page title"
        },
        "description": "The page description",
        "layout": "single-main.html",
        "content": {
            "main": {
                "text": {
                    "fr": "Contenu de la page",
                    "en": "Page content"
                }
            }
        },
        "tags": [
            "tag1",
            "tag2"
        ],
        "restricted": true,
        "pushed_by_parent": false,
        "has_subdomain_copies": false,
        "created_at": "2018-02-20T16:30:35+00:00",
        "last_modified": "2018-02-20T16:30:35+00:00",
        "last_modified_user": {
            "username": "john.doe"
        },
        "author": {
            "username": "john.doe"
        }
    },
    {...},
    {...}
]
```

This endpoint is for deleting multiple pages

### Parameters

No parameters

### Body
This endpoint accepts a list of objects containing the following parameters:

Parameter | Description
--------- | -----------
`slug` <br> *string* | The page's slug to be deleted

### Returns

The list of deleted page objects
