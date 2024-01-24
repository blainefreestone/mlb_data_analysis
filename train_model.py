import pandas as pd

from BattingData import BattingData

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Returns mean absolute error for model with dataset used for training and validation. 
def test_model():
    # Create x and y sets
    batting_data = BattingData()
    X = batting_data.for_predict_model()[["age", "AB", "AVG", "careerAVG"]]

    X.dropna(axis=0, subset=["AVG"], inplace=True)
    y = X['AVG']
    X.drop(['AVG'], axis=1, inplace=True)

    # Split data into training and validation sets
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

    # Generate and fit the predictive model
    gradient_model = XGBRegressor(random_state=0, n_estimators=500, learning_rate=0.04)
    gradient_model.fit(X_train, y_train)

    # Generate predictions with the model
    predictions = pd.Series(gradient_model.predict(X_valid))
    print(predictions)
    print(y_valid)

    # Get mean absolute error for predictions
    return mean_absolute_error(y_valid, predictions)