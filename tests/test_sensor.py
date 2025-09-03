import unittest
from ..sensor import Sensor

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = Sensor(0, 1)

    def test_read_data(self):
        for i in range(100):
            _, value = self.sensor.read_data()
            self.assertGreaterEqual(value, self.sensor.min_value)
            self.assertLessEqual(value, self.sensor.max_value)

if __name__ == '__main__':
    unittest.main()

