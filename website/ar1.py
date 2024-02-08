import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

url = 'https://raw.githubusercontent.com/CrazyImmortal/dustdensity/main/dustdensity.csv'
try:
    df = pd.read_csv(url, header=0, index_col=0, parse_dates=True)
except Exception as e:
    print(f"Error reading data: {e}")
    df = None

if df is not None:
    fig, ax = plt.subplots()
    for i in range(len(df)):
        ax.annotate(str(float(df.iloc[i].values[0])), xy=(df.index[i], df.iloc[i].values[0]), xytext=(5, 2), 
                    textcoords='offset points', ha='right', va='bottom')
    ax.plot(df.index, df.values, label='Actual', marker='o')
    plt.show()

    model = AutoReg(df, lags=7)
    model_fit = model.fit()

    print(model_fit.summary())

    forecast = model_fit.forecast(steps=7)

    print("Forecast:")
    print(forecast)

    # Convert the forecast to a Pandas DataFrame
    forecast_df = pd.DataFrame(forecast, columns=['Forecast'], index=pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=7, freq='D'))

    # Save the forecast to a CSV file
    forecast_df.to_csv('forecast.csv', float_format='{:.0f}'.format)

    fig, ax = plt.subplots()
    for i in range(len(df)):
        ax.annotate(str(float(df.iloc[i].values[0])), xy=(df.index[i], df.iloc[i].values[0]), xytext=(5, 2), 
                    textcoords='offset points', ha='right', va='bottom')
    ax.plot(df.index, df.values, label='Actual', marker='o')
    for i in range(len(forecast)):
        ax.annotate(str(float(forecast[i])), xy=(forecast.index[i], forecast[i]), xytext=(5, 2), 
                    textcoords='offset points', ha='right', va='bottom')
    ax.plot(forecast.index, forecast, label='Predicted', marker='o')
    plt.legend()
    plt.show()
