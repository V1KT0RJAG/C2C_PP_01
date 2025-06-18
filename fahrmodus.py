from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time

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

