import tkinter as tk
import tkinter.ttk as ttk
from dataclasses import dataclass
from typing import Any, Callable, ClassVar, Protocol

from ttkthemes import ThemedTk


@dataclass
class Presenter(Protocol):
    def handle_add(self) -> None:
        ...

    def handle_get(self) -> Any:
        ...

    def handle_delete(self) -> None:
        ...

    def handle_update(self) -> None:
        ...

    def run(self) -> None:
        ...


@dataclass
class Gui(ThemedTk):
    # Window parameters
    __WINDOW_TITLE: ClassVar[str] = "Title"
    __WINDOW_ICON: ClassVar[str] = ""
    __WINDOW_WIDTH: ClassVar[int] = 800
    __WINDOWS_HEIGHT: ClassVar[int] = 600

    def __post_init__(self) -> None:
        super().__init__()

        self.title(Gui.__WINDOW_TITLE)
        self.iconbitmap(Gui.__WINDOW_ICON)
        self.geometry("%sx%s" % (Gui.__WINDOW_WIDTH, Gui.__WINDOWS_HEIGHT))

    def create_ui(self, presenter: Presenter) -> None:
        # STYLING
        self.style = ttk.Style(self)
        self.style.theme_use("black")

        # WIDGETS
        self.entry = ttk.Button(self, text="Hello, world!")
        self.entry.grid(row=0, column=0, sticky="EW")

        # GRID CONFIGURATION
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # BINDINGS
        # .bind('', self.presenter.handle_add)
        # .bind('', self.presenter.handle_get)
        # .bind('', self.presenter.handle_delete)
        # .bind('', self.presenter.handle_update)

    def get(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
