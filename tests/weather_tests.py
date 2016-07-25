import unittest
from unittest.mock import MagicMock
from tests.fixtures.mock import Mock
from airportchallenge.weather import Weather

class TestWeather(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_stormy_false(self):
        self.random_not_stormy = Mock()
        self.random_not_stormy.random = MagicMock(return_value=0.5)
        self.weather = Weather(self.random_not_stormy)
        self.assertEqual(self.weather.is_stormy(), False)

    def test_is_stormy_true(self):
        self.random_stormy = Mock()
        self.random_stormy.random = MagicMock(return_value=0.2)
        self.weather = Weather(self.random_stormy)
        self.assertEqual(self.weather.is_stormy(), True)
