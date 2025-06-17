import basisklassen

class BaseCar:

    def __init__(self):
        self.__steering_angle = 0
        self.__speed = 0
        self.__direction = 0
        print("BaseCar erzeugt")
        
    @property
    def getAngle(self):
        print(self.__steering_angle)
        return self.__steering_angle
    def setAngle(self, angle):
        if angle < 45:
            self.__steering_angle = 45
        elif angle > 135:
            self.__steering_angle = 135
        else:
            self.__steering_angle = angle 

    @property
    def getSpeed(self):
        print(self.__speed)
        return self.__speed
    def setSpeed(self, speed):
        if speed < -100:
            self.__speed = -100
        elif speed > 100:
            self.__speed = 100
        else:
            self.__speed = speed


    @property
    def getDirection(self):
        print(self.__direction)
        return self.__direction

    def drive(self, speed, angle):
        pass

    def stop(self):
        self.setSpeed(0)

    def log_speed():
        pass

    def read_config(path):
        pass
    
car = BaseCar()
car.setAngle(150)
car.getAngle
car.setSpeed(-130)
car.getSpeed
car.setSpeed(80)
car.getSpeed

#Auto wird gestoppt
car.stop()# from basisklassen import Ultrasonic, BackWheels, FrontWheels

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