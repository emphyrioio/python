from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from model import Model


@dataclass
class View(Protocol):
    def create_ui(self, presenter: Presenter) -> None:
        ...

    def add(self) -> None:
        ...

    def get(self) -> Any:
        ...

    def delete(self) -> None:
        ...

    def update(self) -> None:
        ...

    def mainloop(self) -> None:
        ...


@dataclass
class Presenter:
    model: Model
    view: View

    def handle_add(self) -> None:
        item = self.view.get()
        self.model.add(item)

    def handle_get(self) -> Any:
        self.model.get()

    def handle_delete(self) -> None:
        self.model.delete()

    def handle_update(self) -> None:
        self.model.update()

    def run(self) -> None:
        self.view.create_ui(self)
        self.view.mainloop()
