class Vehicle:
    def __init__(self, num_of_wheels, num_of_passengers):
        self.num_of_wheels = num_of_wheels
        self.num_of_passengers = num_of_passengers

    def print_info(self):
        print(self.num_of_wheels)


class Car(Vehicle):
    def __init__(self, num_of_wheels, num_of_passengers, make):
        self.make = make
        super().__init__(num_of_wheels, num_of_passengers)

    def print_info(self):
        print(f'Make: {self.make}, Wheels: {self.num_of_wheels}!')

    def print_only_wheels(self):
        super().print_info()


myVehicle = Vehicle(4, 10)
myCar = Car(2, 4, "Toyota")

myVehicle.print_info()
myCar.print_info()
myCar.print_only_wheels()


for j in range(10):
    print(j)
