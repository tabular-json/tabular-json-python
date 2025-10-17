from typing import Any

from tabularjson.types import Path


def get_in(obj, path):
    """
    Get a nested property from a nested object or array.
    Returns the Symbol undefined when not found.
    """
    value = obj
    i = 0

    while i < len(path) and value is not undefined:
        key = path[i]

        if type(value) is dict:
            value = value[key] if key in value else undefined
        elif type(value) is list:
            index = int(key)
            value = value[index] if index < len(value) else undefined
        else:
            value = undefined

        i += 1

    return value

def set_in(obj, path: Path, value: Any):
    nested = obj
    i_last = len(path) - 1
    i = 0

    while i < i_last:
        part = path[i]

        if part not in nested:
            if type(path[i + 1]) == int:
                nested[part] = []
            else:
                nested[part] = {}

        nested = nested[part]
        i += 1

    if type(path[i_last]) is int:
        arr_assign(nested, path[i_last], value)
    else:
        # dict
        nested[path[i_last]] = value

    return obj

def arr_assign(arr, key, val):
    # https://stackoverflow.com/questions/20567465/dynamically-growing-a-python-array-when-assigning-to-it
    try:
        arr[key] = val
        return
    except IndexError:
        # Do not extend the array for negative indices
        # That is ridiculously counterintuitive
        assert key >= 0
        arr.extend(((key + 1) - len(arr)) * [None])
        arr[key] = val
        return


class Symbol(object):
    def __init__(self, name):
        self.name = name


undefined = Symbol("undefined")
