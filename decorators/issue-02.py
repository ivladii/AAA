import sys
from datetime import datetime


def timed_output(function):
    def wrapper(*args, **kwargs):
        current_date = datetime.now().strftime('%Y-%M-%d %H:%M:%S')
        sys.stdout.write(f'[{current_date}]: ')
        function(*args, **kwargs)
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting('Vlad')
