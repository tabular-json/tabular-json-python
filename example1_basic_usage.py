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
