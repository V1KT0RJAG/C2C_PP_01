from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time
import random

class Fahrmodus:

    def __init__(self,car):
        self.car = car
    
    def user_selected_mode(self, mode):
        if mode == 1:
            self.fahrmodus_1()
        if mode == 2:
            self.fahrmodus_2()
        if mode == 3:
            self.fahrmodus_3()
        if mode == 4:
            self.fahrmodus_4()
        if mode == 5:
            self.fahrmodus_5()
        if mode == 6:
            self.fahrmodus_6()
        if mode == 7:
            self.fahrmodus_7()
        if mode == 8:
            self.fahrmodus_8()
        else:
            self.car.stop()
            print("Bitte gultige Mode auswaehlen")


    def fahrmodus_1(self):
        print("Fahrmodus 1: Vorwärts und Rückwärts")
        self.car.drive(30,90)  # Geradeaus, langsam
        self.car.log()
        time.sleep(3)
        self.car.stop()
        self.car.log()
        time.sleep(1)
        self.car.drive(-30)  # Rückwärts, langsam
        self.car.log()
        time.sleep(3)
        self.car.stop()
        self.car.log()
        self.car.save_log()

    def fahrmodus_2(self):
        print("Fahrmodus 2: Kreisfahrt")
        # Geradeaus
        self.car.drive(40, 90)
        self.car.log()
        time.sleep(1)
        # Kreisfahrt im Uhrzeigersinn (maximaler Lenkwinkel rechts)
        self.car.drive(new_angle=45)
        self.car.log()
        time.sleep(8)
        # Stopp
        self.car.stop()
        self.car.log()
        time.sleep(1)
        # Rückfahrt: Kreisfahrt gegen den Uhrzeigersinn (maximaler Lenkwinkel links)
        self.car.drive(-40, 135)
        self.car.log()
        time.sleep(8)
        # Geradeaus rückwärts
        self.car.drive(new_angle=90)
        self.car.log()
        time.sleep(1)
        self.car.stop()
        self.car.log()
        self.car.save_log()

    def fahrmodus_3(self, stop_distance=20):
        """Fährt vorwärts, bis ein Hindernis erkannt wird."""
        print("Fahrmodus 3: Vorwärtsfahrt bis Hindernis")
        while self.car.get_distance()>stop_distance:
            self.car.drive(new_speed=40, new_angle=90)
            self.car.log()
        self.car.stop()
        self.car.log()
        self.car.save_log()
        print("Hindernis erkannt – Fahrzeug gestoppt.")

    def fahrmodus_4(self, duration=15, distance_min=25): # duration war = 30
        #Erkundungstour mit Hindernisvermeidung.
        print("Fahrmodus 4: Erkundungstour")
        start_time = time.time()
        self.car.drive(new_speed=40, new_angle=90)
        #Logfile 1
        self.car.log()

        while time.time() - start_time < duration:
            distance = self.car.get_distance()
            if distance is not 0 and distance < distance_min:
                print("Hindernis erkannt – Ausweichmanöver")
                self.car.stop()
                self.car.drive(new_speed=-30, new_angle=random.choice([45, 135]))
                time.sleep(3)
                #Logfile 2
                self.car.log()
                
                self.car.drive(new_speed=40, new_angle=90)
                #Logfile 3
                self.car.log()
                
        self.car.stop()
        self.car.log()
        self.car.save_log()
        print("Erkundungstour beendet.")

    def fahrmodus_5(self):
        print("Fahrmodus 5: Linienverfolgung gestartet")
        self.car.get_ir()

        #To-Do: in App integrieren
        self.car.infra.cali_references()
        self.car.increase_references_by_20()
        self.car.infra.set_references
        time.sleep(5)

        start_time = time.time()
        self.car.drive(new_speed=45, new_angle=90)

        while time.time() - start_time < 40:
        
            self.car.get_ir()

            if sum(self.car.digital) == 0:
                print("Linie verloren – Rückwärtsfahren und Neuversuch.")
                self.car.drive(new_speed=-40, new_angle=90)  # Rückwärts geradeaus
                time.sleep(1)  # 1 Sekunde rückwärts fahren
                self.car.stop()
                self.car.get_ir()
                time.sleep(0.5)
                # Neuer Versuch: IR-Sensor erneut auslesen
                if sum(self.car.digital) == 0:
                    print("Linie weiterhin nicht gefunden – Fahrzeug gestoppt.")
                    break
                else:
                    print("Linie wiedergefunden – Fortsetzung der Fahrt.")
                    self.car.drive(new_speed=40) # <<< WICHTIG: Wieder losfahren

            # if sum(sc.digital) == 0:
            #     counter += 1
                # if counter > 300:
                #     # Wenn alle Sensoren 0 melden, ist die Linie verloren
                #     print("Linie verloren – Fahrzeug gestoppt.")
                #     sc.stop()
                #     break
                # continue
                # #time.sleep(1.5)
            if self.car.digital == [1,0,0,0,0]:
                self.car.drive(new_speed=40, new_angle=45)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [1,1,0,0,0]:
                self.car.drive(new_speed=40, new_angle=56)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,1,0,0,0]:
                self.car.drive(new_speed=40, new_angle=67)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,1,1,0,0]:
                self.car.drive(new_speed=40, new_angle=78)
                self.car.log()
            elif self.car.digital == [0,0,1,0,0]:
                self.car.drive(new_speed=40, new_angle=90)
                self.car.log()
            elif self.car.digital == [0,0,1,1,0]:
                self.car.drive(new_speed=40, new_angle=101)
                self.car.log()
            elif self.car.digital == [0,0,0,1,0]:
                self.car.drive(new_speed=40, new_angle=112)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,0,0,1,1]:
                self.car.drive(new_speed=40, new_angle=123)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,0,0,0,1]:
                self.car.drive(new_speed=40, new_angle=135)
                self.car.log()
                time.sleep(0.1)
    
        self.car.stop()
        self.car.log()
        self.car.save_log()

    def fahrmodus_6(self):
        print("Fahrmodus 6: Kreisfahrt gestartet")
        self.car.get_ir()

        #To-Do: in App integrieren
        self.car.infra.cali_references()
        self.car.increase_references_by_20()
        self.car.infra.set_references
        time.sleep(5)

        start_time = time.time()
        self.car.drive(new_speed=45, new_angle=90)

        while time.time() - start_time < 40:
        
            self.car.get_ir()

            if sum(self.car.digital) == 0:
                print("Linie verloren – Rückwärtsfahren und Neuversuch.")
                self.car.drive(new_speed=-40, new_angle=90)  # Rückwärts geradeaus
                self.car.log()
                time.sleep(1)  # 1 Sekunde rückwärts fahren
                self.car.stop()
                self.car.get_ir()
                self.car.log()
                time.sleep(0.5)
                # Neuer Versuch: IR-Sensor erneut auslesen
                if sum(self.car.digital) == 0:
                    print("Linie weiterhin nicht gefunden – Fahrzeug gestoppt.")
                    self.car.log()
                    break
                else:
                    print("Linie wiedergefunden – Fortsetzung der Fahrt.")
                    self.car.drive(new_speed=40) # <<< WICHTIG: Wieder losfahren
                    self.car.log()

            # if sum(sc.digital) == 0:
            #     counter += 1
                # if counter > 300:
                #     # Wenn alle Sensoren 0 melden, ist die Linie verloren
                #     print("Linie verloren – Fahrzeug gestoppt.")
                #     sc.stop()
                #     break
                # continue
                # #time.sleep(1.5)
            if self.car.digital == [1,0,0,0,0]:
                self.car.drive(new_speed=40, new_angle=45)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [1,1,0,0,0]:
                self.car.drive(new_speed=40, new_angle=56)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,1,0,0,0]:
                self.car.drive(new_speed=40, new_angle=67)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,1,1,0,0]:
                self.car.drive(new_speed=40, new_angle=78)
                self.car.log()
            elif self.car.digital == [0,0,1,0,0]:
                self.car.drive(new_speed=40, new_angle=90)
                self.car.log()
            elif self.car.digital == [0,0,1,1,0]:
                self.car.drive(new_speed=40, new_angle=101)
                self.car.log()
            elif self.car.digital == [0,0,0,1,0]:
                self.car.drive(new_speed=40, new_angle=112)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,0,0,1,1]:
                self.car.drive(new_speed=40, new_angle=123)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,0,0,0,1]:
                self.car.drive(new_speed=40, new_angle=135)
                self.car.log()
                time.sleep(0.1)
    
        self.car.stop()
        self.car.log()
        self.car.save_log()
    
    def fahrmodus_7(self):
        print("Fahrmodus 7: Erweiterte Linienverfolgung mit Hindernisserkennung")
        self.car.get_ir()

        #To-Do: in App integrieren
        # self.car.infra.cali_references()
        # self.car.increase_references_by_20()
        # self.car.infra.set_references
        # time.sleep(5)

        start_time = time.time()
        self.car.drive(new_speed=45, new_angle=90)

        while time.time() - start_time < 40:
        
            self.car.get_ir()

            if sum(self.car.digital) == 0:
                print("Linie verloren – Rückwärtsfahren und Neuversuch.")
                self.car.drive(new_speed=-40, new_angle=90)  # Rückwärts geradeaus
                self.car.log()
                time.sleep(1)  # 1 Sekunde rückwärts fahren
                self.car.stop()
                self.car.get_ir()
                self.car.log()
                time.sleep(0.5)
                # Neuer Versuch: IR-Sensor erneut auslesen
                if sum(self.car.digital) == 0:
                    print("Linie weiterhin nicht gefunden – Fahrzeug gestoppt.")
                    self.car.log()
                    break
                else:
                    print("Linie wiedergefunden – Fortsetzung der Fahrt.")
                    self.car.drive(new_speed=40) # <<< WICHTIG: Wieder losfahren
                    self.car.log()

            # if sum(sc.digital) == 0:
            #     counter += 1
                # if counter > 300:
                #     # Wenn alle Sensoren 0 melden, ist die Linie verloren
                #     print("Linie verloren – Fahrzeug gestoppt.")
                #     sc.stop()
                #     break
                # continue
                # #time.sleep(1.5)
            if self.car.ultra.distance()< 25:
                self.car.log()
                self.car.stop()
                self.car.save_log()
                print("Hindernis erkannt – Fahrzeug gestoppt.") 
                continue  

            if self.car.digital == [1,0,0,0,0]:
                self.car.drive(new_speed=40, new_angle=45)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [1,1,0,0,0]:
                self.car.drive(new_speed=40, new_angle=56)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,1,0,0,0]:
                self.car.drive(new_speed=40, new_angle=67)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,1,1,0,0]:
                self.car.drive(new_speed=40, new_angle=78)
                self.car.log()
            elif self.car.digital == [0,0,1,0,0]:
                self.car.drive(new_speed=40, new_angle=90)
                self.car.log()
            elif self.car.digital == [0,0,1,1,0]:
                self.car.drive(new_speed=40, new_angle=101)
                self.car.log()
            elif self.car.digital == [0,0,0,1,0]:
                self.car.drive(new_speed=40, new_angle=112)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,0,0,1,1]:
                self.car.drive(new_speed=40, new_angle=123)
                self.car.log()
                time.sleep(0.1)
            elif self.car.digital == [0,0,0,0,1]:
                self.car.drive(new_speed=40, new_angle=135)
                self.car.log()
                time.sleep(0.1)
    
        self.car.stop()
        self.car.log()
        self.car.save_log()
                
    def fahrmodus_8(self):
        print("Fahrmodus 8: Infra mit PID Regler")
        self.car.get_ir()

        self.car.infra.cali_references()
        self.car.increase_references_by_20()
        self.car.infra.set_references
        time.sleep(5)

        start_time = time.time()
        weights = [-2, -1, 0, 1, 2]  # Sensor-Gewichtung

        # PID-Parameter
        Kp = 15.0
        Ki = 1.0
        Kd = 8.0
                    

        last_error = 0
        integral = 0
        self.car.drive(new_speed=45, new_angle=90)
        last_steering_angle = 90
        stop_driving = False
        while time.time() - start_time <= 1800:
            distance = self.car.get_distance()
            print("Aktuelle Distanz: ", distance)
            if distance < 25 and distance>=0:
                print(distance)
                self.car.log()
                self.car.stop()
                print("STOOOOP")
                self.car.save_log()
                print("Hindernis erkannt – Fahrzeug gestoppt.")
                continue
                
            self.car.get_ir()
            
            no_line_detecetd = sum(self.car.digital) == 0
            
                
            if no_line_detecetd:
                time_line_is_lost = time.time()
                
                while no_line_detecetd:
                    print("Linie nicht erkannt")
                    
                    # Zurück mit altem Lenkwinkel
                    # self.car.drive(new_speed=-30, new_angle=last_steering_angle)
                    # self.car.get_ir()
                
                    # time.sleep(0.5)
                    
                    # Zurück mit gegenlenken
                    # anti_angle = 180 - last_steering_angle
                    anti_angle = 45 if last_steering_angle > 90 else 135
                    self.car.drive(new_angle=anti_angle, new_speed=-30)
                    # self.car.get_ir()
                    
                    
                    time.sleep(0.25)
                     # Zurück mit altem Lenkwinkel
                    self.car.drive(new_speed=-30, new_angle=last_steering_angle)
                    self.car.get_ir()
                
                    time.sleep(0.4)
                    line_detecetd = sum(self.car.digital) > 0
                    
                    if line_detecetd:
                        self.car.drive(new_angle=last_steering_angle, new_speed=30)
                        print("Linie wiedergefunden!")
                        break
                    print("Anti: ", anti_angle, last_steering_angle)
                    
                    waiting_time_over = time.time() - time_line_is_lost
                    print("Wartezeit: ", waiting_time_over)
                    if waiting_time_over > 2.5:
                        self.car.stop()
                        stop_driving = True
                        break
                    
                if stop_driving:
                    self.car.stop()
                    break
                        
                    
                    
                
            # if sum(self.car.digital) == 0:
            #     print("Linie verloren – Rückwärtsfahren und Neuversuch.")
            #     self.car.drive(new_speed=-20, new_angle=90)  # Rückwärts geradeaus
            #     time.sleep(1)  # 1 Sekunde rückwärts fahren
            #     self.car.stop()
            #     time.sleep(0.5)

            #     # Neuer Versuch: IR-Sensor erneut auslesen
            # self.car.get_ir()
            # if sum(self.car.digital) == 0:
            #         print("Linie weiterhin nicht gefunden – Fahrzeug gestoppt.")
            #         break
            # else:
            #     print("Linie wiedergefunden – Fortsetzung der Fahrt.")
            #     self.car.drive(new_speed=30, new_angle=90) # <<< WICHTIG: Wieder losfahren
               
            # Berechne Fehler (Abweichung von der Mitte)
            else: 
                print("Linie erkannt")
                error = sum(w * s for w, s in zip(weights, self.car.digital))
                integral += error
                derivative = error - last_error

                # PID-Regelung
                correction = Kp * error + Ki * integral + Kd * derivative
                new_angle = 90 + correction
                new_angle = max(45, min(135, new_angle))  # Begrenzung

                if self.car.speed > 0:
                    last_steering_angle = new_angle

                self.car.drive(new_angle=new_angle, new_speed=30)
                last_error = error
                time.sleep(0.25)
                
                
                    #break 
            if sum(self.car.digital) == 5:
                self.car.stop()
                break
        self.car.stop()

    #def fahrmodus_8(self):
        #print("Fahrmodus 8: Erweiterte Linienverfolgung mit Hindernisserkennung")
        #self.car.get_ir()
       # pass