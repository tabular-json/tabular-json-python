from typing import TypedDict, NotRequired, Any, Callable


class StringifyOptions(TypedDict):
    indentation: NotRequired[str | int | None]
    trailingCommas: NotRequired[bool]


Path = list[str | int]

SetValue = Callable[[dict[str, Any], Any], None]


class TableField(TypedDict):
    keys: list[str]
    set_value: SetValue
