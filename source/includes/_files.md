# Files

On the OpenDataSoft platform, files can be used as data source to create new datasets.

## The file object

> Example file object

```json
{
    "file_id": "cheese_data.csv",
    "uri": "odsfile://cheese_data.csv",
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
`url` <br> *string* | Generated URL for use withing the platform
`filename` <br> *string* | Human readable name of the file
`properties` <br> *object* | Set of file properties, such as its mimetype
`created` <br> *string* | Time at which the change was made

## List all files

This endpoint lists all files available to the user who performs the request.

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
        "uri": "odsfile://cheese_data.csv",
        "filename": "Cheese Data.csv",
        "properties": {
            "mimetype": "text/csv"
        },
        "created": "2017-06-07T15:16:05.701266+00:00"
    },
    {...}
]
```

## Upload a file

This endpoint is for sending a new file to the platform.

> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/files/
```

Uploads a file to the platform.

> Example request

```shell
curl -XPOST 'https://yourdomain.opendatasoft.com/api/management/v2/files/' -F file=@data.csv
```

Parameter | Description
--------- | -----------
`file` <br> *file* | The file to upload


### Response
> Example response

```json
{
    "url": "odsfile://data.csv",
    "file_id": "data.csv"
}
```

On success, a HTTP 200 is returned with a JSON object providing the url and the file_id of the newly uploaded file.


## Download a file

This endpoint is for downloading a file from the platform.

> Definition

```HTTP
GET https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/files/{FILE_ID}/
```

Downloads the file with the provided file_id from the platform.

### Parameters

> Example request

```shell
curl 'https://yourdomain.opendatasoft.com/api/management/v2/files/data.csv'
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

On success, a HTTP 200 is returned with the file as an attachment.


## Create a new file from text

Sometimes, it can be helpful to create a new data source from text rather than an actual file, for instance when the data comes from the output of a script. The PastedText API endpoint is for uploading and creating a file from textual input.


> Definition

```HTTP
POST https://{DOMAIN_ID}.opendatasoft.com/api/management/v2/files/pasted_text/
```

Create a new file from textual data passed in the request body.


### Parameters

> Example request

```shell
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/files/pasted_text/ \
    -u username:password -d 'language,phrase\nEnglish,Hello World\Esperanto,Saluton mondo\n'
```

Parameter | Description
--------- | -----------
`body` <br> *string* | The text to create a new file from, passed in the request body

### Response
> Example response

```json
{
    "url": "odsfile://pasted_text.tsv",
    "file_id": "pasted_text.tsv"
}
```

On success, a HTTP 200 is returned with a JSON object providing the url and the file_id of the newly created file.
