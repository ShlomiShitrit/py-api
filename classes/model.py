from __future__ import annotations
from typing import Optional
import pandas as pd
from utils.utils import enforce_types
from utils.constants import Errors, Common


class Model:

    def __init__(self):
        self._columns: pd.Index = pd.Index([])
        self._name = ""
        self._unique = []
        self._primary_key: str | float = None
        self._foreign_key = {}

    @property
    def columns(self) -> pd.Index:
        return self._columns

    @columns.setter
    @enforce_types
    def columns(self, columns: pd.Index) -> None:
        self._columns = columns

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @enforce_types
    def name(self, name: str) -> None:
        self._name = name

    @property
    def unique(self) -> list:
        return self._unique

    @unique.setter
    def unique(self) -> None:
        raise ValueError(Errors.cannot_set("unique columns"))

    @property
    def primary_key(self) -> str | float:
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
        self._columns = data.columns
        self._name = model_name

    def set_unique(self, column: str):
        if column not in self._columns:
            raise ValueError(Errors.not_found(Common.Column, column))

        if column in self._unique:
            raise ValueError(Errors.already_set(Common.Column, column, "unique"))

        self._unique.append(column)

    def set_primary_key(self, column: str):
        if column not in self._columns:
            raise ValueError(Errors.not_found(Common.Column, column))

        if column in self._primary_key:
            raise ValueError(Errors.already_set(Common.Column, column, "primary key"))

        self._primary_key = column

    def set_foreign_key(self, column: str, model: Model):
        if column not in self._columns:
            raise ValueError(Errors.not_found(Common.Column, column))

        self._foreign_key[column] = model.name
