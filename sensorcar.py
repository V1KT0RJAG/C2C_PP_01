from basecar import BaseCar
from basisklassen import Ultrasonic, FrontWheels, BackWheels, Infrared
from fahrmodus import Fahrmodus
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3c70140 (update v2)
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
=======
        data_analog = self.infra.read_analog() 
        data_digital = self.infra.read_digital()
        print(data_analog, data_digital)
>>>>>>> f816594 (1st ver not working)

fw = FrontWheels()
bw = BackWheels() 
usm = Ultrasonic()
ir = Infrared()
sc = SensorCar(fw, bw, ultra=usm, infra=ir)

<<<<<<< HEAD

<<<<<<< HEAD
fm = Fahrmodus(sc)

#sc.get_distance()
sc.get_ir()
fm.fahrmodus_5()

""""
print("Fahrmodus 5:")
start_time = time.time()
sc.drive(new_speed=25, new_angle=90)
counter = 0

while True:
    # Prüfe, ob 20 Sekunden vergangen sind
    if time.time() - start_time > 20:
        print("Zeitlimit erreicht – Fahrzeug gestoppt.")
        sc.stop()
        break
    sc.get_ir()
    #sc.stop()

    if sum(sc.digital) == 0:
        counter += 1
        time.sleep(0.1)
        
        if counter > 50:
            # Wenn alle Sensoren 0 melden, ist die Linie verloren
            print("Linie verloren – Fahrzeug gestoppt.")
            sc.stop()
            break
        continue
        #time.sleep(1.5)

    if sc.digital[0] == 1:
        sc.drive(new_speed=40, new_angle=55)


    #[1,1,0,0,0]
    elif sc.digital[0] == 1 and sc.digital[1] == 1:
        sc.drive(new_speed=40, new_angle=65)


    #[0,1,0,0,0]
    elif sc.digital[1] == 1:
        sc.drive(new_speed=40, new_angle=75)


    #[0,1,1,0,0]
    elif sc.digital[1] == 1 and sc.digital[2] ==1:
        sc.drive(new_speed=40, new_angle=80)


    #[0,0,1,0,0] 
    elif sc.digital[2] == 1:
        sc.drive(new_speed=40, new_angle=90)


    #[0,0,1,1,0]
    elif sc.digital[2] == 1 and sc.digital[3] ==1:
        sc.drive(new_speed=40, new_angle=100)


    #[0,0,0,1,0]
    elif sc.digital[3] == 1:
        sc.drive(new_speed=40, new_angle=110)


    #[0,0,0,1,1]
    elif sc.digital[3] == 1 and sc.digital[4] == 1:
        sc.drive(new_speed=40, new_angle=120)


    #[0,0,0,0,1]
    elif sc.digital[4] == 1:
        sc.drive(new_speed=40, new_angle=130)

    
    #time.sleep(0.6)  # Kurze Pause für stabile Steuerung 

sc.drive(new_speed=0, new_angle=90)
sc.stop()"""
=======
analog = ir.read_analog()
digital = ir.read_digital()
print(f"Analog: {analog} | Digital: {digital}")
=======
# #ir.test()
sc.get_ir()

# analog = ir.read_analog()
# digital = ir.read_digital()
# print(f"Analog: {analog} | Digital: {digital}")
>>>>>>> 3c70140 (update v2)
ir.cali_references()
ir.set_references
time.sleep(5)

# #fahrmodus 5
# #linie vefolgen
print("Fahrmodus 5:")
start_time = time.time()
sc.drive(new_speed=20, new_angle=90)
counter = 0

<<<<<<< HEAD
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
>>>>>>> f816594 (1st ver not working)
=======
while True:
    # Prüfe, ob 20 Sekunden vergangen sind
    if time.time() - start_time > 20:
        print("Zeitlimit erreicht – Fahrzeug gestoppt.")
        sc.stop()
        break
    sc.get_ir()

    if sum(sc.digital) == 0:
        counter += 1
        time.sleep(1.5)

    if counter > 5:
        # Wenn alle Sensoren 0 melden, ist die Linie verloren
        print("Linie verloren – Fahrzeug gestoppt.")
        sc.stop()
        break

    if sc.digital == [0, 0, 1, 0, 0]:
        sc.drive(new_angle=90)  # Geradeaus
    elif sc.digital [0] == 1 or sc.digital [1] == 1:
        sc.drive(new_angle=55)  # Nach links lenken
    elif sc.digital [3] == 1 or sc.digital [4] == 1:
        sc.drive(new_angle=125) # Nach rechts lenken   
    else:
        sc.drive(new_angle=90)  # Standard: geradeaus
    time.sleep(0.1)  # Kurze Pause für stabile Steuerung
"""     #[1,0,0,0,0]
    elif sc.digital[0] == 1:
        sc.drive(new_speed=20, new_angle=45)

    #[1,1,0,0,0]
    elif sc.digital[0] == 1 and sc.digital[1] == 1:
        sc.drive(new_speed=20, new_angle=60)

    #[0,1,0,0,0]
    elif sc.digital[1] == 1:
        sc.drive(new_speed=20, new_angle=75)

    #[0,1,1,0,0]
    elif sc.digital[1] == 1 and sc.digital[2] ==1:
        sc.drive(new_speed=20, new_angle=80)

    #[0,0,1,0,0] 
    elif sc.digital[2] == 1:
        sc.drive(new_speed=20, new_angle=90)

    #[0,0,1,1,0]
    elif sc.digital[2] == 1 and sc.digital[3] ==1:
        sc.drive(new_speed=20, new_angle=95)

    #[0,0,0,1,0]
    elif sc.digital[3] == 1:
        sc.drive(new_speed=20, new_angle=120)

    #[0,0,0,1,1]
    elif sc.digital[3] == 1 and sc.digital[4] == 1:
        sc.drive(new_speed=20, new_angle=125)

    #[0,0,0,0,1]
    elif sc.digital[4] == 1:
        sc.drive(new_speed=20, new_angle=135)
    
    time.sleep(0.1)  # Kurze Pause für stabile Steuerung """

sc.drive(new_speed=0, new_angle=90)
sc.stop()
>>>>>>> 3c70140 (update v2)
