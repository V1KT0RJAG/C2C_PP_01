def fahrmodus1(car):
    car.drive(speed=30, angle=90)
    time.sleep(4)
    car.drive(speed=0)
    time.sleep(0.2)
    car.drive(speed=-30)
    time.sleep(4)
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

def fahrmodus3(car):
    pass