import pickle
import os.path


class Article:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"Фильм {self.title} - {self.year} года. (Режиссер: {self.director})"


class FilmModel:
    def __init__(self):
        self.db_name = "film.txt"
        self.Films = self.load_data()

    def add_film(self, dict_films):
        film = Article(*dict_films.values())
        self.Films[film.title] = film

    def get_all_film(self):
        return self.Films.values()

    def get_single_film(self, user_title):
        film = self.Films[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режиссер": film.director,
            "год выпуска": film.year,
            "длительность": film.duration,
            "студия": film.studio,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, user_title):
        return self.Films.pop(user_title)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.Films, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
