import unittest
from city_functions_Гончаров import format_city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_string = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()