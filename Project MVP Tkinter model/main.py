from config import Config
from models import Model
from presenter import Presenter
from view import Gui


def main() -> None:
    conf = Config()
    model = Model()
    view = Gui(conf)
    presenter = Presenter(model, view)
    presenter.run()


if __name__ == "__main__":
    main()
