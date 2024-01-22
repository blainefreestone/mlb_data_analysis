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

        # Generate gradient regressor model
        self.gradient_model = XGBRegressor(random_state=0, n_estimators=500, learning_rate=0.04)

    # Trains object gradient model and return the mean absolute error of the predictions
    def train_model(self):
        # Split data into training and validation sets
        X_train, X_valid, y_train, y_valid = train_test_split(self.X, self.y, train_size=0.8, test_size=0.2, random_state=0)
        
        # Fit model to training data set
        self.gradient_model.fit(X_train, y_train)

        # Generate predictions with the model
        predictions = pd.Series(self.gradient_model.predict(X_valid))

        return mean_absolute_error(y_valid, predictions)