import sys

PATH = './function_output.txt'


def redirect_output(filepath):

    def decorator(function):

        def wrapper(*args, **kwargs):

            def write_to_file(string_text):
                with open(filepath, 'a') as output:
                    output.write(string_text)

            original_write = sys.stdout.write
            sys.stdout.write = write_to_file
            result = function(*args, **kwargs)
            sys.stdout.write = original_write

            return result

        return wrapper

    return decorator


@redirect_output(PATH)
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()

    with open(PATH, 'r') as file:
        data = file.read()
    print(data)