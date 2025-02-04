from utils.types import ColumnType


class Errors:
    not_found = lambda object, name: f"{object} {f"\"{name}\""} not found"
    cannot_set = lambda property: f"Cannot set {property} directly"
    already_set = lambda object, name, type: f"{object} {f"\"{name}\""} already {type}"


class Common:
    Column = "Column"


COLUMNS_DATATYPES = {
    "int64": ColumnType.INTEGER,
    "float64": ColumnType.FLOAT,
    "object": ColumnType.STRING,
}
