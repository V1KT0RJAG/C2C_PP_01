import time
import logging
import random

logging.basicConfig(
    filename='fahrdaten_log.txt',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)

def fahrmodus1(car):
    car.drive(speed=30, angle=90)
    time.sleep(3)
    car.drive(speed=0)
    time.sleep(0.2)
    car.drive(speed=-30)
    time.sleep(3)
    car.stop()
    
def fahrmodus2(car):
    car.drive(speed=30, angle=90)
    time.sleep(1)
    car.drive(speed=30, angle=135)
    time.sleep(8)
    car.stop()
    time.sleep(0.2)
    car.drive(speed=30, angle=45)
    time.sleep(8)
    car.drive(speed=-30, angle=90)
    time.sleep(1) 
    car.stop()
    
    
def fahrmodus3(car, set_dis):
    while True:
        akt_dis = car.get_distance()
        car.drive(speed=30, angle=90)
        time.sleep(0.2)
        # logging.info(f"Auto gestartet:" {speed}"Speed und mit einem Lenkwinkel von" {angle})
        # print(type(akt_dis))

        if not isinstance(akt_dis, (int, float)) or akt_dis <= 0:
            print("Ungültige Messung:", akt_dis)
            time.sleep(0.2)
            continue

        if akt_dis < set_dis:
            car.drive(speed=0)
            # print(f"Hindernis erkannt (Abstand: {akt_dis}. Auto wird gestoppt.")
            # logging.info(f"Hindernis erkannt Abstand:" {akt_dis}". Auto wird gestoppt.")
            break
            

def fahrmodus4(car):
    try:
        while True:
            akt_dis = car.get_distance()
            car.drive(speed=30, angle=90)
            # logging.info(f"Auto gestartet: {car.speed}  Speed und mit einem Lenkwinkel von {car.angle}")
            car.drive(angle=random.choice([35,90,60,110,135]))

            if not isinstance(akt_dis, (int, float)) or akt_dis <= 0:
                print("Ungültige Messung:", akt_dis)
                continue

            if akt_dis < 15:
                car.drive(speed=0)
                print("Hindernis erkannt (Abstand:", akt_dis, "). Auto dreht sich.")
                # logging.info(f"Hindernis erkannt Abstand: {akt_dis}. Auto wird gestoppt.")
                car.drive(speed=-30, angle=35)
                time.sleep(1)
                car.drive(speed=0, angle =90)
                continue 
        
    except KeyboardInterrupt:
        car.drive(speed=0, angle=90)
        
        
def get_akt_values(car):
    speed = car.speed
    angle = car.steering_angle
    dis =   car.get_distance

    
         
