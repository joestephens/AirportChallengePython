import unittest
from airportchallenge.plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def tearDown(self):
        pass

    def test_is_new_object(self):
        self.assertEqual(type(self.plane), object)
