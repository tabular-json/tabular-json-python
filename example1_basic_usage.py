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

data.friends.append({"id": 4, "name": "Alan"})

options: StringifyOptions = {"indentation": 4, "trailingCommas": False}
updatedText = stringify(data, options)
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
