import sys
from datetime import datetime


def timed_output(function):

    def wrapper(*args, **kwargs):

        original_write = sys.stdout.write

        def my_write(string_text):
            string_text = string_text.strip()
            if string_text != '':
                current_date = datetime.now().strftime('%Y-%M-%d %H:%M:%S')
                new_string = f'[{current_date}]: {string_text}\n'
                original_write(new_string)

        sys.stdout.write = my_write
        result = function(*args, **kwargs)
        sys.stdout.write = original_write

        return result

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting('Vlad')
