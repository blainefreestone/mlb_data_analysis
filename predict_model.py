import pandas as pd

from BattingData import BattingData

from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

def predict_for_players(playerIDs, year):
    # Create x and y sets
    batting_data = BattingData()
    X = batting_data.for_predict_model().query(f"yearID != {year}")[["age", "AB", "AVG", "careerAVG"]]
    X.dropna(axis=0, subset=["AVG"], inplace=True)
    y = X['AVG']
    X.drop(['AVG'], axis=1, inplace=True)

    # Generate and fit the predictive model
    gradient_model = XGBRegressor(random_state=0, n_estimators=500, learning_rate=0.04)
    gradient_model.fit(X, y)

    # Generate input data for random model for 10 randomly selected players in 2015
    mask = batting_data.for_predict_model()["playerID"].isin(playerIDs)
    batting_data_year = batting_data.for_predict_model()[mask].query(f"yearID == {year}")

    # Generate predictions with the model
    predictions = pd.Series(gradient_model.predict(batting_data_year[["age", "AB", "careerAVG"]]))

    # Put predictions with their players and information
    return pd.DataFrame(
        {
            "playerID": batting_data_year["playerID"].to_list(),
            "nameFirst": batting_data_year["nameFirst"].to_list(),
            "nameLast": batting_data_year["nameLast"].to_list(),
            "real_AVG": batting_data_year["AVG"].to_list(),
            "predicted_AVG": predictions,
        }
    )