import pandas as pd
import numpy as np

# Crear tiempo total en segundos
total_time = 5 * 60  # 5 minutos
time = np.arange(0, total_time)

# Inicializar arrays
speed = np.zeros_like(time, dtype=float)
steering_angle = np.zeros_like(time, dtype=float)

# Sección 1: 0 a 30s, de 0 a 40, angle = 90
t1 = (time < 30)
speed[t1] = np.linspace(0, 40, np.sum(t1)) + np.random.normal(0, 1, np.sum(t1))
steering_angle[t1] = 90 + np.random.normal(0, 1, np.sum(t1))

# Sección 2: 30 a 90s, 0 a 100, angle = 90
t2 = (time >= 30) & (time < 90)
speed[t2] = np.linspace(0, 100, np.sum(t2)) + np.random.normal(0, 2, np.sum(t2))
steering_angle[t2] = 90 + np.random.normal(0, 1, np.sum(t2))

# Sección 3: 90 a 150s, speed = -50, angle = 45
t3 = (time >= 90) & (time < 150)
speed[t3] = -50 + np.random.normal(0, 2, np.sum(t3))
steering_angle[t3] = 45 + np.random.normal(0, 1, np.sum(t3))

# Sección 4: 150s en adelante, speed = -100, angle = 135
t4 = (time >= 150)
speed[t4] = -100 + np.random.normal(0, 3, np.sum(t4))
steering_angle[t4] = 135 + np.random.normal(0, 1, np.sum(t4))

# Crear DataFrame
df = pd.DataFrame({
    'time': time,
    'speed': speed,
    'steering_angle': steering_angle
})

# Guardar como CSV
df.to_csv('simulated_car_data.csv', index=False)

print("CSV guardado exitosamente.")
