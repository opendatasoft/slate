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
