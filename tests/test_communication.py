import unittest
from unittest.mock import patch
from ..communication import Communication

class TestCommunication(unittest.TestCase):
    def setUp(self):
        self.communication = Communication("http://example.com")

    def test_send_data(self):
        with patch('builtins.print') as mock_print:
            self.communication.send_data({"temp": 25.6, "humidity": 70})
            mock_print.assert_called_with("Sending data to http://example.com: {'temp': 25.6, 'humidity': 70}")

    def test_receive_data(self):
        with patch('builtins.print') as mock_print:
            self.communication.receive_data()
            mock_print.assert_called_with("Receiving data from http://example.com")


if __name__ == '__main__':
    unittest.main()