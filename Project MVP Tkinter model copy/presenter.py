from dataclasses import dataclass

from gui import Gui
from model import Model


@dataclass
class Presenter:
    model: Model
    view: Gui

    def __post_init__(self) -> None:
        # BINDINGS
        self.view.bind_add(self.add)
        self.view.bind_delete(self.delete)

    def add(self, event=None) -> None:
        item = self.view.get()
        self.model.add(item)

    def delete(self, event=None) -> None:
        self.model.delete()

    def run(self) -> None:
        self.view.mainloop()
