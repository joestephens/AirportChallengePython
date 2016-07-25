class Airport(object):

    def __init__(self, weather):
        self.planes = []
        self.weather = weather

    def land(self, plane):
        if not self.weather.is_stormy():
            self.planes.append(plane)
        else:
            raise RuntimeError("Plane can't land in stormy weather.")

    def takeoff(self, plane):
        if not self.weather.is_stormy():
            self.planes.remove(plane)
        else:
            raise RuntimeError("Plane can't takeoff in stormy weather.")
