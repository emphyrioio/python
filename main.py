import textwrap
from dataclasses import dataclass, field
from typing import ClassVar

from sqlalchemy import CHAR, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

@dataclass
class Categories(Base):
    __tablename__: ClassVar[str] = "categories"
    id: ClassVar[Column] = Column("id", Integer, primary_key=True)
    name: ClassVar[Column] = Column("name", String)
    id: int
    name: str


class Addressee(Base):
    __tablename__ = "adressees"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, unique=True)
    category = Column("category", Integer, ForeignKey("categories.id"))
    department = Column("department", String)
    phones = Column("phones", String)
    emails = Column("emails", String)
    faxes = Column("faxes", String)
    websites = Column("websites", String)
    address = Column("address", String)
    PObox = Column("PObox", Integer)
    zipcode = Column("zipcode", Integer)
    town = Column("town", String)
    business_zipcode = Column("business_zipcode", String)
    state = Column("state", String)
    country = Column("country", String)

    def __init__(
        self,
        name,
        category,
        department,
        phones,
        emails,
        faxes,
        websites,
        address,
        PObox,
        zipcode,
        town,
        business_zipcode,
        state,
        country,
    ):
        self.name = name
        self.category = category
        self.department = department
        self.phones = phones
        self.emails = emails
        self.faxes = faxes
        self.websites = websites
        self.address = address
        self.PObox = PObox
        self.zipcode = zipcode
        self.town = town
        self.business_zipcode = business_zipcode
        self.state = state
        self.country = country

    def __repr__(self):
        return textwrap.dedent(
            f"""\
            {self.name}
            {self.department}
            {self.address}
            {self.PObox}
            {self.town} {self.business_zipcode}
            {self.state} {self.country}"""
        )


engine = create_engine("sqlite:///addressees.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

cat_bank = Categories(name="BANK")

session.add(cat_bank)

session.commit()

addressee = Addressee(
    "BNP PARIBAS",
    cat_bank.id,
    "AGENCE SUCCESSIONS",
    "0100000000",
    "mail@mail.com",
    "0100000000",
    "www.site.com",
    "16, boulevard des Italiens",
    "111111",
    "75120",
    "PARIS",
    "CEDEX 02",
    "PARIS",
    "FRANCE",
)

session.add(addressee)
session.commit()

# print(addressee)
