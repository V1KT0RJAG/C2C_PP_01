from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time
import random

class Fahrmodus:

    def __init__(self,car):
        self.car = car

    def fahrmodus_1(self):
        print("Fahrmodus 1: Vorwärts und Rückwärts")
        self.car.drive(30,90)  # Geradeaus, langsam
        time.sleep(3)
        self.car.stop()
        time.sleep(1)
        self.car.drive(-30)  # Rückwärts, langsam
        time.sleep(3)
        self.car.stop()

    def fahrmodus_2(self):
        print("Fahrmodus 2: Kreisfahrt")
        # Geradeaus
        self.car.drive(40, 90)
        time.sleep(1)
        # Kreisfahrt im Uhrzeigersinn (maximaler Lenkwinkel rechts)
        self.car.drive(new_angle=45)
        time.sleep(8)
        # Stopp
        self.car.stop()
        time.sleep(1)
        # Rückfahrt: Kreisfahrt gegen den Uhrzeigersinn (maximaler Lenkwinkel links)
        self.car.drive(-40, 135)
        time.sleep(8)
        # Geradeaus rückwärts
        self.car.drive(new_angle=90)
        time.sleep(1)
        self.car.stop()

    def fahrmodus_3(self, stop_distance=20):
        """Fährt vorwärts, bis ein Hindernis erkannt wird."""
        print("Fahrmodus 3: Vorwärtsfahrt bis Hindernis")
        while self.car.get_distance()>stop_distance:
            self.car.drive(new_speed=40, new_angle=90)
        self.car.stop()
        print("Hindernis erkannt – Fahrzeug gestoppt.")

    def fahrmodus_4(self, duration=30):
        #Erkundungstour mit Hindernisvermeidung.
        print("Fahrmodus 4: Erkundungstour")
        start_time = time.time()
        self.car.drive(new_speed=40, new_angle=90)

        while time.time() - start_time < duration:
            distance = self.car.get_distance()
            if distance is not 0 and distance < 25:
                print("Hindernis erkannt – Ausweichmanöver")
                self.car.stop()
                self.car.drive(new_speed=-30, new_angle=random.choice([45, 135]))
                time.sleep(3)
                #self.car.log_status()
                
                self.car.drive(new_speed=40, new_angle=90)

        self.car.stop()
        print("Erkundungstour beendet.")

"""     def fahrmodus_4(self):
        try:
            while True:
                akt_dis = self.car.get_distance()
                self.car.drive(new_speed=40, new_angle=90)
                time.sleep(0.2)
                #logging.info(f"Auto gestartet:" {speed}"Speed und mit einem Lenkwinkel von" {angle})
                #self.car.drive(angle=random.choice([35,90, 60, 110, 135]))
    
                if not isinstance(akt_dis, (int, float)) or akt_dis <= 0:
                    print("Ungültige Messung:", akt_dis)
                    time.sleep(0.2)
                    continue
    
                if akt_dis < 15:
                    self.car.drive(new_speed=0)
                    print("Hindernis erkannt (Abstand:", akt_dis, "). Auto dreht sich.")
                    #logging.info(f"Hindernis erkannt Abstand:" {akt_dis}". Auto wird gestoppt.")
                    self.car.drive(new_speed=-30, new_angle=35)
                    time.sleep(1)
                    self.car.drive(new_speed=0, new_angle =90)
                    time.sleep(0.5)
                    continue
        
        except KeyboardInterrupt:
            self.car.drive(new_speed=0, new_angle=90) """


