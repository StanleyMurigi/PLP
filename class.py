# Base class
class Money:
    def __init__(self, from_name, to_name, amount):
        self.from_name = from_name
        self.to_name = to_name
        self.amount = amount

    def display_transaction(self):
        print(f"{self.from_name} sent ${self.amount} to {self.to_name}.")

    def reverse_transaction(self):
        return Money(self.to_name, self.from_name, self.amount)

# Subclass with inheritance and polymorphism
class InternationalMoneyTransfer(Money):
    def __init__(self, from_name, to_name, amount, exchange_rate, currency):
        super().__init__(from_name, to_name, amount)
        self.exchange_rate = exchange_rate
        self.currency = currency

    def display_transaction(self):
        converted_amount = self.amount * self.exchange_rate
        print(f"{self.from_name} sent {converted_amount:.2f} {self.currency} "
              f"(converted from ${self.amount}) to {self.to_name}.")

# Test the classes
# Local transaction
local = Money("Alice", "Bob", 150)
local.display_transaction()

# Reversing the local transaction
reversed_local = local.reverse_transaction()
reversed_local.display_transaction()

# International transaction
intl = InternationalMoneyTransfer("John", "Akira", 200, 1.25, "EUR")
intl.display_transaction()



class Vehicle:
    def move(self):
        pass

# Car class
class Car(Vehicle):
    def move(self):
        print("Driving")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Boat class
class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Bicycle class
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

# Test them all in a loop (Polymorphism in action)
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()