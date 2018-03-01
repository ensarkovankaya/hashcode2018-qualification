from input import parse
from car import Car
from ride import Ride


class Map:
    def __init__(self, filepath="b_should_be_easy.in"):
        data = parse(filepath)
        self.cars = []
        for vehicle_id in range(data.get('vehicles')):
            self.cars.append(Car(vehicle_id))

        self.rides = []
        for ride_id in data.get('rides'):
            ride_info = data.get('rides').get(ride_id)
            self.rides.append(Ride(ride_id, **ride_info))

        self.rows = data.get('rows')
        self.columns = data.get('columns')
        self.number_of_rides = data.get('number_of_rides')
        self.bonus = data.get('bonus')
        self.total_steps = data.get('total_steps')

    def assign_ride_to_car(self, ride: Ride, car: Car):
        print(f'Ride {ride.id} assigned to Car {car.id}')
        car.assign_ride(ride)

    def run(self):
        current_step = 0
        while current_step < self.total_steps:
            for car in self.cars:
                if not car.busy:
                    min_distance = None
                    min_distance_ride = None
                    for ride in self.rides:
                        if not ride.is_taken:
                            distances = car.calculate_distance(ride)
                            if not min_distance or distances < min_distance:
                                min_distance = distances
                                min_distance_ride = ride

                    self.assign_ride_to_car(min_distance_ride, car)

            for car in self.cars:
                car.move_or_wait()
