from dash import dcc, html

from data import fetch_data

data = fetch_data()

component = html.Div(
    children=[
        html.Div(
            children=dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines"
                    }
                ],
                "layout": {"title": "Avocados Sold"},
                }
            ),
            className="card"
        )
    ]
)