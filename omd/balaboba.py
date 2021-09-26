import json
from urllib.request import Request, urlopen
import sys


URI = "https://zeapi.yandex.net/lab/api/yalm/text3"


def balaboba(query: str) -> str:
    """
    API для https://yandex.ru/lab/yalm для генерации рандомных историй
    """
    headers = {'Content-Type': 'application/json'}
    payload = {'query': query, 'intro': 0, 'filter': 1}
    params = json.dumps(payload).encode('utf8')

    response = urlopen(Request(URI, data=params, headers=headers))
    json_response = json.loads(response.read().decode('utf8'))

    history = '\n' + json_response['query'] + json_response['text']

    return history


if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        for arg in args:
            print(balaboba(query=arg))
