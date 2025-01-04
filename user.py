from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self,name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid

    @abstractmethod
    def display_profile(self):
        print(f"{self.name}, {self.email}")


class Rider(User):
    def __init__(self, name, email, nid, current_loc):
        super().__init__(name, email, nid)
        self.current_loc = current_loc
        self.initial_amount = 0

    def display_profile(self):
        print(f"{self.name}, {self.email}")

    def load_cash(self, amount):
        if amount > 0:
            self.initial_amount += amount
        else:
            print("Please give amount of more than 0")

    def request_ride(self, ride_sharing, destination):
        pass

    def show_current_ride(self):
        print(self.show_current_ride())


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f"{self.name}, {self.email}")

    def accept_ride(self, ride):
        pass


