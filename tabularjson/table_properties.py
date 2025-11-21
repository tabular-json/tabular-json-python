from typing import Any
from tabularjson.tabular import is_tabular
from tabularjson.types import Record, TabularData


def always[T](_: TabularData[T]) -> bool:
    return True


def no_nested_arrays[T](array: TabularData[T]) -> bool:
    def recurse_object(object: Record) -> bool:
        for value in object.values():
            if type(value) is list:
                return False

            if type(value) is dict and not recurse_object(value):
                return False

        return True

    return all(recurse_object(item) for item in array)


def no_nested_tables[T](array: TabularData[T]) -> bool:
    def recurse(value: Any) -> bool:
        if is_tabular(value):
            return False

        if type(value) is list:
            return all(recurse(item) for item in value)

        if type(value) is dict:
            return all(recurse(item) for item in value.values())

        return True

    return all(recurse(item) for item in array)


def is_homogeneous[T](array: TabularData[T]) -> bool:
    first_item = array[0]

    return all(deep_equal_object_keys(item, first_item) for item in array)


def deep_equal_keys(a: Any, b: Any) -> bool:
    if type(a) is dict:
        if not type(b) is dict or not deep_equal_object_keys(a, b):
            return False
    elif type(b) is dict:
        return False

    if type(a) is list:
        if not type(b) is list or not deep_equal_array_keys(a, b):
            return False
    elif type(b) is list:
        return False

    # primitive values
    return True


def deep_equal_object_keys(a: dict[str, Any], b: dict[str, Any]) -> bool:
    a_keys = a.keys()
    b_keys = b.keys()

    if len(a_keys) != len(b_keys) or any(key not in b for key in a_keys):
        return False

    return all(deep_equal_keys(a[key], b[key]) for key in a_keys)


def deep_equal_array_keys(a: list[Any], b: list[Any]) -> bool:
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if not deep_equal_keys(a[i], b[i]):
            return False

    return True


def no_long_strings[T](array: TabularData[T], max_length=24) -> bool:
    def recurse(value: Any) -> bool:
        if type(value) is dict:
            return all(recurse(item) for item in value.values())

        if type(value) is list:
            return all(recurse(item) for item in value)

        if type(value) is str:
            return len(value) <= max_length

        return True

    return recurse(array)
