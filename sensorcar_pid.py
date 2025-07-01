from basecar import BaseCar
from basisklassen import Ultrasonic, FrontWheels, BackWheels, Infrared
import time
import json
import numpy as np


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

    def increase_references_by_20(self) -> None:
        if hasattr(self.infra, '_references') and self.infra._references is not None:
            increased = np.array(self.infra._references) + 10
            0
            #Sensorwert +20 vorgeben
            self.infra.set_references(increased.tolist())
            print('references erhöht:', self.infra._references)
        else:
        
            print('Zuerst cali_references() aufrufen.')


if __name__ == "__main__":
 

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
    sc.increase_references_by_20()
    ir.set_references
    print("Starte IR-Sensor-Test...")
    for i in range(10):
        analog, digital = sc.get_ir()
        print(f"Test {i+1}: Analog: {analog} | Digital: {digital}")
        time.sleep(0.5)
    time.sleep(5)

    # #fahrmodus 5
    # #linie vefolgen
    print("Fahrmodus 8:")
    start_time = time.time()
    sc.drive(new_speed=45, new_angle=90)

    counter = 0

    start_time = time.time()
    weights = [-2, -1, 0, 1, 2]  # Sensor-Gewichtung

     # PID-Parameter
    Kp = 15.0
    Ki = 1.0
    Kd = 8.0
                

    last_error = 0
    integral = 0

    while time.time() - start_time <= 15:
        sc.get_ir()
        
        if sum(sc.digital) == 0:
            print("Linie verloren – Rückwärtsfahren und Neuversuch.")
            sc.drive(new_speed=-30, new_angle=90)  # Rückwärts geradeaus
            time.sleep(1)  # 1 Sekunde rückwärts fahren
            sc.stop()
            time.sleep(0.5)

            # Neuer Versuch: IR-Sensor erneut auslesen
            sc.get_ir()
            if sum(sc.digital) == 0:
                print("Linie weiterhin nicht gefunden – Fahrzeug gestoppt.")
                break
            else:
                print("Linie wiedergefunden – Fortsetzung der Fahrt.")
                sc.drive(new_speed=30, new_angle=90) # <<< WICHTIG: Wieder losfahren
                continue
        # Berechne Fehler (Abweichung von der Mitte)
        error = sum(w * s for w, s in zip(weights, sc.digital))
        integral += error
        derivative = error - last_error

        # PID-Regelung
        correction = Kp * error + Ki * integral + Kd * derivative
        new_angle = 90 + correction
        new_angle = max(45, min(135, new_angle))  # Begrenzung

        sc.drive(new_angle=new_angle)
        last_error = error
        time.sleep(0.05)

    sc.drive(new_speed=0, new_angle=90)
    sc.stop()
