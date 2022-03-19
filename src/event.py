from datetime import datetime
from typing import Iterable, List, Dict
from session import Session
from movie import Movie, find_movie
from cinema import Cinema, find_cinema


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


SortedEvents = Dict[datetime, Dict[str, Dict[int, List[Event]]]]


def sort_events(events: Iterable[Event]) -> SortedEvents:
    sorted_events: SortedEvents = {}
    for event in events:
        date_ = event.session.date_time.date()
        movie = event.movie.movie_id
        cinema = event.cinema.cinema_id
        if sorted_events.get(date_) is None:
            sorted_events[date_] = {}
        if sorted_events[date_].get(movie) is None:
            sorted_events[date_][movie] = {}
        if sorted_events[date_][movie].get(cinema) is None:
            sorted_events[date_][movie][cinema] = []
        sorted_events[date_][movie][cinema].append(event)
    return sorted_events
