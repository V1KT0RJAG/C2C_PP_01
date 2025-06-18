import basisklassen
import time
import json

class BaseCar:

    def __init__(self, front, back):
        self.__steering_angle = 0
        self.__speed = 0
        self.__direction = 0
        self.front = front
        self.back = back
        print("BaseCar erzeugt")
        
    @property
    def steering_angle(self):
        print(self.__steering_angle)
        return self.__steering_angle
    @steering_angle.setter
    def steering_angle(self, angle):
        if angle < 45:
            self.__steering_angle = 45
        elif angle > 135:
            self.__steering_angle = 135
        else:
            self.__steering_angle = angle 

    @property
    def speed(self):
        print(self.__speed)
        return self.__speed
    @speed.setter
    def speed(self, new_speed):
        if new_speed < -100:
            self.__speed = -100
        elif new_speed > 100:
            self.__speed = 100
        else:
            self.__speed = new_speed

    @property
    def direction(self):
        print(self.__direction)
        return self.__direction

    def drive(self, new_speed, new_angle):
        self.speed = new_speed
        self.steering_angle = new_angle
        print(f"Geschwindigkeit von {self.speed} und Lenkwinkel von {self.steering_angle} wurde übermittelt")
        time.sleep(1)

        fw.turn(new_angle)
        print(new_angle)
        print(type(new_angle))

    def stop(self):
        self.speed = 0

    def read_config(self, path):
        try:
            with open("config.json", "r") as f:
                data = json.load(f)
                turning_offset = data["turning_offset"]
                forward_A = data["forward_A"]
                forward_B = data["forward_B"]
                print("Daten in config.json:")
                print(" - Turning Offset: ", turning_offset)
                print(" - Forward A: ", forward_A)
                print(" - Forward B: ", forward_B)
        except:
            print("Keine geeignete Datei config.json gefunden!")
        else:
            print("Test der Vorderräder:")
            x = input(' Drücken Sie ENTER zum Start.')
            self.front(turning_offset=turning_offset)
            self.front.test()
            time.sleep(1)
            print("Test der Hinterräder:")
            x = input(' ACHTUNG! Das Auto wird ein Stück fahren!\n Drücken Sie ENTER zum Start.')
            self.back(forward_A=forward_A, forward_B=forward_B)
            self.back.test()

fw = basisklassen.FrontWheels()
bw = basisklassen.BackWheels() 

car = BaseCar(fw, bw)
car.steering_angle = 140
car.steering_angle
car.speed =-130
car.speed
car.speed = 80
car.speed

#Auto wird gestopptAdd commentMore actions
car.stop()# from basisklassen import Ultrasonic, BackWheels, FrontWheels