from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
from fahrmodus import Fahrmodus
import time


fw = FrontWheels()
bw = BackWheels() 

car = BaseCar(fw, bw)

modus = Fahrmodus(car)
#modus.fahrmodus_1()
modus.fahrmodus_2()


""" print("Fahrmodus 1: Vorwärts und Rückwärts")
car.drive(30, 90)  # Geradeaus, langsam
time.sleep(3)
car.stop()
time.sleep(1)
car.drive(-30)  # Rückwärts, langsam
time.sleep(3)
car.stop()
#car.drive(50, new_angle=90)
print(fw._turning_offset)

print("Fahrmodus 2: Kreisfahrt")
# Geradeaus
car.drive(40, 90)
time.sleep(1)

# Kreisfahrt im Uhrzeigersinn (maximaler Lenkwinkel rechts)
car.drive(new_angle =45)
time.sleep(8)

# Stopp
car.stop()
time.sleep(1)

# Rückfahrt: Kreisfahrt gegen den Uhrzeigersinn (maximaler Lenkwinkel links)
car.drive(new_speed=-40, new_angle=135)
time.sleep(8)

# Geradeaus rückwärts
car.drive(new_angle=90)
time.sleep(1)

car.stop() """