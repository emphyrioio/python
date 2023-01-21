from dataclasses import dataclass
from typing import Any


@dataclass
class Model:
    def get(self):
        pass

    def add(self, item: Any) -> None:
        pass

    def delete(self) -> None:
        pass

    def update(self) -> None:
        pass
