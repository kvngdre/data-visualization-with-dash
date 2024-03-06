from dash import dcc, html

from data import fetch_data

data = fetch_data()

component = html.Div(
    children=dcc.Graph(
            id="volume-chart",
            config={"displayModeBar": False},
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines"
                    }
                ],
                "layout": {
                    "title": {
                        "text": "Avocados Sold",
                        "x": 0.05,
                        "xanchor": "left"
                        },
                        "xaxis": {"fixedrange": True},
                        "yaxis": {"fixedrange": True},
                        "colorway": ["#E12D39"],
                    },
                }
            ),
            className="card"
    )