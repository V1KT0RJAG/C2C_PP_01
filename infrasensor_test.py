import time
from basisklassen import Infrared

def test_infrared_sensor():
    ir_sensor = Infrared()

    print("Starte Infrarot-Sensortest. Drücke Strg+C zum Beenden.")
    try:
        while True:
            ir_values = ir_sensor.read_digital()
            print(f"Infrarotwerte: {ir_values}")
            time.sleep(0.2)  # Kurze Pause zwischen den Messungen
    except KeyboardInterrupt:
        print("\nTest beendet.")

if __name__ == "__main__":
    test_infrared_sensor()
