from tests.code.one_hot_encoder import fit_transform
import pytest


def test_equal():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_notin():
    cities = ['Moscow']
    transformed_cities = fit_transform(cities)[0]

    assert 0 not in transformed_cities[-1]


def test_raise():
    with pytest.raises(TypeError):
        fit_transform()


def test_true():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    transformed_cities = fit_transform(cities)
    one_in_row = all(sum(row[1]) == 1 for row in transformed_cities)

    assert one_in_row is True


if __name__ == '__main__':
    pytest.main()
