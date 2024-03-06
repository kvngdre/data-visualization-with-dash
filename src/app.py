# Import packages
from dash import Dash, dcc, html

from components import (average_avocado_price_component,
                        avocados_sold_component, header_component)
from data import fetch_data

# Read data
data = fetch_data()

#Initialize the app
external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"

# App layout
app.layout = html.Div(
    children = [
        # Add components
        header_component.component,

        average_avocado_price_component.component,

        avocados_sold_component.component
    ],
    className="header"
)


if __name__ == "__main__":
    app.run_server(debug=True)
