from ride import Ride
import math


class Car:

    def __init__(self, id):
        self.id = int(id)
        self.row = 0
        self.column = 0
        self.completed_rides = []
        self.assigned_rides = []
        self.total_move = 0
        self.busy = False
        self.current_ride = None
        self.wait_for = 0

    def calculate_distance(self, ride: Ride):
        return math.fabs((self.row - ride.start_row) + (self.column - ride.start_column))

    def __repr__(self):
        return "<Car %s>" % self.id

    def move_or_wait(self):
        if self.wait_for > 0:
            self.wait_for -= 1
        else:
            self.busy = False
            self.current_ride = False

    def assign_ride(self, ride: Ride):
        self.assigned_rides.append(ride.id)
        self.current_ride = ride
        ride.is_taken = True
        self.busy = True
        self.wait_for = self.calculate_distance(ride) + ride.calculate_distance()
