class GpsScanInfo:
    def __init__(self, latitude, longitude, accuracy, time):
        self.latitude = latitude
        self.longitude = longitude
        self.accuracy = accuracy
        self.time = time

    def __str__(self):
        return f"latitude: {self.latitude}, longitude: '" \
               f"{self.longitude}, accuracy: {self.accuracy}, time: {self.time}"

    def __repr__(self):
        return f"GpsScanInfo({self.latitude}, {self.longitude}, {self.accuracy}, {self.time})"
