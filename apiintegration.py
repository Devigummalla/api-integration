# -*- coding: utf-8 -*-
"""apiintegration.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NLjTClZkX6WrCdm1VUsTVLPPbeYoevTr
"""

import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# OpenWeatherMap API Key (Replace 'your_api_key' with an actual API key)
API_KEY = "2a22f6e6f3280a1d7e137ec6e7cb6ba1"
CITY = "New York"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(URL)
data = response.json()
# Check if the API request was successful
    # Extract relevant data
timestamps = []
temperatures = []
humidities = []

for entry in data['list']:
    timestamps.append(datetime.datetime.fromtimestamp(entry['dt']))
    temperatures.append(entry['main']['temp'])
    humidities.append(entry['main']['humidity'])

    # Plot temperature and humidity trends
sns.set_style("whitegrid")
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()
ax1.plot(timestamps, temperatures, color='tab:red', marker='o', label='Temperature (°C)')
ax2.plot(timestamps, humidities, color='tab:blue', marker='s', linestyle='dashed', label='Humidity (%)')

    # Labels and title
ax1.set_xlabel("Date & Time")
ax1.set_ylabel("Temperature (°C)", color='tab:red')
ax2.set_ylabel("Humidity (%)", color='tab:blue')
plt.title(f"Weather Forecast for {CITY}")

    # Rotate x-axis labels
plt.xticks(rotation=45)
fig.tight_layout()
plt.show()

print(data)