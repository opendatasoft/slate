# Form widgets

A few endpoints in the API return definitions along with their objects in order to help you build correct requests. These definitions are specifications your objects must conform to in order to be accepted by the API.

Some of these API will contain a `widget` attribute that contains all you need to generate an HTML input that will match the object's structure.

## The form object

> Example object

```json
{
    "type": "text",
    "label": "Language",
    "help_text": "",
    "choices": [
        ["aa", "Afar"],
        ["ab", "Abkhazian"],
        ["ae", "Avestan"],
        ["af", "Afrikaans"],
        [...],
        [...]
    ],
    "widget": {
        "type": "select"
    }
}
```


An object describing exactly the type of data the related object can accept and providing the expected representation in a form.

### Attributes

Attribute | Description
--------- | -----------
`name` <br> *string* | Identifier of the object
`type` <br> *string* | Nature of the object. <br> Possible values are `text`, `multitext`, `html`, `date` and `datetime`
`label` <br> *string* | Plain name of the object depending of the language
`widget` <br> *[widget object](#the-widget-object)* | Characteristics of the expected rendered UI component for the object
`choices` <br> *array* | *`text` and `multitext` only* <br> List of all accepted values by the object, any other value will be rejected. <br> May be an array of strings or an array of 2-item arrays, where the first item is the actual accepted value and the second its label.
`help_text` <br> *string* | Informational text describing the constraints and uses of the form object

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

#### The `datalist` widget

> Example object

```json
{
    "type": "text",
    "label": "License",
    "help_text": "",
    "widget": {
        "type": "datalist",
        "suggest_values": [
            "Licence Ouverte (Etalab)",
            "Licence Ouverte v2.0 (Etalab)",
            "Open Government Licence v3.0",
            "Open Database License (ODbL)",
            "Public Domain",
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
    <option value="Licence Ouverte (Etalab)">
    <option value="Licence Ouverte v2.0 (Etalab)">
    <option value="Open Government Licence v3.0">
    <option value="Open Database License (ODbL)">
    <option value="Public Domain">
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
    "type": "date",
    "label": "Created",
    "help_text": "",
    "widget": {
        "type": "dateinput"
    }
}
```
> Example HTML widget

```html
<label for="created">Created</label>
<input id="created" type="date-local">
```

The `dateinput` widget will render as a date-local input.

<div class="clearfix"></div>

#### The `datetimeinput` widget

> Example object

```json
{
    "type": "datetime",
    "label": "Modified",
    "help_text": "",
    "widget": {
        "type": "datetimeinput"
    }
}
```
> Example HTML widget

```html
<label for="modified">Modified</label>
<input id="modified" type="datetime-local">
```

The `datetimeinput` widget will render as a datetime-local input.

<div class="clearfix"></div>

#### The `multidatalist` widget

> Example object

```json
{
    "type": "multitext",
    "label": "Theme",
    "help_text": "",
    "widget": {
        "type": "multidatalist",
        "suggest_values": [
            "Health",
            "Culture, Heritage",
            "Education, Training, Research, Teaching",
            "Environment",
            "Transport, Movements",
            "Spatial planning, Town planning, Buildings, Equipment, Housing",
            "Economy, Business, SME, Economic development, Employment",
            "Administration, Government, Public finances, Citizenship",
            "Justice, Safety, Police, Crime",
            "Sports, Leisure",
            "Accommodation, Hospitality Industry",
            "Services, Social"
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
    <li><input type="text" value="Sports, Leisure" list="theme_list"><button>remove</button></li>
    <li><input type="text" value="Health" list="theme_list"><button>remove</button></li>
</ul>
<datalist id="theme_list">
    <option value="Health">
    <option value="Culture, Heritage">
    <option value="Education, Training, Research, Teaching">
    <option value="Environment">
    <option value="Transport, Movements">
    <option value="Spatial planning, Town planning, Buildings, Equipment, Housing">
    <option value="Economy, Business, SME, Economic development, Employment">
    <option value="Administration, Government, Public finances, Citizenship">
    <option value="Justice, Safety, Police, Crime">
    <option value="Sports, Leisure">
    <option value="Accommodation, Hospitality Industry">
    <option value="Services, Social">
</datalist>
```

The `multidatalist` widget will render as multiple text inputs with an autocomplete feature, with the possibility to remove and add more inputs.

### Attributes

Common attributes only.

## The `datalist` widget

<div class="clearfix"></div>

#### The `multiselect` widget

> Example object

```json
 {
    "type": "multitext",
    "label": "Type",
    "help_text": "",
    "choices": [
        "Spatial data set",
        "Spatial data set series",
        "Spatial data service"
    ],
    "widget": {
        "type": "multiselect"
    }
}
```
> Example HTML widget

```html
<label for="type">Type</label>
<select id="type">
    <option>Spatial data set</option>
    <option>Spatial data set series</option>
    <option>Spatial data service</option>
</select>
<button>Add theme</button>
<ul>
    <li>
        <select value="Spatial data set series">
            <option>Spatial data set</option>
            <option>Spatial data set series</option>
            <option>Spatial data service</option>
        </select>
        <button>remove</button>
    </li>
    <li>
        <select value="Spatial data set">
            <option>Spatial data set</option>
            <option>Spatial data set series</option>
            <option>Spatial data service</option>
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
    "type": "multitext",
    "label": "Attributions",
    "help_text": "",
    "widget": {
        "type": "multitextinput"
    }
}
```
> Example HTML widget

```html
<label for="attributions">Attributions</label>
<input id="attributions" type="text" placeholder="New attribution...">
<button>Add attribution</button>
<ul>
    <li><input type="text" value="First attribution"><button>remove</button></li>
    <li><input type="text" value="Second attribution"><button>remove</button></li>
    <li><input type="text" value="Third attribution"><button>remove</button></li>
</ul>
```

The `multitextinput` widget will render as multiple simple text inputs, with the possibility to remove and add more inputs.

<div class="clearfix"></div>

#### The `richtextinput` widget

> Example object

```json
{
    "type": "html",
    "label": "Description",
    "help_text": "",
    "widget": {
        "type": "richtextinput"
    }
}
```
> Example HTML widget

```html
<label for="description">Description</label>
<!-- redactor is a js library that transforms a textarea into a wysiwyg editor -->
<textarea id="description" redactor value="<p>Lorem ipsum dolor sit amet</p>"></textarea>
```

The `richtextinput` message will render as a rich text editor, preferably a WYSIWYG (What You See Is What You Get) one.

<div class="clearfix"></div>

#### The `select` widget

> Example object

```json
{
    "type": "text",
    "label": "Language",
    "help_text": "",
    "choices": [
        ["aa", "Afar"],
        ["ab", "Abkhazian"],
        ["ae", "Avestan"],
        ["af", "Afrikaans"],
        [...],
        [...]
    ],
    "widget": {
        "type": "select"
    }
}
```
> Example HTML widget

```html
<label for="language">Language</label>
<select id="language">
    <option value="aa">Afar</option>
    <option value="ab">Abkhazian</option>
    <option value="ae">Avestan</option>
    <option value="af">Afrikaans</option>
    ...
</select>
```

The `select` widget will render as a simple select element.

Options of this element must match the `choices` defined in the parent [form object](#the-form-object).

<div class="clearfix"></div>

#### The `tags` widget

> Example object

```json
{
    "type": "multitext",
    "label": "Keyword",
    "help_text": "Hit Enter after each keyword",
    "widget": {
        "type": "tags",
        "suggest_url": "/api/management/1.0/metadata_templates/default/keyword/suggest/"
    }
}
```
> Example HTML widget

```html
<label for="keyword">Keyword</label>
<input type="text" id="keyword" placeholder="Type keyword">
<button>Add keyword</button>
<p>Hit enter after each keyword</p>
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

Attribute | Description
--------- | -----------
`suggest_url` <br> *string* | The URL of a distant service providing values based on the partial text in the input (e.g. Algolia)
`suggest_values` <br> *array of strings* | A list of default values

<div class="clearfix"></div>

#### The `textinput` widget

> Example object

```json
{
    "type": "text",
    "label": "Title",
    "help_text": "",
    "widget": {
        "type": "textinput"
    }
}
```

> Example HTML widget

```html
<label for="title">Title</label>
<input type="text" id="title">
```

The `textinput` widget will render as a simple text input.

<div class="clearfix"></div>
