import pandas as pd


def fetch_data():
    return (
        pd.read_csv("./assets/data/avocado.csv")
            .query("type == 'conventional' and region == 'Albany'")
            .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
            .sort_values(by="Date")
    )