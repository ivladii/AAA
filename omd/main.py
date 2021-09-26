import random
import balaboba
import weather


def step2_no_umbrella(is_rain: bool) -> str:
    """
    Возвращает затравку для истории, если утка не возьмёт с собой зонт
    """
    if is_rain:
        history_seed = 'Утка напрасно не взяла с собой зонт'
    else:
        history_seed = 'Утка не прогодала, не взяв с собой зонт'

    return history_seed


def step2_umbrella(is_rain: bool) -> str:
    """
    Возвращает затравку для истории, если утка возьмёт с собой зонт
    """
    if is_rain:
        history_seed = 'Утка не прогодала, взяв с собой зонт'
    else:
        history_seed = 'Утка напрасно взяла с собой зонт'

    return history_seed


def step1() -> str:
    """
    Алгоритм принятия решения по поводу того, брать утке зонт или нет
    """
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {
        'да': True,
        'нет': False,
        'хз': random.choice([True, False])
    }
    weather_now = weather.get_weather_now()
    is_rain = weather.check_rain(weather_now)
    print(weather_now)
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella(is_rain)
    return step2_no_umbrella(is_rain)


def main():
    history_seed = step1()
    history = balaboba.balaboba(history_seed)
    print(history)


if __name__ == '__main__':
    main()