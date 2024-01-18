import pandas as pd

class BattingData:
    def __init__(self):
        self.all_players_batting_data = self.__construct_all_players_batting_data()
    
    # Returns pandas DataFrame with hitting statistics every individual player in every year from 1871 to 2015.
    def __construct_all_players_batting_data(self):
        # Convert csv files into Pandas DataFrames
        batting_data = pd.read_csv(r"data\\Batting.csv")
        master_data = pd.read_csv(r"data\\Master.csv")
        # Join two tables with the playerID as the index
        return pd.merge(master_data, \
                        batting_data, \
                        on=["playerID"]) \
                        [["playerID", "nameLast", "nameFirst", "birthYear", "yearID", "AB", "H", "2B", "3B", "HR", "BB", "HBP", "SO", "SF"]] \
                        .sort_values(by=["yearID", "nameLast", "nameFirst"])

    # Returns pandas DataFrame with hitting statistics for a given player in every year there is data.
    def for_player(self, player_id):
        return self.all_players_batting_data.query(f"playerID == '{player_id}'") \
                                            .set_index("yearID") \
                                            [["playerID", "nameLast", "nameFirst", "AB", "H", "2B", "3B", "HR", "BB", "HBP", "SO", "SF"]]

    # Returns pandas DataFrame with league-wide 
    def for_league(self):
        return self.all_players_batting_data[["yearID", "AB", "H", "2B", "3B", "HR", "BB", "HBP", "SO", "SF"]] \
                                            .set_index("yearID") \
                                            .groupby("yearID") \
                                            .sum()

    # Returns DataFrame with batting average, on-base-percentage and slugging percentage added. 
    def __with_statistics(self, data_frame):
        # Needed parameters for statistic calculations:
        hits = data_frame.H
        at_bats = data_frame.AB
        base_on_balls = data_frame.BB
        hit_by_pitch = data_frame.HBP
        sacrifice_flies = data_frame.SF
        doubles = data_frame["2B"]
        triples = data_frame["3B"]
        home_runs = data_frame.HR
        singles = hits - doubles - triples - home_runs

        # Calculations for specific statistics:
        data_frame["AVG"] = hits / at_bats
        data_frame["OBP"] = (hits + base_on_balls + hit_by_pitch) / (at_bats + base_on_balls + hit_by_pitch + sacrifice_flies)
        data_frame["SLG"] = ((singles) + (doubles * 2) + (triples * 3) + (home_runs * 4)) / at_bats
        return data_frame

    # Return DataFrame with player info and three summary statistics.
    def statistics_for_player(self, player_id):
        return self.__with_statistics(self.for_player(player_id))[["playerID", "nameLast", "nameFirst", "AVG", "OBP", "SLG"]]
    
    # Returns DataFrame with year and three league-wide summary statistics.
    def statistics_for_league(self):
        return self.__with_statistics(self.for_league())[["AVG", "OBP", "SLG"]]
    
    def for_predict_model(self):
        data = self.__with_statistics(self.all_players_batting_data)
        
        # Feature engineering:
        data["age"] = data.yearID - data.birthYear # Age
        # Number of previous seasons
        # Career H
        data["careerH"] = data.groupby("playerID")["H"].cumsum() - data.H
        # Career AB
        data["careerAB"] = data.groupby("playerID")["AB"].cumsum() - data.AB
        # Career AVG
        data["careerAVG"] = (data.groupby("playerID")["H"].cumsum() - data.H) / (data.groupby("playerID")["AB"].cumsum() - data.AB)
        # SD of AVGs (seasonal)
        # etc.

        return self.__with_statistics(data)[["playerID", "nameLast", "nameFirst", "age", "AB", "AVG", "careerAB", "careerH"]]