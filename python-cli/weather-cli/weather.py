import requests

SAMPLE_API_KEY = 'b6907d289e10d714a6e88b30761fae22'


def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']
