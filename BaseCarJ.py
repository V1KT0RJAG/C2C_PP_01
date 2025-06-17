from basisklassen import FrontWheels, BackWheels
import json
import time

class BaseCar:

    def __init__(self):
        self.__steering_angle = 0
        self.__speed = 0
        self.__direction = 0
        self.Config_offsett
        self.FW = FrontWheels()
        self.BW = BackWheels()
        print("BaseCar erzeugt")
        
        """
Getter und Setter haben den gleichen namen wie in der init methode
als erstes muss property erstellt werden und dann den setter

@property
def steering_angle(self)
    pass
    
@steering_angle.setter
def steering_angle(self, angle)
    pass

       
        """
        
    @property
    def getAngle(self):
        # print(self.__steering_angle)
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
        # print(self.__speed)
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
        if self.__speed == 0:
            print("Das Fahrzeug steht")
        elif self.__speed < 0:
            print("Das Fahrzeug fährt Rückwärts")
        elif self.__speed > 0:
            print("Das Fahrzeug fährt Vorwärts")  
        return self.__direction

    def drive(self, speed, angle):
        self.setSpeed(speed)
        self.setAngle(angle)
        if self.getSpeed == speed and self.getAngle == angle:
            print(f"Geschwindigkeit von {speed} und Lenkwinkel von {angle} wurde übermittelt")
            time.sleep(1) # startet erst nach 1 Sek
            self.FW.turn(self.getAngle)
            # print(self.getAngle)
            # print(type(self.getAngle))
            if self.getSpeed >= 0:
                self.BW.forward()
                self.BW.left_wheel.speed = self.getSpeed
                self.BW.right_wheel.speed = self.getSpeed
            elif self.getSpeed < 0:
                self.BW.backward()               
                self.BW.left_wheel.speed = abs(self.getSpeed)
                self.BW.right_wheel.speed = abs(self.getSpeed)
                
        else:
            print("Fahrdaten konnten nicht übermittelt werden")
        

    def stop(self):
        self.setSpeed(0)
        print("Das Fahrzeug hält an !")

    def log_speed():
        pass

    @property    
    def Config_offsett(self):
        with open("config.json", "r") as f:
            data = json.load(f)
            turning_offset = data["turning_offset"]
            forward_A = data["forward_A"]
            forward_B = data["forward_B"]
            print("Daten in config.json:")
            print(" - Turning Offset: ", turning_offset)
            print(" - Forward A: ", forward_A)
            print(" - Forward B: ", forward_B)
            FrontWheels(turning_offset=turning_offset)
            BackWheels(forward_A=forward_A, forward_B=forward_B)

"""
Das ist ein besserer Import von den Sachen
oben in __init__ self.fw (bw löschen)
und dann in der py.datei von dem realen auto so die instanz erstellen:
fw = FrontWheels()
bw = BackWheels()
 """           
# car = BaseCar()

# car.drive(50, 90)
# time.sleep(0.5)
# car.drive(0, 90)
# time.sleep(0.5)
# car.drive(-50, 90)
# car.stop()