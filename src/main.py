from cinema import find_cinema, scrape_cinemas
from movie import find_movie, scrape_movies
from session import scrape_sessions
from event import create_events, sort_events
from datetime import date
from template import TEMPLATE_DATE, TEMPLATE_HTML


date_ = date.today().isoformat()
date_ = "2022-03-20"
cinemas = scrape_cinemas(date_)
sessions = scrape_sessions([cinema.cinema_id for cinema in cinemas], date_)
movies = scrape_movies([session.movie_id for session in sessions], date_)
events = create_events(sessions, movies, cinemas)
sorted_events = sort_events(events)

html_body_list = []
for date_, movies_dict in sorted_events.items():
    html_body_list.append(TEMPLATE_DATE.format(date=date_.strftime("%d/%m/%Y")))
    for movie_id, cinemas_dict in movies_dict.items():
        movie = find_movie(movies, movie_id)
        html_body_list.append(str(movie))
        for cinema_id, events_list in cinemas_dict.items():
            cinema = find_cinema(cinemas, cinema_id)
            html_body_list.append(str(cinema))
            for event in events_list:
                html_body_list.append(str(event))
        html_body_list.append('<div style="clear:both;"></div>')

html = TEMPLATE_HTML.format(body="".join(html_body_list))

with open("english_movies.html", "w") as file:
    file.write(html)
