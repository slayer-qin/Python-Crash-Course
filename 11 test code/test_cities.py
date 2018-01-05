import unittest
import city_functions


class CitiesTestCases(unittest.TestCase):
    """测试city_functions"""

    def test_city_country(self):
        formatted_city = city_functions.city_country("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")

    def test_city_country_population(self):
        formatted_city = city_functions.city_country("Santiago", "Chile", 5000000)
        self.assertEqual(formatted_city, "Santiago, Chile - population 5000000")


unittest.main()
