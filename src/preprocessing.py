from src.dependencies import *

temperature_dataset['date'] = temperature_dataset['date'].astype(str)
temperature_dataset['date'] = temperature_dataset['date'].str.replace('/', '')
temperature_dataset['date'] = temperature_dataset['date'].astype(int)

temperature_dataset['time'] = pd.to_datetime(temperature_dataset['time']).dt.hour

temperature_dataset['wind'].fillna('Unknown', inplace=True)

conditions = {'Unknown': 0,
            'Fog': 1,
            'T-Storm': 2, 
            'Thunder': 3, 
            'Drizzle': 4, 
            'Rain': 5,
            'Haze': 6, 
            'Rain / Windy': 7, 
            'Squall': 8, 
            'Haze / Windy': 9, 
            'T-Storm / Windy': 10}

temperature_dataset['condition'] = [conditions[item]for item in temperature_dataset['condition']]

temperature_dataset['wind'].fillna('Unknown', inplace=True)

winds = {'Unknown': 0, 
         'CALM': 1, 
         'ENE': 2, 
         'NE': 3, 
         'E': 4, 
         'ESE': 5, 
         'NNE': 6, 
         'WNW': 7, 
         'N': 8,
         'NNW': 9, 
         'NW': 10, 
         'W': 11, 
         'WSW': 12, 
         'nan': 13, 
         'SSW': 14, 
         'SSE': 15, 
         'SW': 16, 
         'S': 17, 
         'SE': 18}
temperature_dataset['wind'] = [winds[item]for item in temperature_dataset['wind']]
