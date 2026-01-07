# Tabular-JSON Python

This is a Python implementation of **Tabular-JSON**, a superset of JSON adding CSV-like tables.

## Install

Install via PyPI: https://pypi.org/project/tabularjson/

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

options: StringifyOptions = {"indentation": 4, "trailing_commas": False}
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
  - `trailing_commas: bool` when true, the output will contain trailing commas after the last item in an array and the last key/value pair in an object. `False` by default.
  - `output_as_table: Callable[[TabularData[T]], bool]` a callback specifying whether to an array containing tabular data as table or not. This option is explained in detail in the section [Output as table](#output-as-table) below.
- `text` is a string containing Tabular-JSON data, returned by the function

Example:

```python
from tabularjson import stringify, StringifyOptions

data = {
    "id": 1,
    "name": "Brandon",
    "friends": [
        {"id": 2, "name": "Joe"},
        {"id": 3, "name": "Sarah"}
    ]
}

options: StringifyOptions = {"indentation": 4, "trailing_commas": False}
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

#### Output as table

Data is tabular when it is an array containing at least one item, where every item is an object. Stringifying tabular data as a table normally results in the smallest output, but it is not always the most readable way. For example having nested tables inside a table is not very readable. Also, having a table containing a field like "comments" or "description" which contains long texts results in a very wide column, making the formatted table hard to read.

Depending on your use case, you can configure a strategy for when to output tabular data as a table. This can be done using the option `output_as_table`. The lambda function `output_as_table` is invoked for all tabular data in the input json and returns true when the data should be stringified as a table.

The library comes with a number of built-in utility functions that can be used with `output_as_table`:

- `always(tabular_data)`: always serialize tabular data as a table, also when the data contains nested arrays. This is the default value of option `output_as_table`.
- `no_nested_arrays(tabular_data)`: serialize tabular data as a table when the data does not contain nested arrays.
- `no_nested_tables(tabular_data)`: serialize tabular data as a table when the data does not contain nested tables. Allows nested arrays when the contain primitive values like numbers or strings.
- `is_homogeneous(tabular_data)`: serialize tabular data as a table when the structure is homogeneous, that is every item has the exact same keys and nested keys.
- `no_long_strings(tabular_data [, max_length])`: serialize tabular data as a table when the data does not contain long text fields

Usage example:

```python
from tabularjson import stringify, is_homogeneous, StringifyOptions

data = {
    "careTakers": [
        {"id": 1001, "name": "Joe"}, 
        {"id": 1002, "name": "Sarah"}
    ],
    "animals": [
        {
            "animalId": 1,
            "name": "Elephant",
            "description": "Elephants are the largest living land animals.",
        },
        {
            "animalId": 2,
            "name": "Giraffe"
        },
    ],
}

# Output as table only when the data is homogeneous: when all list items have the same keys
print(stringify(data, {"indentation": 2, "output_as_table": is_homogeneous}))
# {
#   "careTakers": ---
#     "id", "name"
#     1001, "Joe"
#     1002, "Sarah"
#   ---,
#   "animals": [
#     {
#       "animalId": 1,
#       "name": "Elephant",
#       "description": "Elephants are the largest living land animals."
#     },
#     {
#       "animalId": 2,
#       "name": "Giraffe"
#     }
#   ]
# }
```

See `example2_output_as_table.py` for a more detailed usage example.

## License

Released under the [ISC license](LICENSE.md).
