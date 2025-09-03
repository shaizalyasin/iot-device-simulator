import unittest
from unittest.mock import Mock, patch
from ..sensor import Sensor
from ..data_processor import DataProcessor
from ..communication import Communication
from ..device import Device


class TestDevice(unittest.TestCase):

    def setUp(self):
        self.mock_sensor = Mock(spec=Sensor)
        self.mock_data_processor = Mock(spec=DataProcessor)
        self.mock_communication = Mock(spec=Communication)
        self.device = Device(self.mock_sensor, self.mock_data_processor, self.mock_communication)

    def test_collect_data(self):
        self.mock_sensor.read_data.side_effect = [(1, 2), (3, 4), (5, 6)]
        self.device.collect_data(3)
        self.assertEqual(self.device.data, [(1, 2), (3, 4), (5, 6)])


    def test_process_data_with_data(self):
        self.device.data = [(1, 2), (3, 4), (5, 6)]
        self.mock_data_processor.calculate_average.return_value = 3.0
        self.mock_data_processor.calculate_min.return_value = 2
        self.mock_data_processor.calculate_max.return_value = 6
        result = self.device.process_data()
        self.assertEqual(result, (3.0, 2, 6))

    def test_send_data_to_server(self):
        self.device.send_data_to_server((3.0, 2, 6))
        self.mock_communication.send_data.assert_called_with((3.0, 2, 6))

if __name__ == '__main__':
    unittest.main()



