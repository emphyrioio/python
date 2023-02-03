import tkinter as tk
import tkinter.ttk as ttk
from dataclasses import dataclass


@dataclass()
class TkFactory(ttk.Frame):
    master: tk.Wm | ttk.Frame
    frame: ttk.Frame = None

    def __post_init__(self) -> None:
        super().__init__()
        self.frame = self.create_frame()

    def create_frame(self):
        self.frame = ttk.Frame(self.master, padding=(5, 10, 5, 10))
        self.treeview = ttk.Treeview(self.frame, selectmode="browse")
        self.xscroll = ttk.Scrollbar(
            self.frame, orient="horizontal", command=self.treeview.xview
        )
        self.yscroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.treeview.yview
        )

        self.treeview.configure(
            xscrollcommand=self.xscroll.set, yscrollcommand=self.yscroll.set
        )

        self.treeview.place(relwidth=0.99, relheight=0.99)
        self.xscroll.place(relwidth=0.99, rely=0.99)
        self.yscroll.place(relheight=0.99, relx=0.99)

        return self.frame
