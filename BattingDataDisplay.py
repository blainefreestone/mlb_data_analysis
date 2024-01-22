from BattingData import BattingData

import matplotlib.pyplot as plt 

class BattingDataDisplay:
    def __init__(self):
        self.batting_data = BattingData()

    def graph_player_batting_statistics(self, player_id):
        player_data = self.batting_data.statistics_for_player(player_id)
        player_data.plot(marker="o", linestyle="dashed")
        plt.title(f"{self.batting_data.name_for_player(player_id)} Statistics")
        plt.xlabel("Season")
        plt.show()

    def graph_league_batting_statistics(self):
        league_data = self.batting_data.statistics_for_league()
        league_data.plot(marker="none")
        plt.title("MLB League Statistics 1871-2015")
        plt.xlabel("Season")
        plt.show()

    def print_player_batting_statistics(self, player_id):
        print(self.batting_data.statistics_for_player(player_id))

    def print_league_batting_statistics(self):
        print(self.batting_data.statistics_for_league())

    def print_player_batting_data(self, player_id):
        print(self.batting_data.for_player(player_id))

    def print_league_batting_data(self):
        print(self.batting_data.for_league())

    def print_predict_model_data(self):
        print(self.batting_data.for_predict_model())