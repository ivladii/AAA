import json
from typing import Union


class ParserJSON:

    def __init__(self, some_json: Union[dict, str]):
        if isinstance(some_json, dict):
            self._data = some_json
        else:
            self._data = json.loads(some_json)

    def add(self, key, value):
        self._data[key] = value

    @property
    def info_(self):
        return self._data

    def __getattr__(self, item):
        value = self._data.get(item)
        if value is None:
            raise AttributeError(f'{item} is not exists')
        if isinstance(value, dict):
            value = self.__class__(value)
        return value

    def __setattr__(self, key, value):
        __dict__ = super().__getattribute__('__dict__')
        if key in __dict__.get('_data', {}):
            __dict__.get('_data')[key] = value
        else:
            __dict__[key] = value


class BaseAdvert(ParserJSON):

    def __init__(self, some_json: Union[dict, str]):
        super().__init__(some_json)

        if self._data.get('title') is None:
            raise AttributeError('title is not exists')

        if self._data.get('price') is None:
            self.add('price', 0)
        elif self._data.get('price') < 0:
            raise ValueError('price must be >= 0')

    def __getattr__(self, item):
        value = self._data.get(item)
        if value is None:
            raise AttributeError(f'{item} is not exists')
        if isinstance(value, dict):
            value = ParserJSON(value)
        return value

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('price must be >= 0')
        else:
            super().__setattr__(key, value)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin:

    """Разукрашивает вывод в консоль"""

    repr_color_code = 32

    def __repr__(self):
        output = super().__repr__()
        format_code = f'\033[0;{self.repr_color_code};1m '
        return format_code + output


class Advert(ColorizeMixin, BaseAdvert):

    def __init__(self, some_json: Union[dict, str]):
        super().__init__(some_json)


if __name__ == '__main__':
    iphone_attrs = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": {
                "street": "город Самара, улица Мориса Тореза",
                "house": 50
            },
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }
    """
    iphone = Advert(iphone_attrs)
    print('title is: ', iphone.title)
    print('info is: ', iphone.location.info_)
    print('drill down is: ', iphone.location.address.street)

    try:
        iphone.price = -1
    except ValueError as ve:
        print(f'ValueError: {ve}')

    banana_attrs = """{
        "title": "Banana"
    }
    """
    banana = Advert(banana_attrs)

    print('repr is: ', banana)
