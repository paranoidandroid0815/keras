#Für Tabellen
import pandas as pd
#Zum Plotten
import matplotlib.pyplot as plt
import re
#Für Matrizen
import numpy as np


#import tkinter as tk
#from pandastable import Table


# Datei einlesen
data_file = "/home/amok/Projects/keras/umlaufdatenbereinigt.csv"
with open(data_file, "r", encoding="ISO-8859-1") as f:
    lines = f.readlines()

#print(f"{lines} \n")


 #Leere Liste für DataFrame
records = []

for line in lines:
    #print(f"{line} \n")
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

## print(df.iloc[3])

# Zeitreihe plotten
plt.figure(figsize=(10, 5))
for _, row in df.iterrows():
    plt.plot(range(len(row["werte"])), row["werte"], label=f"{row['timestamp']} ({row['richtung']})")

#Leistung für jeden Umlauf über Zeit
leistung=[]
for _, row in df.iterrows():
    leistungprozeile=np.trapezoid(row["werte"])
    leistung.append(leistungprozeile)


plt.plot(leistung, label="Leistung")
#position = row["werte"]  # Positionsdaten (z.B. in Metern)
#work=np.trapezoid(position)
#Gesamtzeit=len(position)*0.02
print(f"{leistung} \n")

plt.show()




# Fenster erstellen
#root = tk.Tk()
#root.title("DataFrame Viewer")

# Frame für Tabelle
#frame = tk.Frame(root)
#frame.pack(fill="both", expand=True)

# Pandastable anzeigen
#table = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
#table.show()

# root.mainloop()