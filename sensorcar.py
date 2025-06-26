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
    
    # def get_ir(self):
    #     data = self.infra.read_analog() 
    #     print(data)

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