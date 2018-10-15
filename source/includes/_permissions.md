# Permissions

Users, groups and API keys can bear permissions that grant users the right to access protected endpoints or perform restricted actions on a domain.

## Available permissions

There are 3 kinds of permissions:

- domain level permissions, that grant rights to a user, group or API key on the whole domain,
- dataset level permissions, that grant rights to a user, group or API key on a specific dataset,
- page level permissions, that grant rights to a user, group or API key on a specific page.

### Domain level permissions

Permission    | Description
------------- | -----------
`edit_domain`                | Ability to edit the properties of the domain, including user and group management
`create_page`                | Ability to create new pages
`edit_page`                  | Ability to edit all pages
`manage_page`                | Ability to change the security of any page editable by this user
`explore_restricted_page`    | Ability to browse any page, even the restricted ones
`create_dataset`             | Ability to create new datasets
`edit_dataset`               | Ability to edit all datasets
`publish_dataset`            | Ability to publish datasets editable by this user
`manage_dataset`             | Ability to change the security of datasets editable by this user
`explore_restricted_dataset` | Ability to browse any dataset, even the restricted ones
`edit_reuse`                 | Ability to edit and manage existing reuses
`manage_subdomains`          | Ability to create and manage subdomains
`explore_monitoring`         | Ability to browse any monitoring dataset and access the analytics section of the back-office
`edit_theme`                 | Ability to manage the domain's theme (edit and make live)

### Dataset level permissions

Permission    | Description
------------- | -----------
`edit_dataset`               | Ability to edit this dataset
`publish_dataset`            | Ability to publish this dataset
`manage_dataset`             | Ability to change the security of this dataset
`explore_restricted_dataset` | Ability to browse this dataset

### Page level permissions

Permission    | Description
------------- | -----------
`edit_page`                  | Ability to edit this page
`manage_page`                | Ability to change the security of this page
`explore_restricted_page`    | Ability to browse this page

## Required permissions per endpoint

### Dataset Index

`GET /api/management/v2/datasets/`

Requires one of the following:

- domain permission: `create_dataset` or `edit_dataset`
- any dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Create

`POST /api/management/v2/datasets/`

Requires domain permission: `create_dataset`

### Dataset Lookup

`GET /api/management/v2/datasets/<dataset_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Delete

`DELETE /api/management/v2/datasets/<dataset_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Abort Action

`PUT /api/management/v2/datasets/<dataset_uid>/abort/`

Requires one of the following:

- domain permission: `edit_dataset` and `publish_dataset`
- current dataset permission: (`edit_dataset` and domain:`publish_dataset`) or `publish_dataset`

### Dataset Attachements Index

`GET /api/management/v2/datasets/<dataset_uid>/attachments/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Attachements Create

`POST /api/management/v2/datasets/<dataset_uid>/attachments/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Attachment Lookup

`GET /api/management/v2/datasets/<dataset_uid>/attachments/<attachment_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Attachment Delete

`DELETE /api/management/v2/datasets/<dataset_uid>/attachments/<attachment_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Change Index

`GET /api/management/v2/datasets/<dataset_uid>/changes/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Attachment Download

`GET /api/management/v2/datasets/<dataset_uid>/download_attachment/<attachment_uid>`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset System Processor Index

`GET /api/management/v2/datasets/<dataset_uid>/fields_specifications/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset System Processor Create

`POST /api/management/v2/datasets/<dataset_uid>/fields_specifications/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset System Processor Lookup

`GET /api/management/v2/datasets/<dataset_uid>/fields_specifications/<processor_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset System Processor Update

`PUT /api/management/v2/datasets/<dataset_uid>/fields_specifications/<processor_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Processor Guess Params

`POST /api/management/v2/datasets/<dataset_uid>/guess_processor_params/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Metadata Index

`GET /api/management/v2/datasets/<dataset_uid>/metadata/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Metadata Lookup

`GET /api/management/v2/datasets/<dataset_uid>/metadata/<template_name>/<metadata_name>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Metadata Update

`PUT /api/management/v2/datasets/<dataset_uid>/metadata/<template_name>/<metadata_name>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Metadata Delete

`DELETE /api/management/v2/datasets/<dataset_uid>/metadata/<template_name>/<metadata_name>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Processor Index

`GET /api/management/v2/datasets/<dataset_uid>/processors/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Processor Create

`POST /api/management/v2/datasets/<dataset_uid>/processors/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Processor Lookup

`GET /api/management/v2/datasets/<dataset_uid>/processors/<processor_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Processor Update

`PUT /api/management/v2/datasets/<dataset_uid>/processors/<processor_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Publish Action

`PUT /api/management/v2/datasets/<dataset_uid>/publish/`

Requires one of the following:

- domain permission: `edit_dataset` and `publish_dataset`
- current dataset permission: (`edit_dataset` and domain:`publish_dataset`) or `publish_dataset`

### Dataset Unsaved Resource Preview

`POST /api/management/v2/datasets/<dataset_uid>/resource_preview/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Resource Index

`GET /api/management/v2/datasets/<dataset_uid>/resources/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Resource Create

`POST /api/management/v2/datasets/<dataset_uid>/resources/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Resource Lookup

`GET /api/management/v2/datasets/<dataset_uid>/resources/<resource_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Resource Update

`PUT /api/management/v2/datasets/<dataset_uid>/resources/<resource_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Resource Delete

`DELETE /api/management/v2/datasets/<dataset_uid>/resources/<resource_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Resource Preview

`GET /api/management/v2/datasets/<dataset_uid>/resources/<resource_uid>/preview/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Restore Change Action

`PUT /api/management/v2/datasets/<dataset_uid>/restore_change/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Schedule Index

`GET /api/management/v2/datasets/<dataset_uid>/schedules/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Schedule Create

`POST /api/management/v2/datasets/<dataset_uid>/schedules/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Schedule Lookup

`GET /api/management/v2/datasets/<dataset_uid>/schedules/<schedule_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset` or `publish_dataset`

### Dataset Schedule Update

`PUT /api/management/v2/datasets/<dataset_uid>/schedules/<schedule_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Schedule Delete

`DELETE /api/management/v2/datasets/<dataset_uid>/schedules/<schedule_uid>/`

Requires one of the following:

- domain permission: `edit_dataset`
- current dataset permission: `edit_dataset`

### Dataset Access Policy Lookup

`GET /api/management/v2/datasets/<dataset_uid>/security/access_policy/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Access Policy Update

`PUT /api/management/v2/datasets/<dataset_uid>/security/access_policy/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Default Security Lookup

`GET /api/management/v2/datasets/<dataset_uid>/security/default/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Default Security Update

`PUT /api/management/v2/datasets/<dataset_uid>/security/default/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Group Security Index

`GET /api/management/v2/datasets/<dataset_uid>/security/groups/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Group Security Create

`POST /api/management/v2/datasets/<dataset_uid>/security/groups/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Group Security Lookup

`GET /api/management/v2/datasets/<dataset_uid>/security/groups/<group_id>/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Group Security Update

`PUT /api/management/v2/datasets/<dataset_uid>/security/groups/<group_id>/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Group Security Delete

`DELETE /api/management/v2/datasets/<dataset_uid>/security/groups/<group_id>/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset User Security Index

`GET /api/management/v2/datasets/<dataset_uid>/security/users/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset User Security Create

`POST /api/management/v2/datasets/<dataset_uid>/security/users/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset User Security Lookup

`GET /api/management/v2/datasets/<dataset_uid>/security/users/<username>/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset User Security Update

`PUT /api/management/v2/datasets/<dataset_uid>/security/users/<username>/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset User Security Delete

`DELETE /api/management/v2/datasets/<dataset_uid>/security/users/<username>/`

Requires one of the following:

- domain permission: `edit_dataset` and `manage_dataset`
- current dataset permission: `edit_dataset` and `manage_dataset`

### Dataset Status

`GET /api/management/v2/datasets/<dataset_uid>/status/`

Requires one of the following:

- domain permission: `edit_dataset` and `publish_dataset`
- current dataset permission: (`edit_dataset` and domain:`publish_dataset`) or `publish_dataset`

### Dataset Unpublish Action

`PUT /api/management/v2/datasets/<dataset_uid>/unpublish/`

Requires one of the following:

- domain permission: `edit_dataset` and `publish_dataset`
- current dataset permission: (`edit_dataset` and domain:`publish_dataset`) or `publish_dataset`

### Catalog Export

`GET /api/management/v2/export_datasets/<export_format>/`

Requires one of the following:

- domain permission: `create_dataset` or `edit_dataset`
- any dataset permission: `edit_dataset` or `publish_dataset`

### Extractors Index

`GET /api/management/v2/extractors/`

Requires one of the following:

- domain permission: `create_dataset` or `edit_dataset`
- any dataset permission: `edit_dataset`

### System Processor Index

`GET /api/management/v2/fields_specifications/`

Requires one of the following:

- domain permission: `create_dataset` or `edit_dataset`
- any dataset permission: `edit_dataset`

### Guess Extractor Params

`POST /api/management/v2/guess_extractor_params/`

Requires one of the following:

- domain permission: `create_dataset` or `edit_dataset`
- any dataset permission: `edit_dataset`

### Guess Extractors

`POST /api/management/v2/guess_extractors/`

Requires one of the following:

- domain permission: `create_dataset` or `edit_dataset`
- any dataset permission: `edit_dataset`

### Processor Index

`GET /api/management/v2/processors/`

Requires one of the following:

- domain permission: `create_dataset` or `edit_dataset`
- any dataset permission: `edit_dataset`
