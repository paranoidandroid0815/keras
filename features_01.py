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
# links und rechtsumläufe separat vergleichen
# Leistungsaufnahme links und rechts vergleichen
# Möglichkeit alle Umläufe mit Diagnosemeldungen auszugeben
#

#Für Tabellen
import pandas as pd
#Zum Plotten
import matplotlib.pyplot as plt
import re
#Für Matrizen
import numpy as np

# Datei einlesen
data_file = "/home/amok/Projects/keras/umlaufdatenkurz.csv"
with open(data_file, "r", encoding="ISO-8859-1") as f:
    lines = f.readlines()

# Leere Liste für DataFrame
records = []

for line in lines:
    parts = line.strip().split(";")
    if len(parts) < 10:
        continue  # Zeile überspringen, falls zu kurz
    
    objekt, datum, zeit, richtung, umlaufzeit, temperatur, diagnose, antrieb, intervall, werte = parts[:10]
    
    # Datum-Zeit als String behalten
    timestamp = f"{datum} {zeit}"
    
    # Werte korrekt extrahieren (ersetze Kommas mit Punkten und splitte an Kommas)
    #werte = werte.replace(",", ".")
#mein code
        #werte = werte.replace(",", ".")



    values = [float(x) for x in werte.split(",") if re.match(r'^-?\d+(\.\d+)?$', x)]
    
    records.append({
        "timestamp": timestamp,
        "richtung": richtung,
        "umlaufzeit": float(umlaufzeit.replace(",", ".")),
        "temperatur": float(temperatur.replace(",", ".")),
        "diagnose": diagnose,
        "antrieb": antrieb,
        "intervall": float(intervall.replace(",", ".")),
        "werte": values
    })

# In DataFrame umwandeln
df = pd.DataFrame(records)

# Zeitreihe plotten
plt.figure(figsize=(10, 5))
for _, row in df.iterrows():
    plt.plot(range(len(row["werte"])), row["werte"], label=f"{row['timestamp']} ({row['richtung']})")

print(df)
plt.xlabel("Messpunkt")
plt.ylabel("Wert")
plt.legend()
plt.title("Zeitreihen von Umlaufdaten")
# plt.show()



# Beispiel: Position und Zeit (kann durch deine Messdaten ersetzt werden)
# time = np.array([0, 1, 2, 3, 4, 5])  # Zeitstempel
position = np.array([0, 2, 6, 12, 20, 30])  # Positionsdaten (z.B. in Metern)

time = range(len(row["werte"]))  # Zeitstempel
position = row["werte"]  # Positionsdaten (z.B. in Metern)

print(range(len(row["werte"])))
print(time)

# print(df['werte'].values)
# print(df['timestamp'])
# Berechne die Geschwindigkeit (erste Ableitung der Position)
velocity = np.gradient(position, time)

# Berechne die Beschleunigung (erste Ableitung der Geschwindigkeit)
acceleration = np.gradient(velocity, time)
# Berechne den Ruck (erste Ableitung der Beschleunigung)
jerk = np.gradient(acceleration, time)

work=np.trapezoid(position)
Gesamtzeit=len(position)*0.02

# Visualisiere den Ruck (ruckartige Bewegungen)
import matplotlib.pyplot as plt
plt.plot(time, jerk)
plt.plot(time,velocity)
plt.title('Ruck (Jerk) der Bewegung')
plt.xlabel('Zeit')
plt.ylabel('Ruck')
plt.text(5,0,f"Geleistete Arbeit{work}")
plt.text(4,1,f"Gesamtzeit{Gesamtzeit}")
plt.show()
