# Define the Bus class
class Bus:
    # Initialize the bus with route number, start point, destination, and travel time
    def __init__(self, route_number, start_point, destination, travel_time):
        self.route_number = route_number
        self.start_point = start_point
        self.destination = destination
        self.travel_time = travel_time

    # Method to set and get route number
    def set_number(self, route_number):
        self.route_number = route_number

    def get_number(self):
        return self.route_number

    # Method to set and get start point
    def set_start_point(self, start_point):
        self.start_point = start_point

    def get_start_point(self):
        return self.start_point

    # Method to set and get destination
    def set_destination(self, destination):
        self.destination = destination

    def get_destination(self):
        return self.destination

    # Method to set and get travel time
    def set_travel_time(self, travel_time):
        self.travel_time = travel_time

    def get_travel_time(self):
        return self.travel_time

    # Method to display bus information
    def info(self):
        return (f"Route number: {self.route_number}\n"
                f"Starting point: {self.start_point}\n"
                f"Destination point: {self.destination}\n"
                f"Travel time: {self.travel_time}")

# Create a Bus object
bus = Bus(422, "Moscow", "Minsk", "10:15")

# Change the route number and get the updated value
bus.set_number(244)
print(bus.get_number())  # Output: 244

# Display all bus information
print(bus.info())
