import unittest
from io import StringIO
from ..dashboard import Dashboard

class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.dashboard = Dashboard()
        self.sensor_data = [('2022-05-01 12:30:45.123456', 10), ('2022-05-01 12:31:45.123456', 15), ('2022-05-01 12:32:45.123456', 20)]

    def test_display_data(self):
        # Redirect stdout to StringIO object for testing
        captured_output = StringIO()
        import sys
        sys.stdout = captured_output

        self.dashboard.display_data(self.sensor_data)

        sys.stdout = sys.__stdout__
        # Get the printed output
        output = captured_output.getvalue().strip()

        # Assert that the output matches the expected format
        expected_output = """Sensor Data:
2022-05-01 12:30:45.123456: 10
2022-05-01 12:31:45.123456: 15
2022-05-01 12:32:45.123456: 20"""
        self.assertEqual(output, expected_output)

    def test_display_analytics(self):
        # Redirect stdout to StringIO object for testing
        captured_output = StringIO()
        import sys
        sys.stdout = captured_output

        analytics = (15, 10, 20)
        self.dashboard.display_analytics(analytics)

        sys.stdout = sys.__stdout__
        # Get the printed output
        output = captured_output.getvalue().strip()

        # Assert that the output matches the expected format
        expected_output = """Analytics:
Average: 15
Minimum: 10
Maximum: 20"""
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
