import unittest
from unittest.mock import MagicMock # MagicMock allows stubbing of methods onto real classes
from tests.fixtures.mock import Mock # import fake Mock class from PROJECT/tests/fixtures/mock.py
from airportchallenge.airport import Airport # PROJECT/airportchallenge/airport.py

class TestAirport(unittest.TestCase):

    def setUp(self):
        # stuff in setUp happens before each test
        # create a new instance of the Mock class (created at bottom of test)
        self.weather = Mock()
        # assign the weather object a function of is_stormy which returns False
        self.weather.is_stormy = MagicMock(return_value=False)
        # mock a plane
        self.plane = Mock()
        # create a new instance of Airport and dependency inject the weather mock
        self.airport = Airport(self.weather)

    def tearDown(self):
        # stuff here happens after each test
        pass

    def test_planes(self):
        # expect airport.planes to equal empty array
        self.assertEqual(self.airport.planes, [])

    def test_landing(self):
        # land the plane mock
        self.airport.land(self.plane)
        # expect airport.planes to contain an array with plane mock inside of it
        self.assertEqual(self.airport.planes, [self.plane])

    def test_takeoff(self):
        self.airport.land(self.plane)
        self.airport.takeoff(self.plane)
        self.assertEqual(self.airport.planes, [])

    def test_landing_stormy(self):
        # override the previous return value of is_stormy
        self.weather.is_stormy = MagicMock(return_value=True)
        # expect an error when airport.land is called
        self.assertRaises(RuntimeError, lambda x: self.airport.land(self.plane), "Plane can't land in stormy weather.")
        self.assertEqual(self.airport.planes, [])

    def test_takeoff_stormy(self):
        self.airport.land(self.plane)
        self.weather.is_stormy = MagicMock(return_value=True)
        self.assertRaises(RuntimeError, lambda x: self.airport.takeoff(self.plane), "Plane can't takeoff in stormy weather.")
        self.assertEqual(self.airport.planes, [self.plane])
