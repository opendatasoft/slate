# Files

On the OpenDataSoft platform, files can be used as data source to create new datasets, and as dataset attachments, to add extra informations to datasets.

## The file object

> Example file object

```json
{
    "file_id": "cheese_data.csv",
    "url": "odsfile://cheese_data.csv",
    "filename": "Cheese Data.csv",
    "properties": {
        "mimetype": "text/csv"
    },
    "created": "2017-06-07T15:16:05.701266+00:00"
}
```

The file object contains:

* a unique identifier
* a URL for use in the platform
* the file name
* a set of file properties
* a creation date

### Attributes

Attribute | Description
--------- | -----------
`file_id` <br> *string* | Unique identifier for the file
`url` <br> *string* | Generated internal URL, using the `odsfile` scheme
`filename` <br> *string* | Human readable name of the file
`properties` <br> *object* | Set of file properties, such as its mimetype
`created` <br> *string* | Time at which the file was created

## List all files

This endpoint lists all files available to the user who performs the request. A file is available to the requesting user if either the user uploaded the file themselves, or if the user has sufficient permissions to edit a dataset where the file is used, or if the user is a domain administrator who has sufficient permissions to edit all datasets of the domain.

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/files/
```

> Example response

```json
[
    {...},
    {
        "file_id": "cheese_data.csv",
        "url": "odsfile://cheese_data.csv",
        "filename": "Cheese Data.csv",
        "properties": {
            "mimetype": "text/csv"
        },
        "created": "2017-06-07T15:16:05.701266+00:00"
    },
    {...}
]
```

## List one file

This endpoints is for retrieving the file object with provided file_id.

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/files/{FILE_ID}/
```

> Example request

```shell
curl 'https://yourdomain.opendatasoft.com/api/management/v2/files/cheese_data.csv'
```

> Example response

```json
{
    "file_id": "cheese_data.csv",
    "url": "odsfile://cheese_data.csv",
    "filename": "Cheese Data.csv",
    "properties": {
        "mimetype": "text/csv"
    },
    "created": "2017-06-07T15:16:05.701266+00:00"
}
```


## Upload a file

This endpoint is for uploading a new file to the platform.

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/files/
```

This endpoint can receive a file sent in multipart, or file content sent through the content POST parameter, along with a mimetype and an optional filename.

### Multipart file upload

The multipart file upload is an easy way to send a file with a HTML form. To do so, an example upload form is shown. Note that the name of the parameter is `file`.

> Example HTML file upload form

```html
<form action="https://yourdomain.opendatasoft.com/api/management/v2/files/" method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit">
</form>
```

> Example multipart request

```shell
curl -XPOST 'https://yourdomain.opendatasoft.com/api/management/v2/files/' \
    -F file=@data.csv
```

Parameter | Description
--------- | -----------
`file` <br> **POST parameter** <br> *file* | Multipart file to upload. This is a POST parameter

### POST content upload

> Example POST content request

```shell
curl -XPOST 'https://yourdomain.opendatasoft.com/api/management/v2/files/' \
    -d '{"content": "language,phrase\nEnglish,Hello World\Esperanto,Saluton mondo\n", "mimetype": "text/csv", "filename": "data.csv"}
```

Parameter | Description
--------- | -----------
`content` <br> *string* | Content of the file to create
`mimetype` <br> *string* | Mimetype of the file
`filename` <br> *string* | **optional** Name of the file. Defaults to `file`


### Response
> Example response

```json
{
    "file_id": "data.csv",
    "url": "odsfile://data.csv",
    "filename": "data.csv",
    "properties": {
        "mimetype": "text/csv"
    },
    "created": "2017-06-07T15:16:05.701266+00:00"
}
```

On success, an HTTP 200 is returned along with the file object of the uploaded file.


## Download a file

This endpoint is for downloading a file with the provided file_id from the platform.

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/files/download_file/{FILE_ID}
```

### Parameters

> Example request

```shell
curl 'https://yourdomain.opendatasoft.com/api/management/v2/files/download_file/data.csv'
```


Parameter | Description
--------- | -----------
`file_id` <br> *file* | The file to download

### Response
> Example response

```http
HTTP/1.1 200 OK
[...]
Content-Disposition: attachment; filename="data.csv"
Content-Type: text/csv; charset=utf-8


brand,color
Renault,blue
Citroën,red
Peugeot,white
```

On success, an HTTP 200 is returned with the file as an attachment.
