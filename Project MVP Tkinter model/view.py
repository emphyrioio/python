import tkinter as tk
import tkinter.ttk as ttk
from dataclasses import dataclass
from typing import Callable, Protocol
from config import Config

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
    conf: Config

    def __post_init__(self) -> None:
        super().__init__()

        # Window configuration
        self.title(self.conf.get_parameter("app_title"))
        self.iconbitmap(self.conf.get_parameter("app_icon_file"))

        # Window geometry
        window_width = self.conf.get_parameter("app_window_width")
        window_height = self.conf.get_parameter("app_window_height")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = self._get_center_x(screen_width, window_width)
        center_y = self._get_center_y(screen_height, window_height)

        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    def init_ui(self, presenter: Presenter) -> None:
        # STYLING
        self.style = ttk.Style(self)
        self.style.theme_use(self.conf.get_parameter("app_theme"))
        # WIDGETS

        # GRID CONDIGURATION

        # BIDINGS

    def _get_center_x(self, screen_width: int = 0, window_width: int = 0) -> int:
        center_x = int(screen_width / 2 - window_width / 2)
        return center_x

    def _get_center_y(self, screen_height: int = 0, window_height: int = 0) -> int:
        center_y = int(screen_height / 2 - window_height / 2)
        return center_y

    # ACTIONS
    def add(self) -> None:
        pass

    def get(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass
