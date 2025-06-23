import time

def fahrmodus1(car):
    print("Starte Fahrmodus 1")
    car.drive(new_speed=30, new_angle=90)
    time.sleep(4)
    car.drive(new_speed=0)
    time.sleep(0.2)
    car.drive(new_speed=-30, new_angle=90)
    time.sleep(4)
    car.stop()

def fahrmodus2(car):
    print("Starte Fahrmodus 2")
    car.drive(new_speed=30, new_angle=90)
    time.sleep(1)
    car.drive(new_speed=30, new_angle=135)
    time.sleep(8)
    car.stop()
    time.sleep(0.2)
    car.drive(new_speed=-30, new_angle=45)
    time.sleep(8)
    car.drive(new_speed=-30, new_angle=90)
    time.sleep(1)
    car.stop()

def fahrmodus3(car, abstandsschwelle=20):
    print("Starte Fahrmodus 3 – Hinderniserkennung aktiv")
    car.drive(new_speed=30, new_angle=90)

    try:
        while True:
            distanz = car.get_distance()
            if distanz < abstandsschwelle:
                print(f"Hindernis erkannt bei {distanz} cm – Auto stoppt.")
                car.stop()
                break
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Abbruch durch Benutzer – Auto stoppt.")
        car.stop()