"""Code for Activity 1: Design Your Own Class (Smartphone + Inheritance)"""
# Parent class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
    
    def call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    def charge(self):
        print(f"Charging {self.model}... Battery life: {self.battery_life}%")

# Child class inheriting from Smartphone
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_resolution):
        super().__init__(brand, model, battery_life)
        self.camera_resolution = camera_resolution
    
    def take_photo(self):
        print(f"Taking a photo with {self.camera_resolution} MP camera on {self.model}...")

# Create a Smartphone object
phone1 = Smartphone("Apple", "iPhone 14", 85)
phone1.call("123-456-7890")
phone1.charge()

# Create a SmartphoneWithCamera object
phone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 75, 108)
phone2.call("987-654-3210")
phone2.charge()
phone2.take_photo()

"""Code for Activity 2: Polymorphism with Vehicles"""
# Base class
class Vehicle:
    def move(self):
        pass  # This method will be overridden by subclasses

# Derived class for Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived class for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create objects of Car and Plane
vehicle1 = Car()
vehicle2 = Plane()

# Call the move() method for both objects
vehicle1.move()  # Output: Driving 🚗
vehicle2.move()  # Output: Flying ✈️
