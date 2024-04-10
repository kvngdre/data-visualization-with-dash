# Import packages
from dash import Dash, html, Input, Output

from components import (
    header_component,
    graph_component,
    drop_down_component,
    date_picker_range_component,
)
from data import fetch_data

# Read data
data = fetch_data()

# Initialize the app
external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?" "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"

# Find unique regions and avocado_types
regions = data["region"].sort_values().unique()
avocado_types = data["type"].sort_values().unique()
min_date_allowed = data["Date"].min().date()
max_date_allowed = data["Date"].max().date()
start_date = data["Date"].min().date()
end_date = data["Date"].max().date()

# App layout
app.layout = html.Div(
    children=[
        header_component.component,
        # Menu Component
        html.Div(
            children=[
                drop_down_component.build("Region", "region-filter", "Albany", regions),
                drop_down_component.build(
                    "Type", "type-filter", "conventional", avocado_types
                ),
                date_picker_range_component.build(
                    "Date Range",
                    "date-range",
                    min_date_allowed,
                    max_date_allowed,
                    start_date,
                    end_date,
                ),
            ],
            className="menu",
        ),
        # Charts
        html.Div(
            children=[
                graph_component.build("price-chart"),
                graph_component.build("volume-chart"),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    Output("price-chart", "figure"),
    Output("volume-chart", "figure"),
    Input("region-filter", "value"),
    Input("type-filter", "value"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
# Chart Interactivity
def update_chart(region, avocado_type, start_date, end_date):
    filtered_data = data.query(
        "region == @region and type == @avocado_type"
        " and Date >= @start_date and Date < @end_date"
    )

    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": ("$%{y:.2f}<extra></extra>"),
            }
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {
                "tickprefix": "$",
                "fixedrange": True,
            },
            "colorway": ["#17b897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }

    return price_chart_figure, volume_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)
