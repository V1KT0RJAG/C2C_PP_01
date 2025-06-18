import time
from basecar import BaseCar
from basisklassen import Ultrasonic, Infrared
from SensorCar import SensorCar

# Initialisiere reale Sensorobjekte
ultrasonic_sensor = Ultrasonic()
infrared_sensor = Infrared()

# Lade gespeicherte Referenzwerte für den Infrarotsensor
try:
    infrared_sensor.load_references("ref.json")
except FileNotFoundError:
    print("Referenzdatei 'ref.json' nicht gefunden. Bitte führe zuerst eine Kalibrierung durch.")
    exit(1)

# Erstelle ein SensorCar mit echten Sensoren
car = SensorCar(ultrasonic_sensor, infrared_sensor)

# Starte den Fahrmodus 5
print("Starte Fahrmodus 5...")
car.fahrmodus_5()

# Gib das Fahrprotokoll aus
log = car.get_log()
print("\nFahrprotokoll:")
for eintrag in log:
    print(eintrag)
