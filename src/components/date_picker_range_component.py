from dash import html, dcc

def build(children: str, id: str, min_date_allowed, max_date_allowed, start_date, end_date):
    return html.Div(
        children=[
            html.Div(children=children, className="menu-title"),
            dcc.DatePickerRange(
                id=id,
                min_date_allowed=min_date_allowed,
                max_date_allowed=max_date_allowed,
                start_date=start_date,
                end_date=end_date
            )
        ]
    )