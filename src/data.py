import pandas as pd


def fetch_data():
    return (
        pd.read_csv("./assets/data/stock_data.csv")
        # .query("type == 'conventional' and region == 'Albany'")
        .assign(
            Date=lambda data: pd.to_datetime(data["expiry_date"], format="%Y-%m-%d")
        ).sort_values(by="expiry_date")
    )
