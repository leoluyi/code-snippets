import requests
from datetime import datetime

SAMPLE_API_KEY = 'b6907d289e10d714a6e88b30761fae22'


def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'units': 'metric',
        'lang': 'zh_tw',
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)
    print(response.url)
    weather = response.json()
    print(datetime.fromtimestamp(weather['dt']))

    return (weather['weather'][0]['description'],
            weather['main']['temp'],
            weather['main']['temp_min'],
            weather['main']['temp_max'])
