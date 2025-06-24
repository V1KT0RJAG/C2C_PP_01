from basisklassen import FrontWheels, BackWheels, Ultrasonic
from basecar import BaseCar
from fahrmodus import Fahrmodus
from soniccar import SonicCar
import time


fw = FrontWheels()
bw = BackWheels() 
usm = Ultrasonic()

""" car = BaseCar(fw, bw)

modus = Fahrmodus(car)
#modus.fahrmodus_1()
modus.fahrmodus_2() """

sc = SonicCar(fw, bw, usm)
modus = Fahrmodus(sc)
#modus.fahrmodus_3(stop_distance=20)
modus.fahrmodus_4()





""" stop_distance=25
while sc.get_distance()>stop_distance:
    sc.drive(new_speed=40, new_angle=90)
    #bremsen Weg
    bw= stop_distance + 10
    if sc.get_distance()< bw:
        sc.drive(new_speed=5, new_angle=90)
        break
sc.log_status()
  
sc.stop()
#sc.drive(new_speed=0)
print("Hindernis erkannt – Fahrzeug gestoppt.")  """


    
