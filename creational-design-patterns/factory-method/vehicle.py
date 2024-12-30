class Vehicle:
  def __init__(self, vehicle_type):
    self.vehicle_type = vehicle_type

  def start(self):
    if self.vehicle_type == "car":
      print('Starting the car ...')
    elif self.vehicle_type == "motorcycle":
      print('Starting the motorcycle ...')
    elif self.vehicle_type == "bycicle":
      print('Starting the bycicle ...')
    else:
      print('Invalid vehicle type!')

if __name__ == "__main__":
  car = Vehicle('car')
  car.start()

  motorcycle = Vehicle('motorcycle')
  motorcycle.start()

  bycicle = Vehicle('bycicle')
  bycicle.start()

  invalid = Vehicle('invalid')
  invalid.start()

# Violation of Signle Responsibility Principle (SRP):
# The Vehicle class is responsible for both creating and starting vehicles.
# This violates the SRP, which states that a class should have only one reasone to change.
# In the absence of the Factory Method method, the Vehicle class takes on the responsibility of object creation along with its primary responsibility of starting vehicles.

# Tight Coupling:
# The client code (car = Vehicle('car'), motorcycle = Vehicle('motorcycle'), bicycle= Vehicle('bicycle)) directly creates instances of the Vehicle class and explicitly sets the vehicle type.
# This creates a tight coupling between the client code and the specific vehicle types.
# If new vehicle types are added or existing types are modified, the client code needs to be updated accordingly, which increases the maintenance efforts and instroduces a risk of introducing bugs.

# Lack of Abstraction:
# The code lacks an abstraction layer that represents a common interface for all different vehicle types.
# The absence of an abstraction makes it difficult to introduce new types of vehicles without modifying the Vehicle class.
# It also limits the ability to substitute different vihicle types at runtime or extend the code to handle more complex scenarios involving different behaviors for each vehicle type.

# Code Duplication:
# The conditional statements in the start() method result in code duplication.
# Each time a new vehicle type is added, the same conditional logic needs to be repeated.
# This violates the DRY (Don't Repeat Yourself) principle and leads to maintenance challenges, as any changes or fixes to the logic would require updating multiple places.

# Limited Flexibility and Scalability:
# Without the Factory Method pattern, it becomes harder to extend the code base with new types of vehicles or introduce changes to the existing vehicle creation and behavior.
# The lack of a clear separation of concerns and the tight coupling between the client code and the Vehicle class make the code less flexible and scaleable.

# By applying the Factory Method pattern, these drawbacks can be addressed. The pattern provides a structured approach to object creation, decouples the client code from specific implementations, introduces abstraction and flexibility, and promotes better code organization and maintainability.