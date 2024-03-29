# -*- coding: utf-8 -*-
"""Bitcoin Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16G8sl1mAZlsgoDP_x69VtjcjrzRe4zNy

# 1. Define the Problem

The objective of this project is to develop a machine learning model that can predict whether buying Bitcoin at a given time will result in profitable returns or not. This problem is essential for investors and traders who seek to make informed decisions about when to buy or sell Bitcoin based on historical price data and relevant features.

# 2. Explore the Data

## import
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score

"""## data"""

df = pd.read_csv('BTC-USD.csv')

df.head()

df.info()

"""1. **Date**: represents the date of each data point.

2. **Open**: contains the opening price of the stock for each date.

3. **High**: represents the highest price of the stock during each trading day.

4. **Low**: contains the lowest price of the stock during each trading day.

5. **Close**: represents the closing price of the stock for each trading day.

6. **Adj Close**: represents the adjusted closing price of a stock for each trading day. It is similar to the regular closing price but has been adjusted to account for corporate actions such as stock splits, dividends, and rights offerings.

7. **Volume**: represents the trading volume, which refers to the total number of shares of that particular stock that were traded during a specific time period, typically within a trading day.

**All columns has 2713 non-null entries, meaning there are no missing values (nulls) in this column**
"""

df.describe()

# Select features and target variable
X = df[['Open', 'High', 'Low', 'Adj Close', 'Volume']]
y = df['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict on the testing set
y_pred = model.predict(X_test_scaled)

# Calculate MAE
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae}')

# Calculate MSE
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse}')

# Calculate RMSE (repeated for clarity)
rmse = np.sqrt(mse)
print(f'Root Mean Squared Error (RMSE): {rmse}')

# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print(f'R-squared (R²): {r2}')

# Since accuracy is not directly applicable to regression problems like ours (predicting a continuous value),
# we'll define a custom accuracy metric based on a threshold.
# For example, a prediction is considered accurate if it's within a certain percentage of the actual value.

def custom_accuracy1(y_true, y_pred, threshold=0.05):
    """Calculate the custom accuracy based on a threshold.

    Args:
        y_true (array): The actual values.
        y_pred (array): The predicted values.
        threshold (float): The percentage threshold to consider a prediction accurate.

    Returns:
        float: The custom accuracy.
    """
    correct = 0
    for actual, predicted in zip(y_true, y_pred):
        if abs(actual - predicted) / actual <= threshold:
            correct += 1
    return correct / len(y_true)

# Calculate custom accuracy
accuracy = custom_accuracy(y_test, y_pred)
print(f'Custom Accuracy (within 5% of actual): {accuracy * 100:.2f}%')

# Calculate the mean of the High and Low prices
mean_high = df['High'].mean()
mean_low = df['Low'].mean()

# Define the trading strategy
df['Action'] = df['Close'].apply(lambda x: 'Sell' if x > mean_high else ('Buy' if x < mean_low else 'Hold'))

# Display the first few rows to see the applied actions
print(df[['Date', 'Close', 'Action']])

# Create bar chart
plt.bar(df['Action'], df['Date'], color=['blue', 'green', 'orange'])

# Add labels and title
plt.xlabel('Action')
plt.title('Column Visualization of Three Categories')

plt.yticks([])

# Show the plot
plt.show()