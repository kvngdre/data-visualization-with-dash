from dash import dcc, html

def build(id:str):
    return html.Div(
    children=[
        html.Div(
            children=dcc.Graph(
                id=id,
                config={"displayModeBar": False},
            ),
            className="card"
        )
    ]
)