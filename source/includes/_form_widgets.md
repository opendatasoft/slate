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
`name` <br> *string* | Identifier of the object
`type` <br> *string* | Nature of the object. <br> Possible values are `text`, `multitext`, `html` and `datetime`
`label` <br> *string* | Plain name of the object depending of the language
`widget` <br> *[widget object](#the-widget-object)* | Characteristics of the expected rendered UI component for the object
`choices` <br> *array* | *`text` and `multitext` only* <br> List of all accepted values by the object, any other value will be rejected. <br> May be an array of strings or an array of 2-item arrays, where the first item is the actual accepted value and the second its label.

## The widget object

List of all widget objects:

* [datalist](#the-datalist-widget)
* [datetimeinput](#the-datetimeinput-widget)
* [html](#the-html-widget)
* [multidatalist](#the-multidatalist-widget)
* [multitextinput](#the-multitextinput-widget)
* [select](#the-select-widget)
* [tags](#the-tags-widget)
* [textinput](#the-textinput-widget)

### Common attributes

Attribute | Description
--------- | -----------
`type` <br> *string* | The widget's type <br> Accepted values are `textinput`, `select`, `datalist`, `multitextinput`, `multidatalist`, `tags`, `datetimeinput` and `geographicarea`
`help_text` <br> *string* | Informational text describing the constraints and uses of the form object

#### The `datalist` widget

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

The `datalist` widget is to be rendered as a text input with an autocomplete feature. If the `suggest_values` attributes is set, then a simple html datalist is enough.

Attribute | Description
--------- | -----------
`suggest_url` <br> *string* | The URL of a distant service providing values based on the partial text in the input (e.g. Algolia)
`suggest_values` <br> *array of strings* | A list of default values

<div class="clearfix"></div>


#### The `datetimeinput` widget

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

The `datetimeinput` widget is to be rendered as a datetime-local input.

<div class="clearfix"></div>

#### The `html` widget

> Example object

```json
{
    todo
}
```
> Example HTML widget

```html
todo
```

todo

<div class="clearfix"></div>

#### The `multidatalist` widget

> Example object

```json
{
    todo
}
```
> Example HTML widget

```html
todo
```

The `multidatalist` widget is to be rendered as multiple text inputs with an autocomplete feature, with the possibility to remove and add more inputs. If the `orderable` option is set, then the inputs must be reorderable one relative to the other.

Attribute | Description
--------- | -----------
`orderable` <br> *boolean* | Flag indicating whether the visual component should allow values to be reordered or not

<div class="clearfix"></div>

#### The `multitextinput` widget

> Example object

```json
{
    todo
}
```
> Example HTML widget

```html
todo
```

The `multitextinput` widget is to be rendered as multiple simple text inputs, with the possibility to remove and add more inputs. If the `orderable` option is set, then the inputs must be reorderable one relative to the other.

Attribute | Description
--------- | -----------
`orderable` <br> *boolean* | Flag indicating whether the visual component should allow values to be reordered or not

<div class="clearfix"></div>

#### The `select` widget

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

The `select` widget is to be rendered as a simple select element.

Options of this element must match the `choices` defined in the parent [form object](#the-form-object).

<div class="clearfix"></div>

#### The `tags` widget

> Example object

```json
{
    todo
}
```
> Example HTML widget

```html
todo
```

todo

<div class="clearfix"></div>

#### The `textinput` widget

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

The `textinput` widget is to be rendered as a simple text input.

<div class="clearfix"></div>
