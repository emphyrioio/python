from gui import Gui
from model import Model
from presenter import Presenter


def main() -> None:
    model = Model()
    gui = Gui(model)
    controller = Presenter(model, gui)
    controller.run()


if __name__ == "__main__":
    main()
