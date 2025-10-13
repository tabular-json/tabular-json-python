from typing import TypedDict, NotRequired


class StringifyOptions(TypedDict):
    indentation: NotRequired[str | int]
    trailingCommas: NotRequired[bool]
