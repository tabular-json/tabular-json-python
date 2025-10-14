from typing import TypedDict, NotRequired, Any


class StringifyOptions(TypedDict):
    indentation: NotRequired[str | int]
    trailingCommas: NotRequired[bool]


def is_tabular(value: Any) -> bool:
    return (
        type(value) is list
        and len(value) > 0
        and all(type(item) is dict for item in value)
    )
