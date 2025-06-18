import time
import random
from basecar import BaseCar
from basisklassen import Ultrasonic  # Passe ggf. den Importpfad an

class SonicCar(BaseCar):
    def __init__(self, ultrasonic_sensor: Ultrasonic):
        super().__init__()
        self.ultrasonic = ultrasonic_sensor
        self.log = []

    def get_distance(self, retries=5, delay=0.2):
        """
        Führt eine robuste Distanzmessung durch.
        Wiederholt die Messung bei Fehlern bis zu 'retries'-mal.
        """
        for attempt in range(retries):
            distance = self.ultrasonic.distance()
            if distance >= 0:
                return distance
            else:
                print(f"[Warnung] Sensorfehler (Code {distance}) – Versuch {attempt + 1} von {retries}")
                time.sleep(delay)
        print("[Fehler] Keine gültige Distanzmessung möglich.")
        #self.stop()
        return 0

    def log_status(self):
        """Speichert den aktuellen Fahrzeugstatus und Sensorwert."""
        distance = self.get_distance()
        self.log.append({
            "timestamp": time.time(),
            "speed": self.speed,
            "steering_angle": self.steering_angle,
            "direction": self.direction,
            "distance": distance
        })

    def fahrmodus_3(self, stop_distance=10):
        """Fährt vorwärts, bis ein Hindernis erkannt wird."""
        print("Fahrmodus 3: Vorwärtsfahrt bis Hindernis")
        self.drive(speed=30, steering_angle=90)
        while self.get_distance() > stop_distance:
            self.log_status()
            time.sleep(0.8)
        self.stop()
        self.log_status()
        print("Hindernis erkannt – Fahrzeug gestoppt.")


    def fahrmodus_4(self, duration=30):
        """
        Fahrmodus 4: Erkundungstour mit Hindernisvermeidung.

        Das Fahrzeug fährt für eine bestimmte Dauer geradeaus und weicht Hindernissen aus,
        wenn diese näher als 35 cm erkannt werden. Es führt gelegentlich zufällige Lenkbewegungen aus,
        um eine explorative Bewegung zu simulieren.
        
        Parameter:
        - duration (int): Dauer der Erkundungstour in Sekunden.
        """
        print("Fahrmodus 4: Erkundungstour")
        start_time = time.time()

        # Starte mit Vorwärtsfahrt bei mittlerer Geschwindigkeit und gerader Lenkung
        self.drive(speed=40, steering_angle=90)

        # Solange die vorgegebene Dauer nicht überschritten ist
        while time.time() - start_time < duration:
            # Messe die aktuelle Distanz zum nächsten Hindernis
            distance = self.get_distance()

            # Wenn ein Hindernis erkannt wird (unter 15 cm)
            if distance != 0 and distance < 15:
                print("Hindernis erkannt – Ausweichmanöver")
                self.stop()
                # Rückwärtsfahrt mit zufälliger Lenkung nach links oder rechts
                self.drive(speed=-40, steering_angle=random.choice([45, 135]))
                self.log_status()
                time.sleep(5)  # kurze Rückwärtsfahrt

                # Danach wieder Vorwärtsfahrt mit gerader Lenkung
                self.drive(speed=40, steering_angle=90)

            else:
                # Mit 10% Wahrscheinlichkeit wird eine neue Lenkung gewählt
                if random.random() < 0.1:
                    new_angle = random.choice([70, 110])  # leichte Kurve
                    self.drive(steering_angle=new_angle)

            # Protokolliere den aktuellen Status
            self.log_status()
            time.sleep(0.3)  # kurze Pause zwischen den Zyklen
        # Stoppe das Fahrzeug nach Ablauf der Zeit
        self.stop()
        self.log_status()
        print("Erkundungstour beendet.")


    def get_log(self):
        """Gibt das Fahrprotokoll zurück."""
        return self.log
