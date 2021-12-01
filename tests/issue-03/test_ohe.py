from tests.code.one_hot_encoder import fit_transform
import unittest


class TestOheHotEncoding(unittest.TestCase):

    def test_equal(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_notin(self):
        cities = ['Moscow']
        transformed_cities = fit_transform(cities)[0]

        self.assertNotIn(0, transformed_cities[-1])

    def test_raise(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_true(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed_cities = fit_transform(cities)
        one_in_row = all(sum(row[1]) == 1 for row in transformed_cities)

        self.assertTrue(one_in_row)


if __name__ == '__main__':
   unittest.main()
