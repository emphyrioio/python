from dataclasses import dataclass
from typing import Any


@dataclass
class Model:
    def add(self, item: Any) -> None:
        ...

    def delete(self) -> None:
        ...

    def get(self):
        ...
