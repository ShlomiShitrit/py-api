from __future__ import annotations
from typing import Optional
import pandas as pd
from utils.utils import enforce_types
from utils.constants import Errors, Common
from .column import Column
from utils.types import ColumnType


class Model:

    def __init__(self):
        self._columns: pd.Index[Column] = pd.Index([])
        self._name: str = None
        self._unique: list[Column] = []
        self._primary_key: Column = None
        self._foreign_key = {}

    @property
    def columns(self) -> pd.Index[Column]:
        return self._columns

    @columns.setter
    @enforce_types
    def columns(self, columns: pd.Index[Column]) -> None:
        self._columns = columns

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @enforce_types
    def name(self, name: str) -> None:
        self._name = name

    @property
    def unique(self) -> list[Column]:
        return self._unique

    @unique.setter
    def unique(self) -> None:
        raise ValueError(Errors.cannot_set("unique columns"))

    @property
    def primary_key(self) -> Column:
        return self._primary_key

    @primary_key.setter
    def primary_key(self) -> None:
        raise ValueError(Errors.cannot_set("primary key"))

    @property
    def foreign_key(self) -> dict:
        return self._foreign_key

    @foreign_key.setter
    def foreign_key(self) -> None:
        raise ValueError(Errors.cannot_set("foreign key"))

    def load_model_from_file(self, file_path: str, name: Optional[str] = None) -> None:
        data: pd.DataFrame = pd.read_csv(file_path)
        model_name: str = name if name else file_path.split("/")[-1].split(".")[0]
        self._columns = self.create_columns(data)
        self._name = model_name

    def create_columns(self, data: pd.DataFrame) -> pd.Index[Column]:
        col_dtypes = {
            "int64": ColumnType.INTEGER,
            "float64": ColumnType.FLOAT,
            "object": ColumnType.STRING,
        }
        columns = pd.Index(
            [
                Column(column, col_dtypes.get(str(data[column].dtype)).value)
                for column in data.columns
            ]
        )
        return columns

    def _get_column(self, column: str) -> Column:
        for col in self._columns:
            if col.name == column:
                return col
        raise ValueError(Errors.not_found(Common.Column, column))

    def set_unique(self, column: str):
        col = self._get_column(column)
        if col in self._unique:
            raise ValueError(Errors.already_set(Common.Column, column, "unique"))

        self._unique.append(col)

    def set_primary_key(self, column: str):
        col = self._get_column(column)
        if col == self._primary_key:
            raise ValueError(Errors.already_set(Common.Column, column, "primary key"))

        self._primary_key = col

    def set_foreign_key(self, column: str, model: Model):
        col = self._get_column(column)
        self._foreign_key[col.name] = model.name
