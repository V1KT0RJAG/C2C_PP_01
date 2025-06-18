from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time


fw = FrontWheels
bw = BackWheels

car = BaseCar(fw, bw)

car.drive()