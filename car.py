from ride import Ride
import math

class Car:

    def __init__(self, id):
        self.id = int(id)
        self.row = 0
        self.column = 0
        self.completed_rides = []
        self.rides = []
        self.total_move = 0
        self.is_moving = False

    def calculate_distance(self, ride: Ride):
        return math.fabs((self.row - ride.start_row) + (self.column - ride.start_column))

    def __repr__(self):
        return "<Car %s>" % self.id

    def assign_ride(self, ride: Ride):
        self.rides.append(ride.id)
