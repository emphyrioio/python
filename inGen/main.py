from model import Addressee, DeceasedPerson, Profile, Template
from presenter import Presenter
from view import Gui


def main() -> None:
    profil = Profile()
    addressee = Addressee()
    template = Template()
    deceased_person = DeceasedPerson()
    view = Gui()
    presenter = Presenter(profil, addressee, template, deceased_person, view)
    presenter.run()


if __name__ == "__main__":
    main()
