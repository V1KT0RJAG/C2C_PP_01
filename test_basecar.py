import time
from basecar import BaseCar  # Importiere die Klasse BaseCar, die das Fahrzeug steuert

def fahrmodus_1(car):
    """
    Fahrmodus 1: Das Fahrzeug fährt vorwärts und rückwärts geradeaus.
    """
    print("Fahrmodus 1: Vorwärts und Rückwärts")
    
    # Vorwärtsfahrt mit mittlerer Geschwindigkeit und geradem Lenkwinkel
    print("→ Vorwärtsfahrt:")
    car.drive(speed=30, steering_angle=90)
    print(f"Aktueller Speed: {car.speed} | Lenkwinkel: {car.steering_angle}")
  # Ausgabe der aktuellen Fahrparameter
    time.sleep(3)  # 3 Sekunden fahren
    
    car.stop()  # Fahrzeug anhalten
    time.sleep(1)  # kurze Pause
    
    # Rückwärtsfahrt mit gleicher Geschwindigkeit, Lenkwinkel bleibt unverändert
    print("→ Rückwärtsfahrt:")
    car.drive(speed=-30)
    print(f"Aktueller Speed: {car.speed} | Lenkwinkel: {car.steering_angle}")
    time.sleep(3)
    
    car.stop()  # Fahrzeug anhalten

def fahrmodus_2(car):
    """
    Fahrmodus 2: Das Fahrzeug fährt einen Kreis im und gegen den Uhrzeigersinn.
    """
    print("Fahrmodus 2: Kreisfahrt")
    
    # Geradeausfahrt mit höherer Geschwindigkeit
    print("→ Geradeausfahrt:")
    car.drive(speed=40, steering_angle=90)
    print(f"Aktueller Speed: {car.speed} | Lenkwinkel: {car.steering_angle}")
    time.sleep(1)
    
    # Rechtskurve (im Uhrzeigersinn) mit maximalem Lenkeinschlag
    print("→ Kreisfahrt im Uhrzeigersinn:")
    car.drive(steering_angle=45)
    print(f"Aktueller Speed: {car.speed} | Lenkwinkel: {car.steering_angle}")
    time.sleep(8)
    
    car.stop()  # Fahrzeug anhalten
    time.sleep(1)
    
    # Rückwärtsfahrt in einer Linkskurve (gegen den Uhrzeigersinn)
    print("→ Rückwärts-Kreisfahrt gegen den Uhrzeigersinn:")
    car.drive(speed=-40, steering_angle=135)
    print(f"Aktueller Speed: {car.speed} | Lenkwinkel: {car.steering_angle}")
    time.sleep(8)
    
    # Geradeaus rückwärts
    print("→ Geradeaus rückwärts:")
    car.drive(steering_angle=90)
    print(f"Aktueller Speed: {car.speed} | Lenkwinkel: {car.steering_angle}")
    time.sleep(1)
    
    car.stop()  # Fahrzeug anhalten

if __name__ == "__main__":
    # Hauptprogramm: Initialisiert das Fahrzeug und führt beide Fahrmodi aus
    car = BaseCar()
    fahrmodus_1(car)
    time.sleep(2)  # kurze Pause zwischen den Modi
    fahrmodus_2(car)
