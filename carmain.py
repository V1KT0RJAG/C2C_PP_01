from basecar import BaseCar
from SonicCar import SonicCar
from Fahrmodus import *
from basisklassen import *
import time

fw=FrontWheels()
bw=BackWheels()
us=Ultrasonic()

cars=BaseCar(fw, bw)
