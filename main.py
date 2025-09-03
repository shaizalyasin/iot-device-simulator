import random
from datetime import datetime

# Import the required classes from the respective modules
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard

# Define the main function
def main():
    # Create an instance of the Sensor class with min and max values
    sensor = Sensor(0, 100)
    # Print the sensor instance
    #print (sensor)

    # Read data from the sensor
    data = sensor.read_data()
    # Create an instance of the DataProcessor class with the sensor data
    data_processor = DataProcessor(data)

    # Create an instance of the Communication class with a server URL
    communication = Communication("https://central-server.example.com")

    # Create an instance of the Device class with the sensor, data_processor and communication instances
    device = Device(sensor, data_processor, communication)

    # Create an instance of the Dashboard class
    dashboard = Dashboard()

    # Collect data from the device for a specified number of times
    device.collect_data(10)
    # Process the collected data
    processed_data = device.process_data()
    print ('Muhammad', processed_data)

    # Send the processed data to the central server
    device.send_data_to_server(processed_data)
    # Receive data from the central server
    device.receive_data_from_server()

    # Display the collected sensor data on the dashboard
    dashboard.display_data(device.data)
    # Display the calculated analytics results on the dashboard
    dashboard.display_analytics(processed_data)


if __name__ == "__main__": # why this line is needed? (A Python programme uses the condition if __name__ == '__main__'
    # to only run the code inside the if statement when the program is run directly by the Python
    # interpreter. The code inside the if statement is not executed when the file's code is imported
    # as a module.)
    main()
