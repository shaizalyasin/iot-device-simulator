import statistics

class DataProcessor:
    def __init__(self, data):
        self.data = data
    def calculate_average(self, data):
        """Calculate the average value of a list of data."""
        values = [d[1] for d in data]
        return statistics.mean(values)

    def calculate_min(self, data):
        """Calculate the minimum value of a list of data."""
        values = [d[1] for d in data]
        return min(values)

    def calculate_max(self, data):
        """Calculate the maximum value of a list of data."""
        values = [d[1] for d in data]
        return max(values)

# generate a class that takes the data from the sensor, does something with the data. Hint the timestamp needs to be addressed  as well
