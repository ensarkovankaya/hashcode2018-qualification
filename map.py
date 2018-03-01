from input import parse
from car import Car
from ride import Ride


class Map:
    def __init__(self, filepath="b_should_be_easy.in"):
        data = parse(filepath)
        self.all_cars = []
        self.moving_cars = []
        for vehicle_id in range(data.get('vehicles')):
            self.all_cars.append(Car(vehicle_id))
            self.not_moving_cars = self.all_cars.copy()

        self.all_rides = []
        self.assigned_rides = []
        self.unassigned_rides = []

        for ride_id in data.get('rides'):
            ride_info = data.get('rides').get(ride_id)
            self.all_rides.append(Ride(ride_id, **ride_info))
            self.unassigned_rides = self.all_rides.copy()

        self.rows = data.get('rows')
        self.columns = data.get('columns')
        self.number_of_rides = data.get('number_of_rides')
        self.bonus = data.get('bonus')
        self.total_steps = data.get('total_steps')

    def assign_ride_to_car(self, ride: Ride, car: Car):
        car.assign_ride(ride)
        self.assigned_rides.append(ride.id)
        self.unassigned_rides.pop(ride.id)

    def run(self):
        for car in self.not_moving_cars:
            min_distance = None
            min_distance_ride = None
            for ride in self.unassigned_rides:
                distances = car.calculate_distance(ride)
                if not min_distance or distances < min_distance:
                    min_distance = distances
                    min_distance_ride = ride

            self.assign_ride_to_car(min_distance_ride, car)

