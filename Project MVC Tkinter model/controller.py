from dataclasses import dataclass

from model import Model
from view import View


@dataclass
class Controller:
    model: Model
    view: View

    def __post_init__(self) -> None:
        # BINDINGS
        self.view.bind_add(self.add)
        self.view.bind_delete(self.delete)

    # ACTIONS
    def list(self, event=None) -> None:
        pass

    def add(self, event=None) -> None:
        item = self.view.get()
        self.model.add(item)

    def delete(self, event=None) -> None:
        self.model.delete()

    def update(self, event=None) -> None:
        self.model.update()

    def run(self) -> None:
        self.view.mainloop()
