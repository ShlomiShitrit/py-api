from enum import Enum
from sqlalchemy import Integer, String, Float


class ColumnType(Enum):
    INTEGER = Integer
    STRING = String
    FLOAT = Float
