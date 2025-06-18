import time
from basisklassen import Ultrasonic
from SonicCar import SonicCar

def run_mode(mode):
    ultrasonic_sensor = Ultrasonic()
    car = SonicCar(ultrasonic_sensor)

    if mode == 3:
        car.fahrmodus_3(stop_distance=10)
    elif mode == 4:
        car.fahrmodus_4(duration=3)
    else:
        print("Ungültiger Modus:", mode)
        return

    # Fahrprotokoll speichern
    log_filename = "fahrprotokoll.log"
    with open(log_filename, "w") as logfile:
        for entry in car.get_log():
            logfile.write(f"{entry}\n")

    print(f"Fahrmodus {mode} abgeschlossen. Protokoll gespeichert in '{log_filename}'.")

if __name__ == "__main__":
    run_mode(4)  # Standardmäßig Modus 4
