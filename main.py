import requests
from pprint import pprint
# Copy your generated API key here from api.openweathermap.org
API_Key=''

city= input(' Type a city : ')

base_url= 'https://api.openweathermap.org/data/2.5/weather?appid='+API_Key

weather_data=requests.get(base_url).json()

pprint(weather_data)
