from cinema import scrape_cinemas
from movie import scrape_movies
from session import scrape_sessions
from event import create_events


date = "2022-03-04"
cinemas = scrape_cinemas(date)
sessions = scrape_sessions([cinema.cinema_id for cinema in cinemas], date)
movies = scrape_movies([session.movie_id for session in sessions], date)
events = create_events(sessions, movies, cinemas)

for event in events:
    print(event)
