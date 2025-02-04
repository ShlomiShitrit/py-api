from __future__ import annotations
from typing import Optional
import pandas as pd
from utils.utils import enforce_types
from utils.constants import Errors, Common, COLUMNS_DATATYPES
from .column import Column


class Model:
    """
    Model class to represent a table in a database.

    Attributes:
        columns: pd.Index[Column]
            Index of columns in the model.
        name: str
            Name of the model.
        unique: list[Column]
            List of unique columns in the model.
        primary_key: Column
            Primary key of the model.
        foreign_key: dict
            Dictionary of foreign keys in the model.

    Methods:
        load_model_from_file(file_path: str, name: Optional[str] = None) -> None
            Load model from a CSV file.
        create_columns(data: pd.DataFrame) -> pd.Index[Column]
            Create columns from a DataFrame.
        set_unique(column: str) -> None
            Set a column as unique.
        set_primary_key(column: str) -> None
            Set a column as primary key.
        set_foreign_key(column: str, model: Model) -> None
            Set a column as foreign key
    """

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
        """
        Raises:
            ValueError: If trying to set unique columns.
        """
        raise ValueError(Errors.cannot_set("unique columns"))

    @property
    def primary_key(self) -> Column:
        return self._primary_key

    @primary_key.setter
    def primary_key(self) -> None:
        """
        Raises:
            ValueError: If trying to set primary key.
        """
        raise ValueError(Errors.cannot_set("primary key"))

    @property
    def foreign_key(self) -> dict:
        return self._foreign_key

    @foreign_key.setter
    def foreign_key(self) -> None:
        """
        Raises:
            ValueError: If trying to set foreign key.
        """
        raise ValueError(Errors.cannot_set("foreign key"))

    def load_model_from_file(self, file_path: str, name: Optional[str] = None) -> None:
        """
        Load model from a CSV file.

        Args:
            file_path: str
                Path to the CSV file.
            name: str, optional (default=None)
                Name of the model.
        """
        data: pd.DataFrame = pd.read_csv(file_path)
        model_name: str = name if name else file_path.split("/")[-1].split(".")[0]
        self._columns = self.create_columns(data)
        self._name = model_name

    def create_columns(self, data: pd.DataFrame) -> pd.Index[Column]:
        """
        Create columns from a DataFrame.

        Args:
            data: pd.DataFrame
                DataFrame containing the data.

        Returns:
            pd.Index[Column]: Index of columns in the model.
        """
        columns = pd.Index(
            [
                Column(column, COLUMNS_DATATYPES.get(str(data[column].dtype)).value)
                for column in data.columns
            ]
        )
        return columns

    def _get_column(self, column: str) -> Column:
        """
        Get a column by name.

        Args:
            column: str
                Name of the column.

        Returns:
            Column: Column object.

        Raises:
            ValueError: If column is not found.
        """
        for col in self._columns:
            if col.name == column:
                return col
        raise ValueError(Errors.not_found(Common.Column, column))

    def set_unique(self, column: str) -> None:
        """
        Set a column as unique.

        Args:
            column: str
                Name of the column.

        Raises:
            ValueError: If column is already set as unique.
        """
        col = self._get_column(column)
        if col in self._unique:
            raise ValueError(Errors.already_set(Common.Column, column, "unique"))

        self._unique.append(col)

    def set_primary_key(self, column: str) -> None:
        """
        Set a column as primary key.

        Args:
            column: str
                Name of the column.

        Raises:
            ValueError: If column is already set as primary key.
        """
        col = self._get_column(column)
        if col == self._primary_key:
            raise ValueError(Errors.already_set(Common.Column, column, "primary key"))

        self._primary_key = col

    def set_foreign_key(self, column: str, model: Model) -> None:
        """
        Set a column as foreign key.

        Args:
            column: str
                Name of the column.
            model: Model
                Model to set as foreign key.
        """
        col = self._get_column(column)
        self._foreign_key[col.name] = model.name
