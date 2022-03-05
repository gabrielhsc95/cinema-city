from random import seed
from typing import Iterable, List
from session import Session
from movie import Movie, find_movie
from cinema import Cinema, find_cinema
from datetime import timedelta


class Event:
    def __init__(self, session: Session, movie: Movie, cinema: Cinema) -> None:
        self.session = session
        self.movie = movie
        self.cinema = cinema


#     def get_book_link(self) -> str:
#         return f"https://www.cinemacity.hu/booking?presentationCode={self.session.session_id}&cinemaId={self.session.cinema_id}"

#     def __str__(self):
#         html = f"""
# <div class="card">
#     <div class="poster">
#         <img src={self.movie.poster}/>
#     </div>
#     <div class="movieInfo">
#         <h2>{self.movie.name}</h2>
#         <b>Cinema</b>: {self.cinema.name}
#         <b>Date</b>: {self.session.date_time.date().strftime("%d/%m/%y")}
#         <b>Starts</b>: {self.session.date_time.time().isoformat(timespec='minutes')}
#         <b>Ends</b>: {(self.session.date_time + timedelta(minutes=self.movie.length)).time().isoformat(timespec='minutes')}
#         <b>Length</b>: {self.movie.length//60}h{self.movie.length%60}m
#         <a href="{self.get_book_link()}">Book</a>
#     </div>
# </div>
# """
#         return html


def create_events(
    sessions: Iterable[Session], movies: Iterable[Movie], cinemas: Iterable[Cinema]
) -> List[Event]:
    return [
        Event(
            session,
            find_movie(movies, session.movie_id),
            find_cinema(cinemas, session.cinema_id),
        )
        for session in sessions
    ]
