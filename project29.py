'''Make a child class for the Bus that inherits from the Vehicle class. Any
vehicle's default fare price is seating capacity * 100. For example, we must
add a maintenance charge of 10% to the full fare. As a result, the final fare
for a bus ride will be equal to the total fare plus 10% of the total fare.

The bus has a seating capacity of 50 people. As a result, the total fare should
be INR 5500. In the Bus class, you must override the fare() method of the
Vehicle class.'''
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100
class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        return total_fare + (total_fare * 0.1)
bus = Bus(50)
print("Total Bus fare is: ₹", bus.fare())
