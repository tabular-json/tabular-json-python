# Tabular-JSON Python

This is a Python implementation of **Tabular-JSON**, a superset of JSON adding CSV-like tables.

## Install

Install via PyPi: https://pypi.org/project/tabularjson/

```
pip install tabularjson
```

## Use

```python
from tabularjson import parse, stringify, StringifyOptions

text = """{
    "id": 1,
    "name": "Brandon",
    "friends": ---
    "id", "name"
        2,    "Joe"
        3,    "Sarah"
    ---
}
"""

data = parse(text)
print(data)
# {
#     'id': 1,
#     'name': 'Brandon',
#     'friends': [
#         {'id': 2, 'name': 'Joe'},
#         {'id': 3, 'name': 'Sarah'}
#     ]
# }

data["friends"].append({"id": 4, "name": "Alan"})

options: StringifyOptions = {"indentation": 4, "trailingCommas": False}
updatedText = stringify(data, options)
print(updatedText)
# {
#     "id": 1,
#     "name": "Brandon",
#     "friends": ---
#         "id", "name"
#         2,    "Joe"
#         3,    "Sarah"
#         4,    "Alan"
#     ---
# }
```

## API

### parse

Parse a string containing Tabular-JSON data into JSON.

Syntax:

```
data = parse(text)
```

Where:

- `text` is a string containing Tabular-JSON data
- `data` is the parsed data, returned by the function

Example:

```python
from tabularjson import parse

text = """{
    "id": 1,
    "name": "Brandon",
    "friends": ---
    "id", "name"
        2,    "Joe"
        3,    "Sarah"
    ---
}
"""

data = parse(text)
print(data)
# {
#     'id': 1,
#     'name': 'Brandon',
#     'friends': [
#         {'id': 2, 'name': 'Joe'},
#         {'id': 3, 'name': 'Sarah'}
#     ]
# }
```

### stringify

Stringify data into a string containing Tabular-JSON.

Syntax:

```
text = stringify(data, options)
```
Where:

- `data` is a JSON object or array
- `options` is an optional object which can have the following properties:
  - `indentation: int | str | None` an integer specifying the number of spaces in the indentation, or a string containing the indentation itself, like `"\t"` to get tab indentation. When `None` (default), the output will not be indented.
  - `trailingCommas: bool` when true, the output will contain trailing commas after the last item in an array and the last key/value pair in an object. `False` by default.
- `text` is a string containing Tabular-JSON data, returned by the function

Example:

```python
from tabularjson import stringify, StringifyOptions

data = {
    'id': 1,
    'name': 'Brandon',
    'friends': [
        {'id': 2, 'name': 'Joe'},
        {'id': 3, 'name': 'Sarah'}
    ]
}

options: StringifyOptions = {"indentation": 4, "trailingCommas": False}
text = stringify(data, options)

print(text)
# {
#     "id": 1,
#     "name": "Brandon",
#     "friends": ---
#         "id", "name"
#         2,    "Joe"
#         3,    "Sarah"
#     ---
# }
```

## License

Released under the [ISC license](LICENSE.md).
