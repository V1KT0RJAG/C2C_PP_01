import basisklassen
import time
import json
from basisklassen import FrontWheels, BackWheels


class BaseCar:

    def __init__(self, front, back):
        self.__steering_angle = 90
        self.__speed = 0
        self.__direction = 0
        self.front = front
        self.back = back
        self.offset_config()
        print("BaseCar erzeugt")
        
    @property
    def steering_angle(self):
        # print(self.__steering_angle)
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
        # print(self.__speed)
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

    def drive(self, **kwargs):
        # Falls "speed" übergeben wurde, aktualisieren – sonst alten Wert behalten
        if "speed" in kwargs:
            self.speed = kwargs.get("speed", self.speed)

        # Falls "angle" übergeben wurde, aktualisieren – sonst alten Wert behalten
        if "angle" in kwargs:
            self.steering_angle = kwargs.get("angle", self.steering_angle)

        print(f"Geschwindigkeit von {self.speed} und Lenkwinkel von {self.steering_angle} wurde übermittelt")
        time.sleep(1)
        # print(self.steering_angle)
        # print(type(self.steering_angle))
        self.front.turn(self.steering_angle)
     
        if self.speed >= 0:
            self.back.forward()
            self.back.left_wheel.speed = self.speed
            self.back.right_wheel.speed = self.speed
        elif self.speed < 0:
            self.back.backward()              
            self.back.left_wheel.speed = abs(self.speed)
            self.back.right_wheel.speed = abs(self.speed)
         



    def stop(self):
        self.speed = 0
        self.back.left_wheel.speed = self.speed
        self.back.right_wheel.speed = self.speed

    def offset_config(self):
        try:
            with open("config.json", "r") as f:
                data = json.load(f)
                turning_offset = data.get("turning_offset", 0)
                forward_A = data.get("forward_A", 0)
                forward_B = data.get("forward_B", 0)
                print("Daten in config.json:")
                print(" - Turning Offset: ", turning_offset)
                print(" - Forward A: ", forward_A)
                print(" - Forward B: ", forward_B)
        except:
            print("Keine geeignete Datei config.json gefunden!")
            self.stop()
        else:
            print("Offset wurde geschrieben")
            self.front = self.front(turning_offset=turning_offset)
            self.back = self.back(forward_A=forward_A, forward_B=forward_B)
        finally:
            pass


#           so würde es auch gehen nur dann müsste man bei der erstellung nur fw = FrontWheels schreiben ohne () weil erst in dem Code die "Räder" angebaut werden           
#            FrontWheels(turning_offset=turning_offset) 
#            BackWheeels(forward_A=forward_A, forward_B=forward_B)

"""

            print("Offset wurde geschrieben")
            self.front._turning_offset = turning_offset
            self.back.forward_A = forward_A
            self.back.forward_B = forward_B
            
"""


 
    
