from typing import Iterable, List
import requests
import json
from api_key import key


class Movie:
    def __init__(self, movie_id: str, name: str, length: int, poster: str) -> None:
        self.movie_id = movie_id
        self.name = translate_name(name)
        self.length = length
        self.poster = poster


def scrape_movies(movie_ids: Iterable[str], date: str) -> List[Movie]:
    movies = []
    link = f"https://www.cinemacity.hu/hu/data-api-service/v1/quickbook/10102/films/until/{date}"
    response = requests.get(link)
    content = json.loads(response.content)
    for movie in content["body"]["films"]:
        if movie["id"] in movie_ids:
            m = Movie(movie["id"], movie["name"], movie["length"], movie["posterLink"])
            movies.append(m)
    return movies


def find_movie(movies: Iterable[Movie], movie_id: str) -> Movie:
    for movie in movies:
        if movie.movie_id == movie_id:
            return movie


def translate_name(name: str) -> str:
    link = f"https://imdb-api.com/hu/API/SearchTitle/{key}/{name}"
    response = requests.get(link)
    content = json.loads(response.content)
    if len(content["results"]) > 0:
        return content["results"][0]["title"]
    return name
