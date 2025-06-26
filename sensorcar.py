from basecar import BaseCar
from basisklassen import Ultrasonic, FrontWheels, BackWheels, Infrared
import time


class SensorCar(BaseCar):
    def __init__(self, front, back, ultra, infra, values_to_log=["get_distance", "get_ir"]):
        super().__init__(front, back, values_to_log)
        self.infra = infra
        self.ultra = ultra
        print("SensorCar erzeugt")
    
    def get_distance(self, retries=3, delay=0.2):
        """
        Führt eine robuste Distanzmessung durch.
        Wiederholt die Messung bei Fehlern bis zu 'retries'-mal.
        """
        for attempt in range(retries):
            distance = self.ultra.distance()
            if distance >= 0:
                print('Sonic Car: distance measurement')
                print(self.ultra.distance())
                return distance
            else:
                print(f"[Warnung] Sensorfehler (Code {distance}) – Versuch {attempt + 1} von {retries}")
                time.sleep(delay)

        print("[Fehler] Keine gültige Distanzmessung möglich.") 
        #self.stop()  
        return 0

    def get_ir(self):
        #Logik aufbauen
        data_analog = self.infra.read_analog() 
        data_digital = self.infra.read_digital()
        print(data_analog, data_digital)

fw = FrontWheels()
bw = BackWheels() 
usm = Ultrasonic()
ir = Infrared()
sc = SensorCar(fw, bw, ultra=usm, infra=ir)

#ir.test()
#sc.get_ir()

analog = ir.read_analog()
digital = ir.read_digital()
print(f"Analog: {analog} | Digital: {digital}")
ir.cali_references()
ir.set_references
time.sleep(5)

#fahrmodus 5
#linie vefolgen
print("Fahrmodus 5:")
start_time = time.time()
sc.drive(new_speed=40, new_angle=90)

drive_duration = 0

while drive_duration<20:
    #[1,0,0,0,0]
    if digital[0] == 1:
        sc.drive(new_speed=40, new_angle=45)
        print(digital)
        print(analog)
    #[0,1,0,0,0]
    if digital[1] == 1:
        sc.drive(new_speed=40, new_angle=60)
        print(digital)
        print(analog)
    #[0,0,1,0,0]
    if digital[2] == 1:
        sc.drive(new_speed=40, new_angle=90)
        print(digital)
        print(analog)
    #[0,0,0,1,0]
    if digital[3] == 1:
        sc.drive(new_speed=40, new_angle=120)
        print(digital)
        print(analog)
    #[0,0,0,0,1]
    if digital[4] == 1:
        sc.drive(new_speed=40, new_angle=135)
        print(digital)
        print(analog)
    #[0,0,0,0,0], [1,1,1,1,1], [1,1,0,0,0]
    else:
        sc.stop()
        print(digital)
        print(analog)
    drive_duration += 1

sc.stop()