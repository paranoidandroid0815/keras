import pandas as pd
import matplotlib.pyplot as plt
import re

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
    
    # Werte als Liste von Floats extrahieren
    values = [float(x.replace(",", ".")) for x in werte.split(".") if x.replace(",", ".").replace("-", "").replace(".", "").isdigit()]


# Teile die Zeichenkette an den Kommas auf
einzelne_werte_als_string = werte_als_string.split(",")

# Wandle die einzelnen Zeichenketten in Fließkommazahlen um
werte = [float(wert) for wert in einzelne_werte_als_string]





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

plt.xlabel("Messpunkt")
plt.ylabel("Wert")
plt.legend()
plt.title("Zeitreihen von Umlaufdaten")
plt.show()
