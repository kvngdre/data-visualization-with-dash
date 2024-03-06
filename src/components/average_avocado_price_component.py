from dash import dcc, html

from data import fetch_data

data = fetch_data()

component = html.Div(
    children=[
        html.Div(
            children=dcc.Graph(
                id="price-chart",
                config={"displayModeBar": False},
                figure={
                    "data": [
                        {
                            "x": data["Date"],
                            "y": data["AveragePrice"],
                            "type": "lines",
                            "hovertemplate": ("$%{y:.2f}<extra></extra>")
                        }
                    ],
                    "layout": {
                        "title": { 
                            "text": "Average Price of Avocados", 
                            "x": 0.05, 
                            "xanchor": "left"
                        }, 
                        "xaxis": {"fixedrange": True},
                        "yaxis": {
                            "tickprefix": "$", 
                            "fixedrange": True,
                        },
                        "colorway": ["#17b897"],
                    },
                }
            ),
            className="card"
        )
    ]
)