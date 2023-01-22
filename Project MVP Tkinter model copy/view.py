import tkinter as tk
import tkinter.ttk as ttk
from dataclasses import dataclass
from typing import Callable, ClassVar, Protocol

from ttkthemes import ThemedTk


class Presenter(Protocol):
    def handle_add(self, event: Callable[[tk.Event], None]) -> None:
        ...

    def handle_get(self, event: Callable[[tk.Event], None]) -> None:
        ...

    def handle_update(self, event: Callable[[tk.Event], None]) -> None:
        ...

    def handle_delete(self, event: Callable[[tk.Event], None]) -> None:
        ...


@dataclass
class Gui(ThemedTk):
    # Window parameters
    __WINDOW_TITLE: ClassVar[str] = "Title"
    __WINDOW_ICON: ClassVar[str] = ""
    __WINDOW_WIDTH: ClassVar[int] = 800
    __WINDOWS_HEIGHT: ClassVar[int] = 600

    theme: str = "black"

    def __post_init__(self) -> None:
        super().__init__()
        self.title(Gui.__WINDOW_TITLE)
        self.iconbitmap(Gui.__WINDOW_ICON)
        self.geometry("%sx%s" % (Gui.__WINDOW_WIDTH, Gui.__WINDOWS_HEIGHT))

    def init_ui(self, presenter: Presenter) -> None:
        # STYLING
        self.style = ttk.Style(self)
        self.style.theme_use(self.theme)
        # WIDGETS

        # GRID CONDIGURATION

        # BIDINGS

    # ACTIONS
    def add(self) -> None:
        pass

    def get(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass
