import pandas as pd

from BattingData import BattingData

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

class BattingPrediction:
    def __init__(self):
        # Create x and y sets
        batting_data = BattingData()
        self.X = batting_data.for_predict_model()[["age", "AB", "AVG", "careerH", "careerAB"]]

        self.X.dropna(axis=0, subset=["AVG"], inplace=True)
        self.y = self.X['AVG']
        self.X.drop(['AVG'], axis=1, inplace=True)

    