from dependencies import *
from preprocessing import *
from train import *


def predict_weather(date, time):


  input_data = pd.DataFrame({'date': [date], 'time': [time]})
  prediction = tree_regressor.predict(input_data)

  return prediction


date = input("Enter the date (DDMMYYYY): ")
time = input("Enter the time (HHMM-24h): ")


prediction = predict_weather(date, time)

for i, column in enumerate(Y.columns):
  print(f"{column}: {prediction[0][i]}")
