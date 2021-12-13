import sys
from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text):
    string_text = string_text.strip()
    if string_text != '':
        current_date = datetime.now().strftime('%Y-%M-%d %H:%M:%S')
        new_string = f'[{current_date}]: {string_text}\n'
        original_write(new_string)


if __name__ == '__main__':
    sys.stdout.write = my_write
    print('1, 2, 3')
    sys.stdout.write = original_write
