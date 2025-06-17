from basisklassen import BackWheels, FrontWheels
import json
import time

class BaseCar:
    """Erzeugen Klasse Basecar mit Lenkung, Geschwindigkeit und Fahrtrichtung."""

    def __init__(self):        
        self.__steering_angle = 0   # Lenkwinkel in Grad
        self.__speed = 0            # Geschwindigkeit in km/h
        self.__direction = 0       # Fahrtrichtung in Grad
        self.config_offset
        print(f"Turning Offset{self.config_offset}")
        print("BaseCar erzeugt")
        
    @property
    def getAngle(self):
        """Gibt den aktuellen Lenkwinkel zurück."""
        print (self.__steering_angle)
        return self.__steering_angle

    def setAngle(self, angle):
        """Setzt den Lenkwinkel.
        Er muss zwischen 45 und 135 Grad liegen.
        """
        if angle < 45:
            self.__steering_angle = 45
        elif angle > 135:
            self.__steering_angle = 135
        else:
            self.__steering_angle = angle 


    @property
    def getSpeed(self):
        """Gibt die aktuelle Geschwindigkeit zurück."""
        return self.__speed
    
    def setSpeed(self, speed):
        """Setzt die neue Geschwindigkeit.
        Sie muss zwischen -100 und +100 liegen.
        """
        if speed < -100:
            self.__speed = -100
        elif speed > 100:
            self.__speed = 100
        else:
            self.__speed = speed


    @property
    def getDirection(self):
        """Gibt die aktuell eingestellte Fahrtrichtung zurück."""
        return self.__direction

    def drive(self, speed, angle):
        """Startet die Fahrt mit einer bestimmten Geschwindigkeit und einem Lenkwinkel."""
        self.setSpeed(speed)
        self.setAngle(angle)
        print(f"Das Auto fährt mit {self.__speed} km/h in Richtung {self.__direction} mit Lenkwinkel {self.__steering_angle}")

    def stop(self):
        """Bringt das Auto zum Stehen, indem die Geschwindigkeit auf 0 km/h ausgelegt wird."""
        self.setSpeed(0)
        print("Das Auto hat gestoppt")

    def log_speed(self):
        """Gibt die aktuell eingestellte Geschwindigkeit aus."""
        print(f"Aktuelle Geschwindigkeit: {self.__speed}")

    @property
    def config_offset(self):
        """Liest die Config.json"""
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




# Erstellen einer Auto-Instanz
car = BaseCar()

# Lenkwinkel ändern
car.setAngle(150)
print(car.getAngle)

# Geschwindigkeit ändern
car.setSpeed(-130)
print(car.getSpeed)
car.setSpeed(80)
print(car.getSpeed)

# Auto stoppen
car.stop()