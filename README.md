# Placement Dost Virtual Internship

Welcome to my virtual internship experience at Placement Dost! This repository serves as a documentation hub for the projects and tasks I'll be working on during my internship period.

## About Placement Dost
Placement Dost is a dynamic platform committed to providing impactful internship opportunities for aspiring professionals like me. Through their internship program, they aim to nurture talents, facilitate learning, and foster professional growth by engaging interns in real-world projects and challenges.

## Internship Overview
During the 30-day internship period, I'll be involved in various tasks and projects, contributing to project analysis, report generation, and potentially participating in an intern competition during the final week. This internship presents a fantastic opportunity for me to apply my skills, gain practical experience, and enhance my professional visibility.

## Project 1 : Spam Email Detection using TensorFlow

This project aims to develop a machine learning model to automatically detect spam emails using TensorFlow. The goal is to ensure that the user's inbox remains clean by filtering out unwanted spam emails.

### Introduction

Spam emails pose a significant threat to email users, cluttering their inbox with unsolicited and potentially harmful content. By developing an effective spam email detection system, we can help users maintain a clean inbox and protect them from malicious attacks.

### Project Overview

- **Data Collection**: We collected a dataset of labeled emails, where each email is labeled as either spam or not spam (ham).
- **Data Preprocessing**: We preprocessed the text data to remove noise and convert it into a suitable format for model training.
- **Feature Extraction**: We extracted relevant features from the text data to feed into the machine learning model.
- **Model Building**: We built a machine learning model using TensorFlow, leveraging techniques such as neural networks for classification.
- **Model Training**: We trained the model using the preprocessed data and evaluated its performance.

### Google Colab Notebook

For detailed implementation and code, refer to the Google Colab notebook [here](https://colab.research.google.com/drive/1YrrCSMQOQAO-JuSFUYMafy16pKlTVE_0?usp=sharing).

### Dependencies

- TensorFlow
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

### Dataset

    https://www.kaggle.com/datasets/venky73/spam-mails-dataset/data

### Usage

1. Clone the repository:
    git clone https://github.com/Ayoub-etoullali/Virtual-Internships-Data-Science-PlacementDost

2. Open the Google Colab notebook in your browser and follow the instructions for data loading, preprocessing, model training, and evaluation.

3. Feel free to customize the model architecture, hyperparameters, or data preprocessing steps based on your requirements.

## Project 2 : Bitcoin Price Prediction.ipynb

### Overview : Trading Strategy: Mean Reversion Trading Strategy
This trading strategy aims to capitalize on mean reversion by comparing the closing price of a stock with the mean of the high and low prices. The strategy involves making buy, sell, or hold decisions based on the relationship between the closing price and the mean of the high and low prices.

### Strategy Description
- **Sell Condition**: If the closing price is greater than the mean of the high prices, sell the stock.
- **Buy Condition**: If the closing price is less than the mean of the low prices, buy the stock.
- **Hold Condition**: If the closing price falls between the mean of the high and low prices, hold the stock.

### Implementation
1. **Data Collection**: Obtain historical stock price data for the target stock.
2. **Data Preprocessing**: Clean the data and calculate the mean of the high and low prices.
3. **Trading Algorithm**:
    - Calculate the mean of the high and low prices for each trading period.
    - Compare the closing price with the mean of the high and low prices to determine buy, sell, or hold decisions.
4. **Backtesting**: Backtest the trading strategy using historical data to evaluate its performance.
5. **Risk Management**: Implement risk management techniques to mitigate potential losses, such as setting stop-loss orders or position sizing based on risk tolerance.
6. **Transaction Costs**: Consider transaction costs, including commissions, fees, and slippage, which can impact profitability.
7. **Continuous Monitoring**: Monitor the performance of the strategy and make adjustments as needed based on changing market conditions.

### Results
- Evaluate the performance of the strategy based on metrics such as profitability, risk-adjusted returns, and drawdowns.
- Compare the performance of the strategy against a benchmark index or buy-and-hold strategy.

### Conclusion
The Mean Reversion Trading Strategy provides a systematic approach to trading based on mean reversion principles. While the strategy offers a logical framework, it is essential to thoroughly backtest and refine it before deploying it in live trading. Additionally, consider incorporating risk management techniques and continuously monitoring the strategy's performance to adapt to changing market conditions.

### Dataset

    https://www.kaggle.com/datasets/meetnagadia/bitcoin-stock-data-sept-17-2014-august-24-2021

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<kbd>Enjoy Code</kbd> 👨‍💻
[My portfolio](https://ayoub-etoullali.netlify.app/)