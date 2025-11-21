from tabularjson import stringify, is_homogeneous, StringifyOptions

data = {
    "careTakers": [{"id": 1001, "name": "Joe"}, {"id": 1002, "name": "Sarah"}],
    "animals": [
        {
            "animalId": 1,
            "name": "Elephant",
            "description": "Elephants are the largest living land animals.",
        },
        {"animalId": 2, "name": "Giraffe"},
    ],
}

# Use the default table strategy
print(stringify(data, {"indentation": 2}))
# {
#   "careTakers": ---
#     "id", "name"
#     1001, "Joe"
#     1002, "Sarah"
#   ---,
#   "animals": ---
#     "animalId", "name",     "description"
#     1,          "Elephant", "Elephants are the largest living land animals."
#     2,          "Giraffe",
#   ---
# }

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

# No not output the table with objects having a key "animalId"
options: StringifyOptions = {
    "indentation": 4,
    "output_as_table": lambda tabular_data: "animalId" not in tabular_data[0],
}
print(stringify(data, options))
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
