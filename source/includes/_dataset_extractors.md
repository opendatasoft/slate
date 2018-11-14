# Extractors

Extractors are the components of the OpenDataSoft platform that translate a data source such as a file or an API into a list of records that can then be processed and indexed. The OpenDataSoft platform offers a lot of different extractors for different types of sources, from the simple CSV file to complex APIs. The extractor for a source must be defined when [creating a Resource](#create-a-new-resource). This section documents how to get the list of extractors available for the domain, and how to figure out which extractor is right for your resource as well as the set of parameters that will give the best results.

## List available extractors

The list of available extractors is not set in stone. As we continue to provide extractors for more and more data source types, and as available extractors can differ from domain to domain, it is very useful to list all the extractors that are available for use at any given time. 

> Definition

```HTTP
GET https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/extractors/
```

> Example request

```HTTP
curl -XGET https://yourdomain.opendatasoft.com/api/management/v2/extractors/
    -u username:password
```

> Example response

```json
{
    "type": "csvfile",
    "label": "CSV File",
    "authentication": {},
    "parameters": [{
        "is_mandatory": false,
        "description": "The string used as field delimiter in the file.",
        "default": ",",
        "label": "Separator",
        "type": "string",
        "name": "separator"
    }, {...}]
}
```

The enpoint returns the list of all available extractors, represented with their type, their label, their authentication mode and their available parameters.

### Returns
A list of extractors, represented by the following fields:

Parameter | Description
--------- | -----------
`type` | extractor name <br> *string*
`label` | human readable extractor name <br> *string*
`authentication` | authentication mode for the extractor <br> *object*.
`parameters` | list of parameters available for the extractor <br> *array*.

The parameters are given with the form:

Parameter | Description
--------- | -----------
`name` | parameter name <br> *string*
`label` | human readable parameter name <br> *string*
`type` | parameter type <br> *string*
`description` | parameter description <br> *string*
`default` | default value for the parameter <br> *parameter type*
`is_mandatory` | whether the field is mandatory <br> *boolean*
`choices` | set of all possible values for the parameter <br> *array of choices* only present when applicable
`hidden` | whether the parameter is shown in the interface <br> *boolean* only present if the value is true

## Guess the right extractor for a source

Before configuring a resource one must determine which extractor will perform well with the data source. In order to do that, this endpoint can be called with a URL (`odsfile` or remote).

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/guess_extractors/
```

> Example request

```HTTP
curl -XPOST https://yourdomain.opendatasoft.com/api/management/v2/guess_extractors/
    -u username:password
    -d '{"url": "https://example.com/json/api/"}'
```

> Example response

```json
{
    "recommended_extractors": [
        "jsonfile",
        "file",
        "jsondict"
    ],
    "other_extractors": [
        "csvfile",
        ...
    ]

}
```

The endpoint takes an URL and optionnaly credentials to user in oder to gain access to this URL, and outputs a list of extractors that are likely to work well for this URL, as well as a list of the other extractors available on the domain that are not likely to succeed in extracting records out of that URL. 

### Parameters

Parameter | Description
--------- | -----------
`url` | source URL <br> *string* can be remote (`ftp` or `https` for instance) or a local file with `odsfile`.
`credentials` | credentials used to gain access to the source URL <br> *string*.

### Returns
Returns a list of recommanded extractors filled with the extractor types that are likely to succeed at extracting records out of the URL as well as a list of all other extractors available on the platform that are not likely to do so.


## Guess an extractor parameters

Some extractor parameters are very common and can be guessed with the help of the URL. These guessed parameters can drastically speed up extractor configuration. In order to obtain these guessed parameters, this endpoint can be used.

> Definition

```HTTP
POST https://{YOURDOMAIN}.opendatasoft.com/api/management/v2/guess_extractor_params/
```

> Example request

```HTTP
curl -XVERB https://yourdomain.opendatasoft.com/api/management/v2/guess_extractor_params/
    -u username:password
    -d '{"url": "odsfile://data.csv", "extractor": "csvfile"}'
```

> Example response

```json
{
    "extractor": "csvfile",
    "params": {
        "headers_first_row": true,
        "encoding": "utf-8",
        "separator": ";",
        "first_row_no": 1
    }
}
```

This endpoint takes an URL and an extractor type, and guesses as many extractor parameters as possible.

### Parameters

Parameter | Description
--------- | -----------
`url` | source url <br> *string* can be remote (`ftp` or `https` for instance) or a local file with `odsfile`.
`extractor` | extractor type. <br> *string*.

### Returns
An object composed of the name of the extractor as well as an object whose keys are the name of the guessed parameter and the values the guessed value.
