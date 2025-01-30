import subprocess
from utils.utils import enforce_types
from classes.model import Model
from classes.table import Table


class PyAPI:
    def __init__(self):
        self.name: str = "PyAPI"
        self._models: list[Model] = []
        self._tables: list[Table] = []

    @property
    def models(self) -> list[Model]:
        return self._models

    @models.setter
    @enforce_types
    def models(self, models: list[Model]) -> None:
        self._models = models

    @property
    def tables(self) -> list[Table]:
        return self._tables

    @tables.setter
    @enforce_types
    def tables(self, tables: list[Table]) -> None:
        self._tables = tables

    @enforce_types
    def load_model(self, model: Model) -> None:
        self.models.append(model)
        table = Table(model)
        self.tables.append(table)

    def deploy(self) -> None:
        try:
            result = subprocess.run(["bash", "run_api.sh"], check=True, text=True)
            print("Script output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr)
