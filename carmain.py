<<<<<<< HEAD
""" from basecar import BaseCar
from SonicCar import SonicCar
from Fahrmodus import *
from basisklassen import *
import time

def main():
    fw = FrontWheels()
    bw = BackWheels()
    us = Ultrasonic()

    car = SonicCar(fw, bw, us)

if __name__ == "__main__":
    main() """

from soniccar import SonicCar
from basisklassen import FrontWheels, BackWheels, Ultrasonic
from fahrmodus import fahrmodus1, fahrmodus2, fahrmodus3

def main():
    fw = FrontWheels()
    bw = BackWheels()
    us = Ultrasonic()

    car = SonicCar(fw, bw, us)

    print("\nWähle Fahrmodus:")
    print("1 - Geradeaus & Rückwärts")
    print("2 - Kurvenfahrt")
    print("3 - Hinderniserkennung")
    
    auswahl = input("Modus (1/2/3): ").strip()
    
    if auswahl == "1":
        fahrmodus1(car)
    elif auswahl == "2":
        fahrmodus2(car)
    elif auswahl == "3":
        fahrmodus3(car)
    else:
        print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()
=======
from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time


fw = FrontWheels
bw = BackWheels

car = BaseCar(fw, bw)

car.drive()
>>>>>>> main
