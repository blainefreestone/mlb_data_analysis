from BattingDataDisplay import BattingDataDisplay
from predict_model import predict_for_players
from train_model import test_model

def main():
    batting_data_display = BattingDataDisplay()

    # League Batting Data Table
    print("League Batting Data")
    batting_data_display.print_league_batting_data()
    input()

    # Willie McCovey Batting Data Table
    print("Batting Data for Willie McCovey")
    batting_data_display.print_player_batting_data("mccovwi01")
    input()

    # League Batting Statistics Table
    print("League Batting Statistics")
    batting_data_display.print_league_batting_statistics()
    input()

    # Willie McCovey Batting Statistics Table
    print("Batting Statistics for Willie McCovey")
    batting_data_display.print_player_batting_statistics("mccovwi01")
    input()

    # Predict Model Data Table
    print("Batting Data for Predict Model (with engineered features)")
    batting_data_display.print_predict_model_data()
    input()

    # League Batting Statistics Graph
    batting_data_display.graph_league_batting_statistics()

    # Pablo Sandoval Batting Statistics Graph
    batting_data_display.graph_player_batting_statistics("sandopa01")

    # Player Predictions Table for players in list in year 2015
    print("Predictions")
    playerIDs = ['morelmi01', 'beckhti01',  'swihabl01', 'gomezca01', 'crawfbr01', 'gardnbr01']
    year = 2015
    print(predict_for_players(playerIDs, year))
    input()

    # Mean Absolute Error of the Predictive Model
    print(f"Mean Absolute Error of Predictive Model: {test_model()}")

main()