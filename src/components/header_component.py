from dash import dcc, html

component = html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(children="Avocado Analytics", className="header-title"),
                html.P(children="Analyze the behaviour of avocado prices and the number of avocados sold in the US between 2015 and 2018", 
                    className="header-description",
                ),
            ],
            className="header"
        )