from ride import Ride


class Car:

    def __init__(self, id):
        id = int(id)
        self.row = 0
        self.column = 0
        self.completed_rides = []
        self.total_move = 0

    def calculate_distance(self, ride: Ride):
        return (self.row - ride.start_row) + (self.column - ride.start_column)

