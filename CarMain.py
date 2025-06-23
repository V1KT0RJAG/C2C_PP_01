from BaseCar_Main import BaseCar
from SonicCar import SonicCar
from Fahrmodus import *
from basisklassen import *
import time


fw = FrontWheels
bw = BackWheels
us = Ultrasonic()

carb = BaseCar(fw, bw)
cars = SonicCar(fw, bw, us)

fahrmodus4(cars)
