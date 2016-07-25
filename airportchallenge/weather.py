import random

class Weather(object):

    def __init__(self, weather_probability=random):
        self.weather_probability = weather_probability

    def is_stormy(self):
        if self.weather_probability.random() < 0.25:
            return True
        else:
            return False
