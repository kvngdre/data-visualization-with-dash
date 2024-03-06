# Import packages
from dash import Dash, dcc, html

from components import average_avocado_price_component
from data import fetch_data

# Read data
data = fetch_data()

#Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    children = [
        html.H1(children="Avocado Analytics", className="header-title"),
        html.P(children="Analyze the behaviour of avocado prices and the number of avocados sold in the US between 2015 and 2018", 
               className="header-description",
        ),

        average_avocado_price_component.line_graph,
        html.Hr(),

        dcc.Graph(figure={
            "data": [
                {
                    "x": data["Date"],
                    "y": data["Total Volume"],
                    "type": "lines"
                }
            ],
            "layout": {"title": "Avocados Sold"},
        })
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
