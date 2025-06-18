import time
import random
import numpy as np
from basecar import BaseCar
from basisklassen import Ultrasonic
from basisklassen import Infrared  # Stelle sicher, dass diese Klasse korrekt importiert wird

class SensorCar(BaseCar):
    def __init__(self, ultrasonic_sensor: Ultrasonic, infrared_sensor: Infrared):
        """
        Initialisiert das SensorCar mit Ultraschall- und Infrarotsensor.

        Args:
            ultrasonic_sensor (Ultrasonic): Objekt für Ultraschallsensor.
            infrared_sensor (Infrared): Objekt für Infrarotsensor.
        """
        super().__init__()
        self.ultrasonic = ultrasonic_sensor
        self.infrared = infrared_sensor
        self.log = []  # Liste zur Protokollierung von Fahr- und Sensordaten

    def get_distance(self, retries=0, delay=0.2, min_valid=2.0, max_valid=400.0):
#     Führt eine robuste Distanzmessung durch. Wiederholt die Messung bei Fehlern oder unplausiblen Werten. Protokolliert Fehlversuche im internen Log.
#     Args:
#         retries (int): Anzahl der Wiederholungsversuche. 
#         delay (float): Wartezeit zwischen den Versuchen.
#         min_valid (float): Minimale plausible Distanz in cm.
#         max_valid (float): Maximale plausible Distanz in cm.

#     Returns:
#         float: Gemessene Distanz oder 0 bei Fehler.
        for attempt in range(1, retries + 1):
            distance = self.ultrasonic.distance()
            if distance is not None and min_valid <= distance <= max_valid:
                return distance
            else:
                print(f"[Warnung] Ungültige Distanzmessung ({distance}) – Versuch {attempt} von {retries}")
                self.log.append({
                    "timestamp": time.time(),
                    "event": "distance_error",
                    "attempt": attempt,
                    "measured_value": distance
                })
                time.sleep(delay)

        print("[Fehler] Keine gültige Distanzmessung nach mehreren Versuchen.")
        self.log.append({
            "timestamp": time.time(),
            "event": "distance_failed",
            "retries": retries
        })
        return 0

    def log_status(self):
        """
        Protokolliert den aktuellen Fahrzeugstatus inkl. Infrarot- und Ultraschalldaten.
        """
        distance = self.get_distance()
        ir_values = self.infrared.read_digital()
        self.log.append({
            "timestamp": time.time(),
            "speed": self.speed,
            "steering_angle": self.steering_angle,
            "direction": self.direction,
            "distance": distance,
            "infrared": ir_values
        })

    def fahrmodus_5(self):
        print("Fahrmodus 5: Linienverfolgung gestartet")
        self.drive(speed=50, steering_angle=90)  # Starte mit mittlerer Geschwindigkeit und gerader Lenkung

        start_time = time.time()  # Startzeit merken

        while True:
            # Prüfe, ob 20 Sekunden vergangen sind
            if time.time() - start_time > 40:
                print("Zeitlimit erreicht – Fahrzeug gestoppt.")
                self.stop()
                break

            ir = self.infrared.read_digital()  # Lese digitale Infrarotwerte
            self.log_status()  # Protokolliere aktuellen Zustand

            if sum(ir) == 0:
                # Wenn alle Sensoren 0 melden, ist die Linie verloren
                print("Linie verloren – Fahrzeug gestoppt.")
                self.stop()
                break
            if ir == [0, 0, 1, 0, 0]:
                self.drive(steering_angle=90)  # Geradeaus
            elif ir[0] == 1 or ir[1] == 1:
                self.drive(steering_angle=55)  # Nach links lenken
            elif ir[3] == 1 or ir[4] == 1:
                self.drive(steering_angle=125) # Nach rechts lenken   
            else:
                self.drive(steering_angle=90)  # Standard: geradeaus

            time.sleep(0.1)  # Kurze Pause für stabile Steuerung

    def get_log(self):
        """
        Gibt das Fahrprotokoll zurück.

        Returns:
            list: Liste mit protokollierten Zuständen.
        """
        return self.log
