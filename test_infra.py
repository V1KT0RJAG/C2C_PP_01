



import json
from basisklassen import Infrared # Passe den Import ggf. an

# Initialisiere den Sensor
ir = Infrared()

# Starte Kalibrierung
ir.cali_references()

# Speichere die Referenzwerte automatisch
ir.save_references("ref.json")




# from basisklassen import Infrared
# import time

# ir = Infrared()
# print("Teste IR-Sensor – halte ihn über Linie und Boden")

# try:
#     while True:
#         values = ir.read_digital()
#         print("IR-Werte:", values)
#         time.sleep(0.3)
# except KeyboardInterrupt:
#     print("Test beendet.")
