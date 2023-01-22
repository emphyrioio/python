from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from typing import Callable, Protocol

from model import Model


class View(Protocol):
    def init_ui(self, presenter: Presenter) -> None:
        ...

    def add(self) -> None:
        ...

    def get(self) -> None:
        ...

    def update(self) -> None:
        ...

    def delete(self) -> None:
        ...

    def mainloop(self) -> None:
        ...


@dataclass
class Presenter:
    model: Model
    view: View

    def __post_init__(self) -> None:
        pass

    # ACTIONS
    def handle_add(self, event: Callable[[tk.Event], None]) -> None:
        pass

    def handle_get(self, event: Callable[[tk.Event], None]) -> None:
        pass

    def handle_update(self, event: Callable[[tk.Event], None]) -> None:
        pass

    def handle_delete(self, event: Callable[[tk.Event], None]) -> None:
        pass

    def run(self) -> None:
        self.view.init_ui(self)
        self.view.mainloop()
