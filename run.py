from input import parse
from car import Car
from ride import Ride


class Game:
    def __init__(self, filepath="b_should_be_easy.in"):
        data = parse(filepath)
        self.cars = []
        for vehicle_id in range(data.get('vehicles')):
            self.cars.append(Car(vehicle_id))

        self.rides = []
        for ride_id in data.get('rides'):
            ride_info = data.get('rides').get(ride_id)
            self.rides.append(Ride(ride_id, **ride_info))

        self.moving_cars = []
        self.rows = data.get('rows')
        self.columns = data.get('columns')
        self.number_of_rides = data.get('number_of_rides')
        self.bonus = data.get('bonus')
        self.total_steps = data.get('total_steps')

    def run(self):
        pass
