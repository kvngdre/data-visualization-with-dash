from dash import dcc

from data import fetch_data

data = fetch_data()

line_graph = dcc.Graph(figure={
            "data": [
                {
                    "x": data["Date"],
                    "y": data["AveragePrice"],
                    "type": "lines",
                }
            ],
            "layout": {"title": "Average Price of Avocados"},
        })