from typing import TypedDict, NotRequired, Any, Callable


class StringifyOptions(TypedDict):
    indentation: NotRequired[str | int | None]
    trailingCommas: NotRequired[bool]


def is_tabular(value: Any) -> bool:
    return (
        type(value) is list
        and len(value) > 0
        and all(type(item) is dict for item in value)
    )


Path = list[str | int]

SetValue = Callable[[dict[str, Any], Any], None]


class TableField(TypedDict):
    keys: list[str]
    set_value: SetValue
