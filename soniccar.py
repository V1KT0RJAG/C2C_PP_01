from basecar import BaseCar
from basisklassen import Ultrasonic, FrontWheels, BackWheels
from datetime import datetime
import json
import os
import csv
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
    
    def logging_data(self):
        timestamp_data = datetime.now().strftime('%Y-%m-%d') #Zeitstempel für den Dateinamen
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #Zeitstempel für die Messung
        
        
        if os.path.exists(f"Loggdata_{timestamp_data}.csv"):
            with open(f"Loggdata_{timestamp_data}.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, self.speed, self.steering_angle, self.ultra.distance()])

        else:
            with open(f"Loggdata_{timestamp_data}.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Speed", "Lenkwinkel","Ultraschallsensor"])
                writer.writerow([timestamp, self.speed, self.steering_angle, self.ultra.distance()])

if __name__ == "__main__":
    #test 
    fw = FrontWheels()
    bw = BackWheels() 
    usm = Ultrasonic()

    sc = SonicCar(fw, bw, usm)
    sc.logging_data()