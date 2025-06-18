from basisklassen import FrontWheels, BackWheels
import time
import json

class BaseCar:

    def __init__(self, front, back):
        self.__steering_angle = 90
        self.__speed = 0
        self.__direction = 0
        self.front = front
        self.back = back
        self.read_config()
        print("BaseCar erzeugt")
        
    @property
    def steering_angle(self):
        #print(self.__steering_angle)
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
        #print(self.__speed)
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
        #print(self.__direction)
        return self.__direction

    def drive(self, new_speed=None, new_angle=None):
        if new_speed is None:
            self.speed = self.speed
        else:
            self.speed = new_speed
        if new_angle is None:
            self.steering_angle= self.steering_angle
        else:
            self.steering_angle = new_angle

        print(f"Geschwindigkeit von {self.speed} und Lenkwinkel von {self.steering_angle} wurde übermittelt")
        time.sleep(1)

        if self.speed >= 0:
            self.back.forward()
            self.back.left_wheel.speed = self.speed
            self.back.right_wheel.speed = self.speed
        elif self.speed < 0:
            self.back.backward()              
            self.back.left_wheel.speed = abs(self.speed)
            self.back.right_wheel.speed = abs(self.speed)

        off = self.front._turning_offset 
        self.steering_angle = self.steering_angle + off

        self.front.turn(self.steering_angle)
        print(self.steering_angle)
        print(type(self.steering_angle))

    def stop(self):
        self.speed = 0
        self.back.left_wheel.speed = self.speed
        self.back.right_wheel.speed = self.speed

    def read_config(self):
        try:
            with open("config.json", "r") as f:
                data = json.load(f)

        except:
            print("Keine geeignete Datei config.json gefunden!")
            self.stop()
        else:
            #dictionary
            turning_offset = data.get("turning_offset")
            forward_A = data["forward_A"]
            forward_B = data["forward_B"]
            print("Daten in config.json:")
            print(" - Turning Offset: ", turning_offset)
            print(" - Forward A: ", forward_A)
            print(" - Forward B: ", forward_B)
            self.front._turning_offset = turning_offset
            self.back.forward_A= forward_A
            self.back.forward_B=forward_B
        finally:
            pass

""" 
fw = FrontWheels()
bw = BackWheels()
car = BaseCar(fw, bw)
 """

""" fw = basisklassen.FrontWheels()
bw = basisklassen.BackWheels() 

car = BaseCar(fw, bw)
car.steering_angle = 140
car.steering_angle
car.speed =-130
car.speed
car.speed = 80
car.speed
 """
#Auto wird gestopptAdd commentMore actions
#car.stop()# from basisklassen import Ultrasonic, BackWheels, FrontWheels