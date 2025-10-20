from typing import TypedDict, NotRequired, Any, Callable


class StringifyOptions(TypedDict):
    indentation: NotRequired[str | int | None]
    trailingCommas: NotRequired[bool]


type Path = list[str | int]

type SetValue = Callable[[dict[str, Any], Any], None]


class TableField(TypedDict):
    keys: list[str]
    set_value: SetValue


# Parse result is [True, ...] when something is parsed, and [False, None] otherwise
type ParseResult = tuple[bool, Any]
