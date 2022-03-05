from datetime import datetime
import requests
import json
from typing import Iterable, List


class Session:
    def __init__(
        self, session_id: int, movie_id: str, cinema_id: int, date_time: datetime
    ) -> None:
        self.session_id = session_id
        self.movie_id = movie_id
        self.cinema_id = cinema_id
        self.date_time = date_time


def scrape_sessions(cinema_ids: Iterable[int], date: str) -> List[Session]:
    sessions = []
    for cinema_id in cinema_ids:
        link = f"https://www.cinemacity.hu/hu/data-api-service/v1/quickbook/10102/film-events/in-cinema/{cinema_id}/at-date/{date}"
        response = requests.get(link)
        content = json.loads(response.content)
        for session in content["body"]["events"]:
            if "original-lang-en-us" in session["attributeIds"]:
                s = Session(
                    session["id"],
                    session["filmId"],
                    cinema_id,
                    datetime.fromisoformat(session["eventDateTime"]),
                )
                sessions.append(s)
    return sessions
