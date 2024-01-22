import pandas as pd
pd.options.mode.chained_assignment = None

from BattingData import BattingData

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

class BattingPrediction:
    def __init__(self):
        # Create x and y sets
        batting_data = BattingData()

        self.twenty_fifteen_batting_data = batting_data.for_predict_model().query("yearID == 2015")

        self.X = batting_data.for_predict_model().query("yearID < 2015")[["age", "AB", "AVG", "careerAVG"]]
        self.X.dropna(axis=0, subset=["AVG"], inplace=True)
        self.y = self.X['AVG']
        self.X.drop(['AVG'], axis=1, inplace=True)

        # Generate gradient regressor model
        self.gradient_model = XGBRegressor(random_state=0, n_estimators=500, learning_rate=0.04)

    def __fit_model(self):
        self.gradient_model.fit(self.X, self.y)

    # Trains object gradient model and return the mean absolute error of the predictions
    def test_model(self):
        # Split data into training and validation sets
        X_train, X_valid, y_train, y_valid = train_test_split(self.X, self.y, train_size=0.8, test_size=0.2, random_state=0)
        
        # Fit model to training data set
        self.gradient_model.fit(X_train, y_train)

        # Generate predictions with the model
        predictions = pd.Series(self.gradient_model.predict(X_valid))

        print(self.year_batting_statistics)
        return mean_absolute_error(y_valid, predictions)

    # Returns batting average prediction for player based on playerID
    def for_player(self, playerID):
        self.__fit_model()
        data = self.twenty_fifteen_batting_data.query(f"playerID == '{playerID}'")
        data.drop(['yearID', 'playerID', "nameFirst", "nameLast", "AVG"], axis=1, inplace=True)
        prediction = self.gradient_model.predict(data)
        return prediction