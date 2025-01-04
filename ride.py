from datetime import datetime


class Ride:
    def __init__(self, start_loc, end_loc):
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.driver = None  # driver er obj
        self.rider = None  # Rider er obj
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.initial_amount -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self):
        return f"Ride details. Start location: {self.start_time}, Estimated fare: {self.estimated_fare}"


class RideReq:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_drivers(self, ride_req):
        if len(self.available_drivers) > 0:
            driver = self.available_drivers[0]
            ride = Ride(ride_req.rider.current_loc, ride_req.end_loc)
            driver.accept_ride(ride)
            return ride
