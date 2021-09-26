import requests

URI = 'https://wttr.in/'

weather_parameters = {
    '0': '',
    'M': '',
    'lang': 'ru'
}


def get_weather_now() -> str:
    """Получает прогноз погоды на данный момент"""
    return requests.get(URI, params=weather_parameters).text


def check_rain(weather: str) -> bool:
    """Проверяет, есть ли дождь"""
    return 'дожд' in weather


if __name__ == '__main__':
    weather = get_weather_now()
    print(weather, check_rain(weather))
