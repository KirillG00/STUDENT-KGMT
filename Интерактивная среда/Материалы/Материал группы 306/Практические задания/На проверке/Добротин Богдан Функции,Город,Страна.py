import unittest
from city_functions_Добротин import format_city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.maim()