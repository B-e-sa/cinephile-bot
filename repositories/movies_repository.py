from sqlalchemy.orm import Session
from db.models.movie import Movie

class MoviesRepository():
    def __init__(self, session: Session):
        self.__session = session

    def create(self, name: str, year: int = None):
        movie = Movie(name=name, year=year)
        self.__session.add(movie)
        self.__session.commit()
        self.__session.refresh(movie)
        return movie

    def find(self, name: str) -> Movie | None:
        q = self.__session.query(Movie).filter(Movie.name.like(f'%{name}%')).all()
        if len(q) != 0:
            return q[0]

    def get(self):
        return self.__session.query(Movie).all()
