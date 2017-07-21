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
`type` <br> *string* | Nature of the object. <br> Possible values are `text`, `multitext`, `html`, `date` and `datetime`
`label` <br> *string* | Plain name of the object depending of the language
`widget` <br> *[widget object](#the-widget-object)* | Characteristics of the expected rendered UI component for the object
`choices` <br> *array* | *`text` and `multitext` only* <br> List of all accepted values by the object, any other value will be rejected. <br> May be an array of strings or an array of 2-item arrays, where the first item is the actual accepted value and the second its label.

## The widget object

List of all widget objects:

* [datalist](#the-datalist-widget)
* [dateinput](#the-dateinput-widget)
* [datetimeinput](#the-datetimeinput-widget)
* [multidatalist](#the-multidatalist-widget)
* [multiselect](#the-multiselect-widget)
* [multitextinput](#the-multitextinput-widget)
* [richtextinput](#the-richtextinput-widget)
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
</datalist>
```

The `datalist` widget will render as a text input with an autocomplete feature. If the `suggest_values` attributes is set, then a simple html datalist is enough.

Attribute | Description
--------- | -----------
`suggest_url` <br> *string* | The URL of a distant service providing values based on the partial text in the input (e.g. Algolia)
`suggest_values` <br> *array of strings* | A list of default values

<div class="clearfix"></div>

#### The `dateinput` widget

> Example object

```json
{
    "name": "created",
    "type": "date",
    "label": "Created",
    "widget": {
        "type": "dateinput"
    }
}
```
> Example HTML widget

```html
<label for="created">Last Modified</label>
<input id="created" type="date-local">
```

The `dateinput` widget will render as a date-local input.

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

The `datetimeinput` widget will render as a datetime-local input.

<div class="clearfix"></div>

#### The `multidatalist` widget

> Example object

```json
{
    "name": "theme",
    "type": "multitext",
    "label": "Theme",
    "widget": {
        "type": "multidatalist",
        "suggest_values": [
            "theme1",
            "theme2"
        ]
    }
}
```
> Example HTML widget

```html
<label for="theme">Theme</label>
<input id="theme" type="text" placeholder="New theme..." list="theme_list">
<button>Add theme</button>
<ul>
    <li><input type="text" value="theme2" list="theme_list"><button>remove</button></li>
    <li><input type="text" value="theme3" list="theme_list"><button>remove</button></li>
</ul>
<datalist id="theme_list">
    <option value="theme1">
    <option value="theme2">
</datalist>
```

The `multidatalist` widget will render as multiple text inputs with an autocomplete feature, with the possibility to remove and add more inputs.

<div class="clearfix"></div>

#### The `multiselect` widget

> Example object

```json
{
    "name": "theme",
    "type": "multitext",
    "label": "Theme",
    "choices": [
        "theme1",
        "theme2",
        "theme3"
    ],
    "widget": {
        "type": "multiselect",
    }
}
```
> Example HTML widget

```html
<label for="theme">Theme</label>
<select id="theme">
    <option>theme1</option>
    <option>theme2</option>
    <option>theme3</option>
</select>
<button>Add theme</button>
<ul>
    <li>
        <select value="theme1">
            <option>theme1</option>
            <option>theme2</option>
            <option>theme3</option>
        </select>
        <button>remove</button>
    </li>
    <li>
        <select value="theme2">
            <option>theme1</option>
            <option>theme2</option>
            <option>theme3</option>
        </select>
        <button>remove</button>
    </li>
</ul>
```

The `multiselect` widget will render as multiple selects components, with the possibility to remove, change and add more values.

<div class="clearfix"></div>

#### The `multitextinput` widget

> Example object

```json
{
    "name": "theme",
    "type": "multitext",
    "label": "Theme",
    "widget": {
        "type": "multitextinput"
    }
}
```
> Example HTML widget

```html
<label for="theme">Theme</label>
<input id="theme" type="text" placeholder="New theme...">
<button>Add theme</button>
<ul>
    <li><input type="text" value="theme1"><button>remove</button></li>
    <li><input type="text" value="theme2"><button>remove</button></li>
    <li><input type="text" value="theme3"><button>remove</button></li>
</ul>
```

The `multitextinput` widget will render as multiple simple text inputs, with the possibility to remove and add more inputs.

<div class="clearfix"></div>

#### The `richtextinput` widget

> Example object

```json
{
    "name": "description",
    "type": "html",
    "label": "Description",
    "widget": {
        "type": "richtextinput"
    }
}
```
> Example HTML widget

```html
<label for="description">Description>
<!-- redactor is a js library that transforms a textarea into a wysiwyg editor -->
<textarea id="description" redactor></textarea>
```

The `richtextinput` message will render as a rich text editor, preferably a WYSIWYG (What You See Is What You Get) one.

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

The `select` widget will render as a simple select element.

Options of this element must match the `choices` defined in the parent [form object](#the-form-object).

<div class="clearfix"></div>

#### The `tags` widget

> Example object

```json
    "name": "keywords",
    "type": "multitext",
    "label": "Keywords",
    "widget": {
        "type": "tags"
    }
```
> Example HTML widget

```html
<label for="keywords">Keywords</label>
<input type="text" id="keywords" placeholder="Type keyword">
<button>Add keyword</button>
<ul>
    <li>
        Keyword1 <button>remove</button>
    </li>
    <li>
        Keyword2 <button>remove</button>
    </li>
</ul>
```

The `tags` widget will render as an editable list of tags. If possible, the input area where the user enters their new tag should autocomplete with existing values to enhance consistency.

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

The `textinput` widget will render as a simple text input.

<div class="clearfix"></div>
