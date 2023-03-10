import tkinter as tk
import tkinter.ttk as ttk
from dataclasses import dataclass
from typing import Callable, ClassVar

from model import Model
from ttkthemes import ThemedTk


@dataclass
class View(ThemedTk):
    # Window parameters
    __WINDOW_TITLE: ClassVar[str] = "Title"
    __WINDOW_ICON: ClassVar[str] = ""
    __WINDOW_WIDTH: ClassVar[int] = 800
    __WINDOWS_HEIGHT: ClassVar[int] = 600

    model: Model
    theme: str = "black"

    def __post_init__(self) -> None:
        super().__init__()

        self.title(View.__WINDOW_TITLE)
        self.iconbitmap(View.__WINDOW_ICON)
        self.geometry("%sx%s" % (View.__WINDOW_WIDTH, View.__WINDOWS_HEIGHT))

        self.create_ui()

    def create_ui(self) -> None:
        # STYLING
        self.style = ttk.Style(self)
        self.style.theme_use(self.theme)

        # WIDGETS
        self.entry = ttk.Button(self, text="Hello, world!")
        self.entry.grid(row=0, column=0, sticky="EW")

        # GRID CONFIGURATION
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def get(self):
        pass

    # BINDINGS
    def bind_add(self, callback: Callable[[tk.Event], None]) -> None:
        pass

    def bind_delete(self, callback: Callable[[tk.Event], None]) -> None:
        pass
