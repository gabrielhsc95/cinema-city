from typing import List, Iterable
import requests
import json


class Cinema:
    def __init__(self, cinema_id: int, name: str, address: str) -> None:
        self.cinema_id = cinema_id
        self.name = name
        self.address = address


def scrape_cinemas(date: str) -> List[Cinema]:
    link = f"https://www.cinemacity.hu/hu/data-api-service/v1/quickbook/10102/cinemas/with-event/until/{date}"
    response = requests.get(link)
    content = json.loads(response.content)
    cinemas = []
    for cinema in content["body"]["cinemas"]:
        if cinema["groupId"] == "budapest":
            c = Cinema(
                cinema["id"], cinema["displayName"].split(" - ")[0], cinema["address"]
            )
            cinemas.append(c)
    return cinemas


def find_cinema(cinemas: Iterable[Cinema], cinema_id: str) -> Cinema:
    for cinema in cinemas:
        if cinema.cinema_id == cinema_id:
            return cinema
