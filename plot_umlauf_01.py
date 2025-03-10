#Für Tabellen
import pandas as pd
#Zum Plotten
import matplotlib.pyplot as plt
import re
#Für Matrizen
import numpy as np

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

print(df)