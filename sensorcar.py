from basecar import BaseCar
from basisklassen import Ultrasonic, FrontWheels, BackWheels, Infrared
import time
import json


class SensorCar(BaseCar):
    def __init__(self, front, back, ultra, infra, values_to_log=["get_distance", "get_ir"]):
        super().__init__(front, back, values_to_log)
        self.infra = infra
        self.ultra = ultra
        self.ir_config()
        self.analog=[]
        self.digital=[]
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
        self.analog = self.infra.read_analog() 
        self.digital = self.infra.read_digital()
        print(self.analog, self.digital)
        return self.analog, self.digital
        
   
    def ir_config(self):
        try:
            with open("config.json", "r") as ff:
                data = json.load(ff)

        except:
            print("Keine geeignete Datei config.json gefunden!")
            
        else:
            #dictionary
            ir_ref = data["ir_ref"]
            print("Daten in config.json:")
            print(" - IR_ref: ", ir_ref)

            self.infra.set_references(ir_ref)
            ff.close()
        finally:
            pass

fw = FrontWheels()
bw = BackWheels() 
usm = Ultrasonic()
ir = Infrared()
sc = SensorCar(fw, bw, ultra=usm, infra=ir)

# #ir.test()
sc.get_ir()

# analog = ir.read_analog()
# digital = ir.read_digital()
# print(f"Analog: {analog} | Digital: {digital}")
ir.cali_references()
ir.set_references
time.sleep(5)

# #fahrmodus 5
# #linie vefolgen
print("Fahrmodus 5:")
start_time = time.time()
sc.drive(new_speed=30, new_angle=90)


while True:
    # Prüfe, ob 20 Sekunden vergangen sind
    if time.time() - start_time > 20:
        print("Zeitlimit erreicht – Fahrzeug gestoppt.")
        sc.stop()
        break
    sc.get_ir()

    if sum(sc.digital) == 0:
        # Wenn alle Sensoren 0 melden, ist die Linie verloren
        print("Linie verloren – Fahrzeug gestoppt.")
        sc.stop()
        break
    #[1,0,0,0,0]
    elif sc.digital[0] == 1:
        sc.drive(new_speed=20, new_angle=45)

    #[1,1,0,0,0]
    elif sc.digital[0] == 1 and sc.digital[1] == 1:
        sc.drive(new_speed=20, new_angle=60)

    #[0,1,0,0,0]
    elif sc.digital[1] == 1:
        sc.drive(new_speed=20, new_angle=75)

    #[0,0,1,0,0] 
    elif sc.digital[2] == 1:
        sc.drive(new_speed=20, new_angle=90)

    #[0,1,1,0,0]
    elif sc.digital[1] == 1 and sc.digital[2] ==1:
        sc.drive(new_speed=20, new_angle=90)

    #[0,0,1,1,0]
    elif sc.digital[2] == 1 and sc.digital[3] ==1:
        sc.drive(new_speed=20, new_angle=90)

    #[0,0,0,1,0]
    elif sc.digital[3] == 1:
        sc.drive(new_speed=20, new_angle=120)

    #[0,0,0,1,1]
    elif sc.digital[3] == 1 and sc.digital[4] == 1:
        sc.drive(new_speed=20, new_angle=135)

    #[0,0,0,0,1]
    elif sc.digital[4] == 1:
        sc.drive(new_speed=20, new_angle=135)
    
    time.sleep(0.1)  # Kurze Pause für stabile Steuerung

sc.drive(new_speed=0, new_angle=90)
sc.stop()
