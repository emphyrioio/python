from gui import Gui
from model import Model
from presenter import Presenter


def main() -> None:
    model = Model()
    gui = Gui()
    presenter = Presenter(model, gui)
    presenter.run()


if __name__ == "__main__":
    main()
