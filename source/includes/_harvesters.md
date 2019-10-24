# Harvesters

Harvesters provide a way for administrators to easily create and update an important number of datasets by importing them from an external source such as a CSW catalog or an ArcGIS service, among many others.
Your user and your API key need the permissions "create_dataset", "edit_dataset" and "publish_dataset".


Through the management API, it is possible to:

- create a harvester
- start a harvester
- publish the datasets attached to a harvester
- unpublish the datasets attached to a harvester
- delete a harvester and optionally delete its datasets


## List Harvesters

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

This endpoint lists all the API harvesters on the domain.

