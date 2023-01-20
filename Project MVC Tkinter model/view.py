import tkinter as tk

from model import Model


class View(tk.Tk):
    WINDOW_TITLE = "Title"
    WINDOW_WIDTH = 800
    WINDOWS_HEIGHT = 600

    def __init__(self, model: Model) -> None:
        super().__init__()
        self.model = model
        self.title(View.WINDOW_TITLE)
        self.geometry("%sx%s" % (View.WINDOW_WIDTH, View.WINDOWS_HEIGHT))

    def create_ui(self) -> None:
        pass
