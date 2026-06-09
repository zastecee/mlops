import mlflow

# Step 2: Configure Tracking

# Option A: Database (Recommended)
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Option C: Remote Tracking Server
# mlflow.set_tracking_uri("http://localhost:5000")

mlflow.set_experiment("my-first-experiment")

# Step 3: Verify Your Connection
print(f"MLflow Tracking URI: {mlflow.get_tracking_uri()}")
print(f"Active Experiment: {mlflow.get_experiment_by_name('my-first-experiment')}")

import pandas as pd

house_price_data = pd.read_csv("./house_price_data.csv")
house_price_data = house_price_data.dropna(axis=0)

# Load the House price dataset
features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = house_price_data[features].astype(float)
y = house_price_data["Price"]

from sklearn.model_selection import train_test_split

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from sklearn.linear_model import LinearRegression

# Enable autologging for scikit-learn
mlflow.sklearn.autolog()

# Just train the model normally
house_price_lr_model = LinearRegression()
house_price_lr_model.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error

predictions = house_price_lr_model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")