import random
from datetime import datetime

class Sensor:
## create a class that simulate a sensor (a class that generate a random data), the data should be send with the timestamp
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def read_data(self):
        timestamp = datetime.now()
        value = random.uniform(self.min_value, self.max_value)
        return (timestamp, value)


# class TemperatureSensor(Sensor):
#     def __init__(self):
#         super().__init__(-10, 50)
#
#
# class HumiditySensor(Sensor):
#     def __init__(self):
#         super().__init__(0, 100)
#
#
# class LightSensor(Sensor):
#     def __init__(self):
#         super().__init__(0, 1000)
