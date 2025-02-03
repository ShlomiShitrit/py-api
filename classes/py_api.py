import subprocess
from utils.utils import enforce_types
from classes.model import Model
from sqlalchemy import ForeignKey, Column as SqlColumn
from sqlalchemy.orm import relationship
from database import Base


class PyAPI:
    def __init__(self):
        self.name: str = "PyAPI"
        self._models: list[Model] = []
        self._tables: list[Base] = []

    @property
    def models(self) -> list[Model]:
        return self._models

    @models.setter
    @enforce_types
    def models(self, models: list[Model]) -> None:
        self._models = models

    @property
    def tables(self) -> list[Base]:
        return self._tables

    @tables.setter
    @enforce_types
    def tables(self, tables: list[Base]) -> None:
        self._tables = tables

    @enforce_types
    def load_model(self, model: Model) -> None:
        self.models.append(model)
        table = self._create_table_class(model)
        self.tables.append(table)

    def _create_table_class(self, model: Model) -> Base:
        """Dynamically creates a SQLAlchemy ORM model class."""
        attributes = {"__tablename__": model.name}

        for column in model.columns:
            col_type = column.type
            col_name = column.name

            if column == model.primary_key:
                attributes[col_name] = SqlColumn(col_type, primary_key=True)
            elif column in model.unique:
                attributes[col_name] = SqlColumn(col_type, unique=True)
            elif foreign_column := model.foreign_key.get(col_name):
                attributes[col_name] = SqlColumn(col_type, ForeignKey(foreign_column))
                attributes[f"{col_name}_obj"] = relationship(foreign_column)
            else:
                attributes[col_name] = SqlColumn(col_type)

        print(f"Creating table: {model.name}")
        print("Attributes:", attributes)

        return type(model.name, (Base,), attributes)

    def deploy(self) -> None:
        try:
            result = subprocess.run(["bash", "run_api.sh"], check=True, text=True)
            print("Script output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr)
