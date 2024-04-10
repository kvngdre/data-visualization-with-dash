from dash import html, dcc

def build(children: str, id: str, value, items: list):
    return html.Div(
        children=[
            html.Div(children=children, className="menu-title"),
            dcc.Dropdown(
                id=id,
                options=[
                    {"label": item, "value": item}
                    for item in items
                ],
                value=value,
                clearable=False,
                className="dropdown"
            )
        ]
    )