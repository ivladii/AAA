import requests
import random
import json
import urllib.request


def check_rain() -> bool:
    """
    Функция выводит прогноз погоды на данный момент
    и возвращает True, если идёт дождь, в противном случае False
    """
    url = f'https://wttr.in/'
    weather_parameters = {
        '0': '',
        'M': '',
        'lang': 'ru'
    }
    wheather = requests.get(url, params=weather_parameters).text
    print(wheather)
    return 'дожд' in wheather


def pabalabol(query: str) -> str:
    """
    API для https://yandex.ru/lab/yalm для генерации рандомных историй
    """
    API_URL = 'https://zeapi.yandex.net/lab/api/yalm/text3'
    headers = {'Content-Type': 'application/json'}
    payload = {"query": query, "intro": 0, "filter": 1}
    params = json.dumps(payload).encode('utf8')
    req = urllib.request.Request(API_URL, data=params, headers=headers)
    response = urllib.request.urlopen(req)
    json_response = json.loads(response.read().decode('utf8'))
    history = '\n' + json_response['query'] + json_response['text']
    return history


def step2_umbrella(is_rain: bool) -> str:
    """
    Выводит затравку для истории, если утка возьмёт с собой зонт
    """
    if is_rain:
        history_seed = 'Утка не прогодала, взяв с собой зонт'
    else:
        history_seed = 'Утка напрасно взяла с собой зонт'

    return history_seed


def step2_no_umbrella(is_rain: bool) -> str:
    """
    Выводит текст с историей о том, что случится с уткой, не взяв с собой зонт
    """
    if is_rain:
        history_seed = 'Утка напрасно не взяла с собой зонт'
    else:
        history_seed = 'Утка не прогодала, не взяв с собой зонт'

    return history_seed


def step1() -> str:
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {
        'да': True,
        'нет': False,
        'пусть сама решает': random.choice([True, False])
    }
    is_rain = check_rain()
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella(is_rain)
    return step2_no_umbrella(is_rain)


if __name__ == '__main__':
    print(pabalabol(step1()))