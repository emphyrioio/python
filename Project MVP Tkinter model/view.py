import tkinter as tk
import tkinter.ttk as ttk
from dataclasses import dataclass
from typing import Callable, Protocol
from config import Config

from ttkthemes import ThemedTk
from tkfactory import TkFactory


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
        self.resizable(
            self.conf.get_parameter("app_window_resizable_width"),
            self.conf.get_parameter("app_window_resizable_height"),
        )
        self.minsize(
            self.conf.get_parameter("app_window_min_width"),
            self.conf.get_parameter("app_window_min_height"),
        )
        self.maxsize(
            self.conf.get_parameter("app_window_max_width"),
            self.conf.get_parameter("app_window_max_height"),
        )
        self.attributes("-alpha", self.conf.get_parameter("app_window_alpha"))
        self.attributes("-topmost", self.conf.get_parameter("app_window_topmost"))

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
        def styling():
            self.style = ttk.Style(self)
            self.style.theme_use(self.conf.get_parameter("app_theme"))
            self.style.configure("RedFrame.TFrame", background="red")

        # WIDGETS
        def init_main_frame():
            self.main_frame = ttk.Frame(self)
            self.main_frame.grid(row=0, column=0, sticky="nsew")

        # GRID CONDIGURATION
        def grid_config():
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.main_frame.rowconfigure(0, weight=1)
            self.main_frame.columnconfigure(0, weight=1)

        styling()
        init_main_frame()
        grid_config()

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


@dataclass()
class ScrollableTreeFactory:
    root: ThemedTk
    frame: ttk.Frame = None

    def __post_init__(self) -> None:
        self.frame = self.create_frame()

    def create_frame(self):
        frame = ttk.Frame(self.root)
        tree = ttk.Treeview(frame)
        tree.grid(row=0, column=0)
        return frame
