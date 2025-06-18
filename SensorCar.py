import time
import random
import numpy as np
from basecar import BaseCar
from basisklassen import Ultrasonic
from basisklassen import Infrared  # Stelle sicher, dass diese Klasse korrekt importiert wird
from SonicCar import SonicCar

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

    def get_distance(self, retries=1, delay=0.01, min_valid=2.0, max_valid=400.0):
        distance = None  # Initialisierung

        for attempt in range(1, retries + 1):
            distance = self.ultrasonic.distance()
            if distance is not None and min_valid <= distance <= max_valid:
                print(f"Erfolgreiche Messung: {distance} cm")
                self.log.append({
                    "timestamp": time.time(),
                    "event": "distance_success",
                    "attempt": attempt,
                    "measured_value": distance
                })
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
        return None  # oder 0, je nachdem wie du Fehler behandeln willst


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
        self.drive(speed=60, steering_angle=90)

        start_time = time.time()
        weights = [-2, -1, 0, 1, 2]
        Kp, Ki, Kd = 8.0, 0.2, 2.0
        last_error = 0
        integral = 0
        loop_counter = 0

        while True:
            current_time = time.time()
            if current_time - start_time > 60:
                break  # Zeit abgelaufen

            ir = self.infrared.read_digital()
            self.log_status()

            if loop_counter % 10 == 0:
                distance = self.get_distance(retries=1)
                if distance is not None and distance > 0:
                    print(f"[Live] Ultraschall-Distanz: {distance} cm")
                    if distance < 20:
                        print("Hindernis erkannt – Anhalten.")
                        self.stop()
                        time.sleep(0.1)
                        break
                else:
                    print(f"[Fehler] Ultraschallmessung fehlgeschlagen (Code: {distance})")

            if sum(ir) == 0:
                print("Linie verloren – Rückwärtsfahren und Suche starten.")
                self.drive(speed=-30, steering_angle=90)

                # Solange keine Linie erkannt wird, weiter rückwärts fahren
                if sum(ir) == 0:
                    print("Linie verloren – Rückwärtsfahren mit Gegenlenkung.")
    
                    while True:
                        ir = self.infrared.read_digital()
                        error = sum(w * s for w, s in zip(weights, ir))  # gleiche weights wie beim Vorwärtsfahren
                        correction = Kp * error  # einfache P-Regel reicht oft
                        steering_angle = max(45, min(135, 90 - correction))  # Gegenlenken beim Rückwärtsfahren!

                        self.drive(speed=-30, steering_angle=steering_angle)
                        time.sleep(0.2)

                        if sum(ir) > 0:
                            print("Linie wiedergefunden – Fortsetzung der Fahrt.")
                            self.stop()
                            time.sleep(0.2)
                            self.drive(speed=60, steering_angle=90)
                            break
                    
                        else:
                            print("Linie konnte nicht gefunden werden – Fahrzeug gestoppt.")
                            self.stop()
            else:
                error = sum(w * s for w, s in zip(weights, ir))
                integral += error
                derivative = error - last_error
                correction = Kp * error + Ki * integral + Kd * derivative
                steering_angle = max(45, min(135, 90 + correction))
                self.drive(steering_angle=steering_angle)
                last_error = error

            loop_counter += 1
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
