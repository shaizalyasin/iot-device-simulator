import unittest
from ..data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.data = [('2022-05-01 12:00:00', 10), ('2022-05-01 12:01:00', 20), ('2022-05-01 12:02:00', 30)]
        self.dp = DataProcessor(self.data)

    def test_calculate_average(self):
        self.assertEqual(self.dp.calculate_average(self.data), 20)

    def test_calculate_min(self):
        self.assertEqual(self.dp.calculate_min(self.data), 10)

    def test_calculate_max(self):
        self.assertEqual(self.dp.calculate_max(self.data), 30)


if __name__ == '__main__':
    unittest.main()