from typing import Generic, TypeVar, TypedDict, NotRequired, Any, Callable


T = TypeVar("T")

type NonEmptyList[T] = list[T]

type TabularData[T] = NonEmptyList[dict[str, T]]

type OutputAsTable[T] = Callable[[TabularData[T]], bool]


class StringifyOptions(TypedDict, Generic[T]):
    indentation: NotRequired[str | int | None]
    trailingCommas: NotRequired[bool]
    output_as_table: NotRequired[OutputAsTable[T]]


class Symbol(object):
    def __init__(self, name):
        self.name = name


type Path = list[str | int]

type Record = dict[str, Any | Record]

type SetValue = Callable[[Record, Any], None]
type GetValue = Callable[[Record], tuple[Any, bool]]


class TableFieldSetter(TypedDict):
    keys: list[str]
    set_value: SetValue


class TableFieldGetter(TypedDict):
    name: str
    get_value: GetValue


# Parse result is a tuple (parsed, value)
type ParseResult = tuple[bool, Any]
