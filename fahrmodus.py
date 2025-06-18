from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time

def fahrmodus_1(car):
   print("Fahrmodus 1: Vorwärts und Rückwärts")
   car.drive(speed=30, steering_angle=90)  # Geradeaus, langsam
   time.sleep(3)
   car.stop()
   time.sleep(1)
   car.drive(speed=-30)  # Rückwärts, langsam
   time.sleep(3)
   car.stop()

def fahrmodus_2(car):
   print("Fahrmodus 2: Kreisfahrt")
   # Geradeaus
   car.drive(speed=40, steering_angle=90)
   time.sleep(1)

   # Kreisfahrt im Uhrzeigersinn (maximaler Lenkwinkel rechts)
   car.drive(steering_angle=45)
   time.sleep(8)

   # Stopp
   car.stop()
   time.sleep(1)

   # Rückfahrt: Kreisfahrt gegen den Uhrzeigersinn (maximaler Lenkwinkel links)
   car.drive(speed=-40, steering_angle=135)
   time.sleep(8)

   # Geradeaus rückwärts
   car.drive(steering_angle=90)
   time.sleep(1)

   car.stop()

if __name__ == "__main__":
   car = BaseCar()
   fahrmodus_1(car)
   time.sleep(2)
   fahrmodus_2(car)