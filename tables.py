import pandas as pd

# Returns pandas DataFrame with hitting statistics every individual player in every year from 1871 to 2015.
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

# Returns pandas DataFrame with hitting statistics for a given player in every year there is data.
def get_player_batting_data(player_id):
    batting_data = get_all_players_batting_data()
    return batting_data.query(f"playerID == '{player_id}'")

# Returns pandas DataFrame with league-wide 
def get_league_batting_data():
    return get_all_players_batting_data()[["yearID", "AB", "H", "2B", "3B", "HR", "BB", "SO"]] \
                                         .groupby("yearID") \
                                         .sum()