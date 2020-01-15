# Harvesters

Harvesters provide a way for administrators to create and update an important number of datasets by importing them from an external source such as a CSW catalog or an ArcGIS service, among many others.
Your user and your API key need the permissions "create_dataset", "edit_dataset" and "publish_dataset".


Through the management API, it is possible to:

- create a harvester
- start a harvester
- publish the datasets attached to a harvester
- unpublish the datasets attached to a harvester
- delete a harvester and optionally delete its datasets


## List harvesters

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/harvesters/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/harvesters/ \
    -u username:password
```

> Example response

```json
[
  {
    "status": "new", 
    "fetcher": {
      "type": "ods",
      "label": "Opendatasoft",
      "description": "Harvester description",
      "parameters": [
        {
          "is_mandatory": false,
          "type": "string",
          "name": "api_key",
          "label": "Api key"
        }, 
        {
          "is_mandatory": false,
          "type": "boolean",
          "name": "delete",
          "label": "Delete datasets removed from remote portal"
        }, 
        {
          "is_mandatory": true,
          "type": "string",
          "name": "domain_id",
          "label": "Domain (ID or URL)"
        }, 
        {
          "is_mandatory": false,
          "type": "string",
          "name": "forced_metas",
          "label": "Forced metadata as a JSON object"
        }, 
        {
          "is_mandatory": false,
          "type": "string",
          "name": "refines",
          "label": "Refines"
        }, 
        {
          "is_mandatory": false, 
          "type": "boolean", 
          "name": "restrict_visibility", 
          "label": "Make the visibility of newly harvested datasets restricted (does not update visibility of existing datasets)"
        }
      ]
    }, 
    "last_modified_by": "john.doe", 
    "schedules": null, 
    "errors": {
      "resources": 0, 
      "harvester": 0
    }, 
    "name": "My Harvester", 
    "harvester_id": "my-harvester", 
    "last_modified_at": "2019-07-19T14:56:25+00:00", 
    "version": 1, 
    "params": {
      "restrict_visibility": true
    }, 
    "created_at": "2019-07-19T14:56:25+00:00", 
    "counters": {
      "attached": 0, 
      "published": 0
    }
  }
]
```

This endpoint lists all the harvesters on the domain, including their parameters.


## Start a harvester

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/harvesters/<harvester_id>/start/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/harvesters/my_harvester/start/ \
    -X PUT \
    -u username:password
```

This endpoint will start a harvester. If it succeeds, it will return a status code 200 with the harvester details.


## Publish a harvester's datasets

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/harvesters/<harvester_id>/publish/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/harvesters/my_harvester/publish/ \
    -X PUT \
    -u username:password
```

This endpoint will publish all datasets attached to the harvester.
If it succeeds, it will return a status code 200 with the harvester details.


## Unpublish a harvester's datasets

> Definition

```HTTP
PUT https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/harvesters/<harvester_id>/unpublish/
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/harvesters/my_harvester/unpublish/ \
    -X PUT \
    -u username:password
```

This endpoint will unpublish all datasets attached to the harvester.
If it succeeds, it will return a status code 200 with the harvester details.


## Delete a harvester (and its datasets)

> Definition

```HTTP
DELETE https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/harvesters/<harvester_id>/?delete_attached_datasets=0
```

> Example request

```shell
curl https://yourdomain.opendatasoft.com/api/management/v2/harvesters/my_harvester/?delete_attached_datasets=0 \
    -X DELETE \
    -u username:password
```

This endpoint will delete the harvester and all its attached datasets if `delete_attached_datasets=1`.

If you set `delete_attached_datasets=0`, then the harvester will be deleted but the attached datasets will be kept.

If it succeeds, it will returns a status code 204 with an empty body.
