# Trendanalyse der aufgenommen Gesamtleistung
# Indikator für Zeit und Höhe
# Entropeänderungen eines gleitenden Bildausschnittes
# Grauwertverteilung
# Mittelwert
# Standardabweichung
# fft
# Schwellwerte
# Abweichung von Referenz unterschreiten überschreiten der Stromwerte
# Abweichung der Zeit
# Jerk-Analyse (bewertet Unstetigkeiten) Ruckwerte
# Temperatur
# Abweichung mittlere quadratische Abweichung

import numpy as np

# Beispiel: Position und Zeit (kann durch deine Messdaten ersetzt werden)
time = np.array([0, 1, 2, 3, 4, 5])  # Zeitstempel
position = np.array([0, 2, 6, 12, 20, 30])  # Positionsdaten (z.B. in Metern)

# Berechne die Geschwindigkeit (erste Ableitung der Position)
velocity = np.gradient(position, time)

# Berechne die Beschleunigung (erste Ableitung der Geschwindigkeit)
acceleration = np.gradient(velocity, time)
# Berechne den Ruck (erste Ableitung der Beschleunigung)
jerk = np.gradient(acceleration, time)

# Visualisiere den Ruck (ruckartige Bewegungen)
import matplotlib.pyplot as plt
plt.plot(time, jerk)
plt.title('Ruck (Jerk) der Bewegung')
plt.xlabel('Zeit')
plt.ylabel('Ruck')
plt.show()
