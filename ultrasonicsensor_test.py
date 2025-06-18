import time
from basisklassen import Ultrasonic  # Passe ggf. den Importpfad an

def main():
    # Initialisiere den Ultraschallsensor
    sensor = Ultrasonic()

    # Messe 10 Mal die Distanz und gib die Werte aus
    for i in range(20):
        distance = sensor.distance()
        if distance < 0:
            print(f"Messung {i + 1}: Fehler (Code {distance})")
        else:
            print(f"Messung {i + 1}: {distance} cm")
        time.sleep(1.5)  # Warte 1,5 Sekunden zwischen den Messungen

if __name__ == "__main__":
    main()
