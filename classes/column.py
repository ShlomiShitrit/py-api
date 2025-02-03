from dataclasses import dataclass
from utils.types import ColumnType


@dataclass
class Column:
    name: str
    type: ColumnType
