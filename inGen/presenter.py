from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from model import Addressee, DeceasedPerson, Profil, Template


class View(Protocol):
    def init_ui(self, presenter: Presenter) -> None:
        ...

    def add(self) -> None:
        ...

    def get(self) -> None:
        ...

    def delete(self) -> None:
        ...

    def update(self) -> None:
        ...

    def mainloop(self) -> None:
        ...


@dataclass
class Presenter:
    profil: Profil
    addressee: Addressee
    template: Template
    deceased_person: DeceasedPerson
    view: View

    def __post_init__(self) -> None:
        pass

    # ACTIONS
    def handle_add(self, event=None) -> None:
        pass

    def handle_get(self, event=None) -> None:
        pass

    def handle_delete(self, event=None) -> None:
        pass

    def handle_update(self, event=None) -> None:
        pass

    def run(self) -> None:
        self.view.init_ui(self)
        self.view.mainloop()
