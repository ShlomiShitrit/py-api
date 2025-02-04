from dataclasses import dataclass
from utils.types import ColumnType


@dataclass
class Column:
    """
    Column class to represent a column in a table

    Attributes:
        name: str
            name of the column
        type: ColumnType
            data type of the column
    """

    name: str
    type: ColumnType
