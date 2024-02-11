import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split




temperature_dataset = pd.read_csv("D:\Goal\pycool\Temperature_Predection\Dataset\weather_history_bangladesh.csv")

# temperature_dataset.head()