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

