#For running test cases we have to import like this other wise it will give error:attempted relative import with no known parent package 
# from .sensor import Sensor
# from .data_processor import DataProcessor
# from .communication import Communication

from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication

class Device:
    def __init__(self, sensor, data_processor, communication):
        self.sensor = sensor
        self.data_processor = data_processor
        self.communication = communication
        self.data = []

    def collect_data(self, num_samples):
        try:
            for _ in range(num_samples):
                self.data.append(self.sensor.read_data())
        except Exception as e:
            print(f"Error collecting data: {e}")
            # raising an exception here instead of just printing the error message.

    def process_data(self):
        try:
            if not self.data:
                raise ValueError("No data to process.")
            average = self.data_processor.calculate_average(self.data)
            min_value = self.data_processor.calculate_min(self.data)
            max_value = self.data_processor.calculate_max(self.data)
            return average, min_value, max_value
        except Exception as e:
            print(f"Error processing data: {e}")

    
    def send_data_to_server(self, processed_data):
        try:
            self.communication.send_data(processed_data)
        except Exception as e:
            print(f"Error sending data to server: {e}")

    def receive_data_from_server(self):
        try:
            self.communication.receive_data()
        except Exception as e:
            print(f"Error receiving data from server: {e}")

