import pandas as pd

def get_all_players_batting_data():
    batting_data = pd.read_csv(r"data\\Batting.csv")
    batting_data.set_index("playerID")

    master_data = pd.read_csv(r"data\\Master.csv")
    master_data.set_index("playerID")

    return pd.merge(master_data, \
                    batting_data, \
                    on=["playerID"]) \
                    [["playerID", "nameLast", "nameFirst", "yearID", "AB", "H", "2B", "3B", "HR", "BB", "SO"]] \
                    .sort_values(by=["yearID", "nameLast", "nameFirst"]) \
                    .dropna()