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

    def fahrmodus_4(self, duration=15, distance_min=25): # duration war = 30
        #Erkundungstour mit Hindernisvermeidung.
        print("Fahrmodus 4: Erkundungstour")
        start_time = time.time()
        self.car.drive(new_speed=40, new_angle=90)
        #Logfile 1
        self.car.log()

        while time.time() - start_time < duration:
            distance = self.car.get_distance()
            if distance is not 0 and distance < distance_min:
                print("Hindernis erkannt – Ausweichmanöver")
                self.car.stop()
                self.car.drive(new_speed=-30, new_angle=random.choice([45, 135]))
                time.sleep(3)
                #Logfile 2
                self.car.log()
                
                self.car.drive(new_speed=40, new_angle=90)

        self.car.stop()
        print("Erkundungstour beendet.")

  
    def fahrmodus_5(self, duration=20, distance_min=25):
        #Linie mit Hindernisvermeidung.

        print("Fahrmodus 5: Linie")
        start_time = time.time()
        
        self.car.drive(new_speed=30, new_angle=90)
        self.car.counter = 0
        #Logfile 1
        #self.car.log()

        while True:
        # Prüfe, ob 20 Sekunden vergangen sind
            if time.time() - start_time > duration:
                print("Zeitlimit erreicht – Fahrzeug gestoppt.")
                self.car.stop()
                break
            self.car.get_ir()
            #distance = self.car.get_distance()
            #self.car.log()
            #if distance is not 0 and distance < distance_min:
             #   print("Hindernis erkannt – Ausweichmanöver")
              #  self.car.stop()
               # self.car.drive(new_speed=-30, new_angle=random.choice([45, 135]))
                #time.sleep(3)
                #Logfile 2

                #self.car.drive(new_speed=40, new_angle=90)

            if sum(self.car.digital) == 0:
                self.car.counter += 1
                time.sleep(0.1)
        
                if self.car.counter > 50:
                # Wenn alle Sensoren 0 melden, ist die Linie verloren
                    print("Linie verloren – Fahrzeug gestoppt.")
                    self.car.stop()
                    break
                continue
        #time.sleep(1.5)

     #[1,0,0,0,0]
            if self.car.digital[0] == 1:
                self.car.drive(new_speed=40, new_angle=55)


    #[1,1,0,0,0]
            elif self.car.digital[0] == 1 and self.car.digital[1] == 1:
                self.car.drive(new_speed=40, new_angle=65)


    #[0,1,0,0,0]
            elif self.car.digital[1] == 1:
                self.car.drive(new_speed=40, new_angle=75)


    #[0,1,1,0,0]
            elif self.car.digital[1] == 1 and self.car.digital[2] ==1:
                self.car.drive(new_speed=40, new_angle=80)


    #[0,0,1,0,0] 
            elif self.car.digital[2] == 1:
                self.car.drive(new_speed=40, new_angle=90)


    #[0,0,1,1,0]
            elif self.car.digital[2] == 1 and self.car.digital[3] ==1:
                self.car.drive(new_speed=40, new_angle=100)


    #[0,0,0,1,0]
            elif self.car.digital[3] == 1:
                self.car.drive(new_speed=40, new_angle=110)


    #[0,0,0,1,1]
            elif self.car.digital[3] == 1 and self.car.digital[4] == 1:
                self.car.drive(new_speed=40, new_angle=120)


    #[0,0,0,0,1]
            elif self.car.digital[4] == 1:
                self.car.drive(new_speed=40, new_angle=130)

    
    #time.sleep(0.6)  # Kurze Pause für stabile Steuerung """
        self.car.stop()
