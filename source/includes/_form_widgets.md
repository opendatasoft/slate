# Form widgets

A few endpoints in the API return definitions along their objects in order to help you build correct requests. These definitions are specifications your objects must conform to in order to be accepted by the API.

Some of these API will contain a `widget` attribute that contains all you need to generate an HTML input that will match the object's structure.

## The form object

### Attributes

> Example object

```json
{
    "name": "license",
    "type": "text",
    "label": "License",
    "choices": [
        "Licence Ouverte (Etalab)",
        "Licence Ouverte v2.0 (Etalab)",
        "Open Database License (ODbL)",
        "Public Domain",
        "CC BY",
        "CC BY-ND",
        "CC BY-NC-ND",
        "CC BY-NC",
        "CC BY-NC-SA",
        "CC BY-SA",
        "CC BY-IGO"
    ],
    "widget": {
        "type": "datalist"
    }
}
```

Attribute | Description
--------- | -----------
`name` <br> *string* | Identifier for the object
`type` <br> *string* | Nature of the object. <br> Possible values are `text`, `multitext`, `choice`, `multichoice`, `date`, `datetime`, `html`, `boolean`, `int`, `number`, `geographicarea`
`label` <br> *string* | Plain name of the object depending of the language
`widget` <br> *[widget object](#the-widget-object)* | Characteristics of the expected rendered UI component for the object
`choices` <br> *array of strings* | *`choice` and `multichoice` only* List of all accepted values by the object, any other value will be rejected.
`decimals` <br> *int* | *`number` only* Number of accepted decimals for the object's value
`precision` <br> *string* | *`date` and `datetime` only* The required time precision of the object's value <br> Possible values are `year`, `month`, `day`, `hour`, `minute`, `second`  
`max_length` <br> *int* | *`text` only* Number of accepted characters for the object's value

## The widget object

### Common attributes

Attribute | Description
--------- | -----------
`type` <br> *string* | The widget's type <br> Accepted values are `textinput`, `select`, `datalist`, `multitextinput`, `multiselect`, `multidatalist`, `tags`, `dateinput`, `datetimeinput`, `toggle`, `number` and `geographicarea`
`help_text` <br> *string* | Help text describing the constraints and uses of this form object

#### The `textinput` widget

The `textinput` widget is to be rendered as a simple text input.

> Example object

```json
{
    "name": "license",
    "type": "text",
    "label": "License",
    "widget": {
        "type": "textinput"
    }
}
```

> Example HTML widget

```html
<label for="license">License</label>
<input type="text" id="license" name="license">
```

#### The `select` widget

The `select` widget is to be rendered as a simple select element.

Options of this element must match the `choices` defined in the parent [form object](#the-form-object).

> Example object

```json
{
    "name": "license",
    "type": "text",
    "label": "License",
    "choices": [
        "CC BY",
        "CC BY-ND",
        "CC BY-NC-ND",
        "CC BY-NC",
        "CC BY-NC-SA",
        "CC BY-SA",
        "CC BY-IGO"
    ],
    "widget": {
        "type": "select"
    }
}
```
> Example HTML widget

```html
<label for="license">License</label>
<select id="license" name="license">
    <option value="CC BY">CC BY</option>
    <option value="CC BY-ND">CC BY-ND</option>
    <option value="CC BY-NC-ND">CC BY-NC-ND</option>
    <option value="CC BY-NC">CC BY-NC</option>
    <option value="CC BY-NC-SA">CC BY-NC-SA</option>
    <option value="CC BY-SA">CC BY-SA</option>
    <option value="CC BY-IGO">CC BY-IGO</option>
</select>
```

#### The `datalist` widget

The `datalist` widget is to be rendered as a text input with an autocomplete feature. If the `suggest_values` attributes is set, then a simple html datalist is enough.

Attribute | Description
--------- | -----------
`suggest_url` <br> *string* | The URL of a distant service providing values based on the partial text in the input (e.g. Algolia)
`suggest_values` <br> *array of strings* | A list of default values

> Example object

```json
{
    "name": "license",
    "type": "text",
    "label": "License",
    "widget": {
        "type": "datalist",
        "suggest_values": [
            "CC BY",
            "CC BY-ND",
            "CC BY-NC-ND",
            "CC BY-NC",
            "CC BY-NC-SA",
            "CC BY-SA",
            "CC BY-IGO"
        ]
    }
}
```
> Example HTML widget

```html
<label for="license">License</label>
<input type="text" id="license" name="license" list="license_list">
<datalist id="license_list">
    <option value="CC BY">
    <option value="CC BY-ND">
    <option value="CC BY-NC-ND">
    <option value="CC BY-NC">
    <option value="CC BY-NC-SA">
    <option value="CC BY-SA">
    <option value="CC BY-IGO">
</select>
```

#### The `multitextinput` widget

The `multitextinput` widget is to be rendered as multiple simple text inputs, with the possibility to remove and add more inputs. If the `orderable` option is set, then the inputs must be reorderable one relative to the other.

Attribute | Description
--------- | -----------
`orderable` <br> *boolean* | Flag indicated whether the visual component should allow values to be reordered or not

#### The `multiselect` widget

The `multiselect` widget is to be rendered as multiple select elements, with the possibility to remove and add more inputs. If the `orderable` option is set, then the inputs must be reorderable one relative to the other.
Options of this element must match the `choices` defined in the parent [form object](#the-form-object).

Attribute | Description
--------- | -----------
`orderable` <br> *boolean* | Flag indicated whether the visual component should allow values to be reordered or not

#### The `multidatalist` widget

The `multidatalist` widget is to be rendered as multiple text inputs with an autocomplete feature, with the possibility to remove and add more inputs. If the `orderable` option is set, then the inputs must be reorderable one relative to the other.

Attribute | Description
--------- | -----------
`orderable` <br> *boolean* | Flag indicated whether the visual component should allow values to be reordered or not

#### The `tags` widget
#### The `dateinput` widget

The `dateinput` widget is to be rendered as a date input.


> Example object

```json
{
    "name": "date_modified",
    "type": "date",
    "label": "Date Modified",
    "widget": {
        "type": "dateinput"
    }
}
```
> Example HTML widget

```html
<label for="date_modified">Date Modified</label>
<input id="date_modified" type="date">
```
#### The `datetimeinput` widget

The `datetimeinput` widget is to be rendered as a datetime-local input.


> Example object

```json
{
    "name": "last_modified",
    "type": "datetime",
    "label": "Last Modified",
    "widget": {
        "type": "datetimeinput"
    }
}
```
> Example HTML widget

```html
<label for="last_modified">Last Modified</label>
<input id="last_modified" type="datetime-local">
```

#### The `toggle` widget

The `toggle` widget is to be rendered as a ods-toggle input.


> Example object

```json
{
    "name": "preview",
    "type": "boolean",
    "label": "Preview",
    "widget": {
        "type": "toggle"
    }
}
```
> Example HTML widget

```html
Note : je sais pas ce que je fais :)
<ods-catalog-context context="catalog" catalog-domain="public.opendatasoft.com">
 
    <input type="checkbox" ods-toggle-model="catalog.parameters" ods-toggle-key="refine.publisher" ods-toggle-value="Government">
    <input type="checkbox" ods-toggle-model="catalog.parameters" ods-toggle-key="refine.publisher" ods-toggle-value="World Bank">
 
</ods-catalog-context>
```


#### The `checkbox` widget

The `checkbox` widget is to be rendered as a checkbox input.


> Example object

```json
{
    "name": "enabled",
    "type": "boolean",
    "label": "Enabled",
    "widget": {
        "type": "checkbox"
    }
}
```
> Example HTML widget

```html
<label for="enabled">Enabled</label>
<input id="enabled" type="checkbox">
```

#### The `number` widget

The `number` widget is to be rendered as a number imput.

Attribute | Description
--------- | -----------
`min` <br> *int* | The minimum value for this item, which must not be greater than its maximum (max attribute) value.
`max` <br> *int* | The maximum value for this item, which must not be less than its minimum (min attribute) value.
`step` <br> *positive int* | Works with the min and max attributes to limit the increments at which a value can be set.


> Example object

```json
{
    "name": "language",
    "type": "text",
    "label": "Language",
    "choices": ["fr", "en"],
    "widget": {
        "type": "radio"
    }
}
```
> Example HTML widget

```html
<label for="language">Language</label>
<input type="radio" name="language" value="fr">fr<br>
<input type="radio" name="language" value="en">en<br>

```
#### The `radio` widget

The `radio` widget is to be rendered as a radio input.


> Example object

```json
{
    "name": "language",
    "type": "text",
    "label": "Language",
    "choices": ["fr", "en"],
    "widget": {
        "type": "radio"
    }
}
```
> Example HTML widget

```html
<label for="language">Language</label>
<input type="radio" name="language" value="fr">fr<br>
<input type="radio" name="language" value="en">en<br>

```

#### The `geographicarea` widget
FIXME
