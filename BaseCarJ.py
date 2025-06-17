from basisklassen import FrontWheels, BackWheels
import json
import time

class BaseCar():
    
    def __init__(self):
        self._speed = 0
        self._angle = 90
        self.fw = FrontWheels()
        self.bw = BackWheels()
        self.offsetting()
        
    def offsetting(path):
            with open("config.json", "r") as f:
                data = json.load(f)
                turning_offset = data["turning_offset"]
                forward_A = data["forward_A"]
                forward_B = data["forward_B"]
                fw = FrontWheels(turning_offset=turning_offset)
                bw = BackWheels(forward_A=forward_A, forward_B=forward_B)
    
    def drive(self, speed, angle):
        pass
    def stop(self):
        self._speed = 0
        
    @property
    def speed(self):
        return self.speed
    
    @speed.setter
    def speed(self, Geschwindigkeit):
        if Geschwindigkeit < -100
            speed = -100
        elif Geschwindigkeit > 100
            speed = 100
        else:
            Geschwindigkeit = speed
    
    @property
    def steering_angle(self)
        return self.steering_angle
    
    @steering_angle.setter(self, angle)
        if angle > 135:
            steering_angle = 135
        elif angle < 45:
            steering_angle = 45
        else:
            angle = steering_angle
        
        if angle == fw.get_angles
            print(f"Lenkwinkel von {angle} wurde eingestellt")