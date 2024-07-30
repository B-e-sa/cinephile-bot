from repositories.movies_repository import MoviesRepository
from sqlalchemy.orm import Session


class MoviesService():
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self.__db_session = None
            self.__movies_repository = None

    def register(self, db_session: Session):
        self.__db_session = db_session
        self.__movies_repository = MoviesRepository(db_session)

    def add_vote(self, name: str):
        found_movie = self.__movies_repository.find(name=name)
        if found_movie:
            found_movie.votes += 1
            self.__db_session.commit()

    def create(self, name: str, year: int):
        found_movie = self.__movies_repository.find(name)
        if not found_movie:
            self.__movies_repository.create(name, year)

    def get_all(self):
        return self.__movies_repository.get()
