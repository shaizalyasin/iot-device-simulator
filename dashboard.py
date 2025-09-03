import random
from datetime import datetime

class Dashboard:
    def display_data(self, data):
        print("Sensor Data:")
        for timestamp, value in data:
            print(f"{timestamp}: {value}")

    def display_analytics(self, analytics):
        print("Analytics:")
        print(f"Average: {analytics[0]}")
        print(f"Minimum: {analytics[1]}")
        print(f"Maximum: {analytics[2]}")


# ## Bonos!
# # you can also generate some figures using the data and python modules like matplotlib, etc
# # if simple GUI can be used. Hint: you can use django
# # any extra flavor that you think it can add to the task. Hint(use your imagination and skills)


