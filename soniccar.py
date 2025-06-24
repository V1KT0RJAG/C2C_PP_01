from basecar import BaseCar
from basisklassen import Ultrasonic, FrontWheels, BackWheels
import time

#SonicCar Klasse
class SonicCar(BaseCar):
    def __init__(self, front, back, ultra):
        super().__init__(front, back)
        self.ultra = ultra
        self.log = []
        #self.fahrmodi = fahrmodi
        print("SonicCar erzeugt")
        #print(self.ultra)

    def get_distance(self, retries=3, delay=0.2):
        """
        Führt eine robuste Distanzmessung durch.
        Wiederholt die Messung bei Fehlern bis zu 'retries'-mal.
        """
        for attempt in range(retries):
            distance = self.ultra.distance()
            if distance >= 0:
                print('Sonic Car: distance measurement')
                print(self.ultra.distance())
                return distance
            else:
                print(f"[Warnung] Sensorfehler (Code {distance}) – Versuch {attempt + 1} von {retries}")
                time.sleep(delay)

        print("[Fehler] Keine gültige Distanzmessung möglich.") 
        #self.stop()  
        return 0
    
    def log_status(self):
        """Speichert den aktuellen Fahrzeugstatus und Sensorwert."""
        distance = self.get_distance()
        self.log.append({
            "timestamp": time.time(),
            "speed": self.speed,
            "steering_angle": self.steering_angle,
            "direction": self.direction,
            "distance": distance
        })
        """Gibt das Fahrprotokoll zurück."""
        return self.log


if __name__ == "__main__":
    #test 
    fw = FrontWheels()
    bw = BackWheels() 
    usm = Ultrasonic()

    sc = SonicCar(fw, bw, usm)
    sc.get_distance()