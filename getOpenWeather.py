import requests, json, pyperclip
from pathlib import Path

APPID = ''

location = 'San Francisco'

GeocodingURL =f'http://api.openweathermap.org/geo/1.0/zip?zip=E14,GB&appid={APPID}' 
Geocoding = requests.get(GeocodingURL)
Geocoding.raise_for_status() 
GeocodingStr = json.loads(Geocoding.text)
lat = GeocodingStr['lat']
lon = GeocodingStr['lon']
WeatherURL = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APPID}'
WeatherJSON = requests.get(WeatherURL)
WeatherJSON.raise_for_status()
WeatherStr = json.loads(WeatherJSON.text)
print(Geocoding.text)
print(WeatherStr)
pyperclip.copy(WeatherJSON.text)
