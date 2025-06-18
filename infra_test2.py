import time
import numpy as np
from basisklassen import Infrared  # Ersetze 'your_module' durch den Namen deiner Datei ohne .py

sensor = Infrared()

print("Starte Live-Test. Bewege den Sensor über verschiedene Flächen (z. B. Linie und Hintergrund).")
print("Drücke STRG+C zum Beenden.\n")

try:
    while True:
        analog = sensor.read_analog()
        digital = sensor.read_digital()
        print(f"Analog: {analog} | Digital: {digital}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nTest beendet.")
