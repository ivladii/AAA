import csv
from collections import defaultdict
from typing import List, Dict

PATH_RAW_DATA = './Corp Summary.csv'
PATH_DEPARTMENT_SUMMARY = './department_summary.csv'

TASKS = {
    1: 'Вывести иерархию команд',
    2: 'Вывести сводный отчёт по департаментам',
    3: 'Сохранить сводный отчёт по департаментам'
}


def read_csv(path: str) -> List[dict]:
    """
    Читает csv-файл

    Параметры:
    - path: str

    Возвращает:
    - data: List[dict]

    """
    with open(path, 'r', newline='\n') as file:
        reader = csv.DictReader(file, delimiter=';')
        data = [row for row in reader]
    return data


def select_task_id(tasks: dict) -> int:
    """
    Функция спрашивает у пользователя, какую задачу он хочет выполнить

    Параметры:
    - tasks: dict
        - Перечень задач, которые готова выполнить система

    Возвращает:
    - task_id: int
    """

    output_tasks = '\n'.join(
        [
            '. '.join(map(str, task))
            for task in tasks.items()
        ]
    )
    print(f'Что хочешь сделать?\n{output_tasks}')

    task_id = None
    while not tasks.get(task_id):
        task_id = input('Введи номер задачи: ')
        if task_id.isdigit():
            task_id = int(task_id)

        if not tasks.get(task_id):
            print(f'❌ Нужно ввести цифорку от {min(tasks.keys())} до {max(tasks.keys())}')

    return task_id


def execute_task(task_id: int, workers: List[dict]):
    """
    Выполняет указанную задачу

    Параметры:
    - task_id: int
    - workers: List[dict]
        - список с описанием сотрудников компании
    """
    if task_id == 1:
        pretty_command_hierarchy(get_command_hierarchy(workers))
    elif task_id == 2:
        pretty_department_summary_report(get_department_summary_report(workers))
    elif task_id == 3:
        write_csv(get_department_summary_report(workers), PATH_DEPARTMENT_SUMMARY)


# task_id = 1

def get_command_hierarchy(workers: List[dict]) -> Dict[str, tuple]:
    """
    Опрелеяет, какие отделы входят в департамент

    Параметры:
    - workers: List[dict]
        - список с описанием сотрудников компании

    Возвращает:
    - command_hierarchy: Dict[str, tuple]
        - Связка департамент и входящие в него отделы

    """
    command_hierarchy = defaultdict(set)
    for worker in workers:
        command_hierarchy[worker['Департамент']].add(worker['Отдел'])

    command_hierarchy = {
        department: tuple(branches)
        for department, branches
        in command_hierarchy.items()
    }

    return command_hierarchy


def pretty_command_hierarchy(command_hierarchy: Dict[str, tuple], **kwargs):
    """
    Выводит в читабельном виде иерархию команд

    Параметры:
    - command_hierarchy: Dict[tuple]
        - Связка департамент и входящие в него отделы
    """
    point = kwargs.get('point', '-')
    indent = kwargs.get('indent', 2)

    for department, commands in command_hierarchy.items():
        print(point, department)
        for command in commands:
            print(' '*indent, point, command)


# task_id = 2

def get_department_summary_report(workers: List[dict]) -> Dict[str, dict]:
    """
    Считает сводный отчёт по департаментам:
    количество сотрудников, минимальный, средний, максимальный оклады

    Параметры:
    - workers: List[dict]
        - список с описанием сотрудников компании

    Возвращает:
    - department_summary_report: Dict[str, dict]
        - сводный отчёт по департаментам
    """
    department_salaries = defaultdict(list)
    for worker in workers:
        department_salaries[worker['Департамент']].append(int(worker['Оклад']))

    department_summary_report = defaultdict(dict)
    for department_name, salaries in department_salaries.items():
        department_summary_report[department_name]['Сотрудников'] = len(salaries)
        department_summary_report[department_name]['Минимальный оклад'] = min(salaries)
        department_summary_report[department_name]['Максимальный оклад'] = max(salaries)
        department_summary_report[department_name]['Средний оклад'] = round(sum(salaries) / len(salaries))

    return department_summary_report


def pretty_department_summary_report(department_summary_report: Dict[str, dict], **kwargs):
    """
    Выводит в читабельном виде сводный отчёт по департаментам

    Параметры:
    - department_summary_report: Dict[dict]
        - агрегированная статистика по департаментам
    """
    point = kwargs.get('point', '-')
    indent = kwargs.get('indent', 2)

    for department, params in department_summary_report.items():
        print(point, department)
        print(' '*indent, point,
              'Сотрудников:', params['Сотрудников'])
        print(' ' * indent, point,
              'Вилка зарплат:',
              '-'.join(map(str, [params['Минимальный оклад'], params['Средний оклад'], params['Максимальный оклад']])))


# task_id = 3

def write_csv(data: Dict[str, dict], path: str):
    """
    Записывает данные в csv-файл

    Параметры:
    - data: Dict[str, dict]
    - path: str
    """
    data_format = [{**{'Департамент': key}, **val} for key, val in data.items()]
    fieldnames = data_format[0].keys()
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_format)

    print(f'Файл сохранён в {path}')


def main():

    workers = read_csv(PATH_RAW_DATA)

    while True:
        task_id = select_task_id(TASKS)
        execute_task(task_id, workers)

        answer = input('Что нибудь ещё?(да/нет)')
        if answer != 'да':
            exit()


if __name__ == '__main__':
    main()