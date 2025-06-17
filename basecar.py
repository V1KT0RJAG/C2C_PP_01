# from basisklassen import Ultrasonic, BackWheels, FrontWheels

# class Car(BackWheels, FrontWheels, Ultrasonic):

# #     def _init_(self, forward_A= 0, forward_B= 0):
# #         super(). __init__(forward_A, forward_B)
        
class Car:
    def __init__(self, speed):
        self._speed = speed  # "protected" atribute"        
        
class BaseCar():
    def __init__(self, speed):
        self._speed = speed
        
        @property
        def speed(self):
            """Getter: returns speed"""
            return self._speed
        
        @speed.setter
        def speed(self, new_speed):
            if new_speed < 0:
                print("The speed cannot be negative")
            else:
                self._speed = new_speed
                

auto = Car(100)

print(f"Initial speed: {auto.speed} km/h")

auto.speed = 120

print(f"Updated speed: {auto.speed} km/h")

auto.speed = -50
print(f"Updated speed invalid: {auto.speed} km/h")