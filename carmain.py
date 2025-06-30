from basisklassen import FrontWheels, BackWheels, Ultrasonic
from basecar import BaseCar
from fahrmodus import Fahrmodus
from soniccar import SonicCar
import time
#import plotly.express as px


import pandas as pd 
from pandas import Series, DataFrame 
import numpy as np


fw = FrontWheels()
bw = BackWheels() 
usm = Ultrasonic()

""" car = BaseCar(fw, bw)

modus = Fahrmodus(car)
#modus.fahrmodus_1()
modus.fahrmodus_2() """

sc = SonicCar(fw, bw, ultra=usm)
modus = Fahrmodus(sensor_c)

modus.fahrmodus_7() 
#modus.fahrmodus_3(stop_distance=20)
#modus.fahrmodus_4(duration=45)

#for eintrag in sc.log_status():
    #readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(eintrag["timestamp"]))
    #print(eintrag)#f"Zeit: {readable_time}, Geschwindigkeit: {eintrag['speed']}")

#print(sc.log_status())
log_df = DataFrame(sc.data)

# initial_fig = px.line(log_df, x="timestamp", y="speed")

# initial_fig.show()

log_df.to_csv("sonic_log.csv", index = False)







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


    
