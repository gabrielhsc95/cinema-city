TEMPLATE_HTML = """
<html>
    <head>
        <style>
            .movie {{
                margin-left: 20pt;
                width: 250px;
                float: left;
            }}

            .cinema {{
                margin-left: 210pt;
            }}

            .session {{
                margin-left: 230pt;
            }}

            a {{
                border-style: solid;
                border-radius: 10px;
                border-color: lightblue;
                padding: 5px 10px 5px 10px;
                background-color: lightblue;
                color: black;
                text-decoration: none;
            }}
        </style>
        <title>Movies in English streaming on CinemaCity in Budapest</title>
    </head>
    <body>
    {body}
    </body>
</html>
"""


TEMPLATE_DATE = """
          <h1>{date}</h1>
"""

TEMPLATE_MOVIE = """
            <div class="movie">
                <h2>{name}</h2>
                <img src="{poster}" />
                <b>Length</b>: {length}<br />
            </div>
            <br />
            <br />
            <br />
"""

TEMPLATE_CINEMA = """
            <div class="cinema">
                <h3>{name}</h3>
            </div>
"""
TEMPLATE_EVENT = """
            <div class="session">
                <p>
                    <a href="{booking_link}" target="_blank">Book</a>
                    <b>Start</b>: {start} ; <b>End</b>: {end}
                </p>

            </div>
"""
