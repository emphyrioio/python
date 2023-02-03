from dataclasses import dataclass
from contextlib import contextmanager
from abc import ABC, abstractclassmethod
import sqlite3


class Model(ABC):
    @abstractclassmethod
    def add(self) -> None:
        pass

    @abstractclassmethod
    def get(self) -> None:
        pass

    @abstractclassmethod
    def update(self) -> None:
        pass

    @abstractclassmethod
    def delete(self) -> None:
        pass


@dataclass
class SQLiteModel:
    db_file: str = None

    @contextmanager
    def open_db(self):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        try:
            yield cursor
        except sqlite3.DatabaseError as error:
            print(error)
        finally:
            connection.close()


@dataclass
class SimpleSQLiteModel(Model, SQLiteModel):
    def __post_init__(self) -> None:
        super().__init__()

    def add(self) -> None:
        pass

    def get(self):
        with self.open_db() as cursor:
            cursor.execute("SELECT * FROM table")
            results = cursor.fetchall()

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass
