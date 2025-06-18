# Se importa un módulo externo llamado 'basisklassen', aunque en este código no se utiliza.
import basisklassen


# Se define la clase BaseCar que representa un automóvil básico con dirección, velocidad y dirección de movimiento.
class BaseCar:

    def __init__(self):
        """
        Constructor de la clase BaseCar. Inicializa los atributos privados:
        - __steering_angle: ángulo de dirección (valor inicial = 0)
        - __speed: velocidad actual (valor inicial = 0)
        - __direction: dirección del vehículo (valor inicial = 0)
        """
        self.__steering_angle = 0
        self.__speed = 0
        self.__direction = 0
        print("BaseCar erzeugt")  # Imprime mensaje indicando que el objeto BaseCar ha sido creado (en alemán).


    # Getter para el ángulo de dirección. Se define como propiedad para acceso tipo atributo.
    @property
    def getAngle(self):
        print(self.__steering_angle)
        return self.__steering_angle

    # Setter para el ángulo de dirección. Limita el valor entre 45 y 135 grados.
    def setAngle(self, angle):
        """
        Establece el ángulo de dirección. El valor se restringe entre 45 y 135 grados.
        - Si es menor que 45, se ajusta a 45.
        - Si es mayor que 135, se ajusta a 135.
        """
        if angle < 45:
            self.__steering_angle = 45
        elif angle > 135:
            self.__steering_angle = 135
        else:
            self.__steering_angle = angle 


    # Getter para la velocidad. También es una propiedad.
    @property
    def getSpeed(self):
        print(self.__speed)
        return self.__speed

    # Setter para la velocidad. Limita la velocidad entre -100 y 100.
    def setSpeed(self, speed):
        """
        Establece la velocidad del vehículo. El valor se restringe entre -100 y 100.
        - Velocidades negativas representan reversa.
        """
        if speed < -100:
            self.__speed = -100
        elif speed > 100:
            self.__speed = 100
        else:
            self.__speed = speed


    # Getter para la dirección del vehículo.
    @property
    def getDirection(self):
        print(self.__direction)
        return self.__direction


    # Método de conducción (actualmente vacío)
    def drive(self, speed, angle):
        """
        Método para conducir el vehículo ajustando velocidad y ángulo.
        Actualmente no implementado (pass).
        """
        pass

    # Método para detener el vehículo (establece velocidad a 0).
    def stop(self):
        """
        Detiene el vehículo estableciendo la velocidad a 0.
        """
        self.setSpeed(0)

    # Método de logging (actualmente vacío).
    def log_speed():
        """
        Registra o muestra la velocidad actual.
        Método no implementado (pass).
        """
        pass

    # Método para leer una configuración desde un archivo.
    def read_config(path):
        """
        Lee configuración desde un archivo dado por 'path'.
        Método no implementado (pass).
        """
        pass


# === Ejecución del programa ===

# Se crea una instancia de BaseCar
car = BaseCar()

# Se establece un ángulo de dirección fuera del límite superior (150 -> se ajusta a 135)
car.setAngle(150)
car.getAngle  # Aunque se accede a la propiedad, no se imprime porque no se están usando paréntesis.

# Se establece una velocidad fuera del límite inferior (-130 -> se ajusta a -100)
car.setSpeed(-130)
car.getSpeed  # Igual que antes, no se imprimirá nada porque falta '()'.

# Se establece una velocidad válida (80)
car.setSpeed(80)
car.getSpeed  # Tampoco imprime por falta de paréntesis.

# El auto se detiene (velocidad = 0)
car.stop()


# Comentario que sugiere un import específico desde 'basisklassen' (no ejecutado en el código):
# from basisklassen import Ultrasonic, BackWheels, FrontWheels
