from cinema import find_cinema, scrape_cinemas
from movie import find_movie, scrape_movies
from session import scrape_sessions
from event import create_events, sort_events
from datetime import date


date_ = date.today().isoformat()
date_ = "2022-03-20"
cinemas = scrape_cinemas(date_)
sessions = scrape_sessions([cinema.cinema_id for cinema in cinemas], date_)
movies = scrape_movies([session.movie_id for session in sessions], date_)
events = create_events(sessions, movies, cinemas)
sorted_events = sort_events(events)

for date_, movies_dict in sorted_events.items():
    print(date_.isoformat())
    for movie_id, cinemas_dict in movies_dict.items():
        print(f"\t{find_movie(movies, movie_id).name}")
        for cinema_id, events_list in cinemas_dict.items():
            print(f"\t\t{find_cinema(cinemas, cinema_id).name}")
            for e in events_list:
                print(f"\t\t\t{e.session.date_time}")
