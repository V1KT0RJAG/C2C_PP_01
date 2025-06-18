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
        print("Fahrmodus 5 (PID): Linienverfolgung gestartet")
        self.drive(speed=70, steering_angle=90)

        start_time = time.time()
        weights = [-2, -1, 0, 1, 2]  # Sensor-Gewichtung

        # PID-Parameter
        Kp = 12.0
        Ki = 1.0
        Kd = 8.0

        last_error = 0
        integral = 0

        while time.time() - start_time <= 60:
            ir = self.infrared.read_digital()
            self.log_status()

            if sum(ir) == 0:
                print("Linie verloren – Rückwärtsfahren und Neuversuch.")
                self.drive(speed=-30, steering_angle=90)  # Rückwärts geradeaus
                time.sleep(1)  # 1 Sekunde rückwärts fahren
                self.stop()
                time.sleep(0.5)

                # Neuer Versuch: IR-Sensor erneut auslesen
                ir = self.infrared.read_digital()
                if sum(ir) == 0:
                    print("Linie weiterhin nicht gefunden – Fahrzeug gestoppt.")
                    break
                else:
                    print("Linie wiedergefunden – Fortsetzung der Fahrt.")
                    self.drive(speed=70, steering_angle=90) # <<< WICHTIG: Wieder losfahren
                    continue
            # Berechne Fehler (Abweichung von der Mitte)
            error = sum(w * s for w, s in zip(weights, ir))
            integral += error
            derivative = error - last_error

            # PID-Regelung
            correction = Kp * error + Ki * integral + Kd * derivative
            steering_angle = 90 + correction
            steering_angle = max(45, min(135, steering_angle))  # Begrenzung

            self.drive(steering_angle=steering_angle)
            last_error = error
            time.sleep(0.05)

        self.stop()
        print("Fahrmodus 5 beendet.")


    def get_log(self):
        """
        Gibt das Fahrprotokoll zurück.

        Returns:
            list: Liste mit protokollierten Zuständen.
        """
        return self.log
