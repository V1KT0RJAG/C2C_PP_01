import json
from basisklassen import BackWheels, FrontWheels

class BaseCar:
    def __init__(self, config_path="config.json"):
        # Lädt Konfigurationswerte aus einer JSON-Datei
        with open(config_path, "r") as file:
            config = json.load(file)

        # Konfigurationswerte mit Standardwerten als Fallback
        self._turning_offset = config.get("turning_offset", 0)
        self._forward_A = config.get("forward_A", 0)
        self._forward_B = config.get("forward_B", 0)

        # Initialisiert die Radobjekte
        self._back_wheels = BackWheels()
        self._front_wheels = FrontWheels()

        # Setzt Anfangswerte für Geschwindigkeit und Lenkwinkel
        self._speed = 0
        self._steering_angle = 90  # 90° = geradeaus

    @property
    def steering_angle(self):
        # Gibt den aktuellen Lenkwinkel zurück
        return self._steering_angle

    @steering_angle.setter
    def steering_angle(self, angle):
        # Begrenzung des Lenkwinkels auf einen sinnvollen Bereich (45°–135°)
        angle = max(45, min(135, angle))

        # Anwendung des Konfigurations-Offsets
        angle += self._turning_offset
        # Speichern und Weitergabe an die Vorderräder
        self._steering_angle = angle
        self._front_wheels.turn(angle)

    @property
    def speed(self):
        # Gibt die aktuelle Geschwindigkeit zurück
        return self._speed

    @speed.setter
    def speed(self, value):
        # Begrenzung der Geschwindigkeit auf -100 bis 100
        value = max(-100, min(100, value))
        self._speed = value

        if value > 0:
            # Vorwärtsfahrt aktivieren
            self._back_wheels.forward()
            self._back_wheels.speed = value + self._forward_A
        elif value < 0:
            # Rückwärtsfahrt aktivieren
            self._back_wheels.backward()
            self._back_wheels.speed = abs(value + self._forward_B)
        else:
            # Fahrzeug anhalten
            self._back_wheels.stop()

    @property
    def direction(self):
        # Gibt die Fahrtrichtung zurück:
        # 1 = vorwärts, -1 = rückwärts, 0 = steht
        if self._speed > 0:
            return 1
        elif self._speed < 0:
            return -1
        else:
            return 0

    def drive(self, speed=None, steering_angle=None):
        # Kombinierte Methode zum Setzen von Geschwindigkeit und Lenkwinkel
        if speed is not None:
            self.speed = speed
        if steering_angle is not None:
            self.steering_angle = steering_angle

    def stop(self):
        # Stoppt das Fahrzeug durch Setzen der Geschwindigkeit auf 0
        self.speed = 0
        
