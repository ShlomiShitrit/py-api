from enum import Enum
from sqlalchemy import Integer, String, Float


class ColumnType(Enum):
    """
    Enum class to represent the data types of a column

    Attributes:
        INTEGER: Integer
            Integer data type
        STRING: String
            String data type
        FLOAT: Float
            Float data type
    """

    INTEGER = Integer
    STRING = String
    FLOAT = Float
