import csv
from faker import Faker
from random import choice, uniform, randint


DEP_MARKETING = 'Маркетинг'
DEP_SALES = 'Продажи'
DEP_DEVEL = 'Разработка'
DEP_ANALYTICS = 'Аналитика'
DEP_ACCOUNTING = 'Бухгалтерия'
DEP_ALL = (
    DEP_MARKETING,
    DEP_SALES,
    DEP_DEVEL,
    DEP_ANALYTICS,
    DEP_ACCOUNTING,
)

OCCUPATION_BY_DEP = {
    DEP_MARKETING: ('Маркетинг-менеджер', ),
    DEP_SALES: ('Sales manager', 'Key account manager'),
    DEP_DEVEL: (
        'iOS-инженер',
        'Android-инженер',
        'Backend-инженер',
        'Frontend-инженер',
        'Продакт-менеджер',
    ),
    DEP_ACCOUNTING: ('Бухгалтер', ),
    DEP_ANALYTICS: ('ML-инженер', 'Data Science инженер', ),
}

AREA_BY_DEP = {
    DEP_MARKETING: ('Direct', 'Performance', ),
    DEP_SALES: ('B2C', 'B2B', 'Госы', ),
    DEP_DEVEL: ('Платформа', 'Основной продукт', 'Внутренний портал', ),
    DEP_ACCOUNTING: ('Компенсации и льготы', 'Зарплата', ),
    DEP_ANALYTICS: ('DWH', 'Product', ),
}

REPORT_HEADER_FIELDS = (
    'ФИО полностью',
    'Департамент',
    'Отдел',
    'Должность',
    'Оценка',
    'Оклад',
)

SALARY_MIN = 55000
SALARY_MAX = 125000

PERF_SCORE_MIN = 3.5
PERF_SCORE_MAX = 5.0


faker_gen = Faker('ru_RU')
with open('Corp Summary.csv', 'w') as f:
    out_file = csv.writer(f, delimiter=';')
    out_file.writerow(REPORT_HEADER_FIELDS)
    for _ in range(200):
        dep_name = choice(DEP_ALL)
        area_name = choice(AREA_BY_DEP[dep_name])
        occupation = choice(OCCUPATION_BY_DEP[dep_name])

        out_file.writerow((
            faker_gen.name(),
            dep_name,
            area_name,
            occupation,
            '{:3.1f}'.format(uniform(PERF_SCORE_MIN, PERF_SCORE_MAX)),
            randint(SALARY_MIN, SALARY_MAX) // 100 * 100,
        ))