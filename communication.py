
class Communication:
    def __init__(self, server_url):
        # Initialize the instance with the URL of the central server
        self.server_url = server_url

    def send_data(self, data):
        # Simulate sending the data payload to the server
        print(f"Sending data to {self.server_url}: {data}")

    def receive_data(self):
        # Simulate receiving data from the server
        print(f"Receiving data from {self.server_url}")

