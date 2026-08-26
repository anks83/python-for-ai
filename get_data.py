import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
if response.status_code == 200: 
    data = response.json()
    print(data)
else:
    raise Exception(f"API request failed with status code {response.status_code}")

daily_data = data['daily']
print(daily_data)

df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})


df['date'] = pd.to_datetime(df['date'])

print(df)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/paris_weather.csv')