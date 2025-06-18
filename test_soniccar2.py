import time
from datetime import datetime
from basisklassen import Ultrasonic
from SonicCar import SonicCar

sensor = Ultrasonic()
car = SonicCar(sensor)

car.fahrmodus_4(duration=10)

log = car.get_log()

# Berechne Gesamtdauer
timestamps = [entry["timestamp"] for entry in log]
total_time = max(timestamps) - min(timestamps)
readable_total_time = time.strftime('%H:%M:%S', time.gmtime(total_time))

print(f"Gesamtdauer: {readable_total_time}")

# Gib jeden Eintrag aus
for eintrag in log:
    readable_time = datetime.fromtimestamp(eintrag["timestamp"]).strftime('%H:%M:%S')
    print(f"Zeit: {readable_time}, Geschwindigkeit: {eintrag['speed']}")
