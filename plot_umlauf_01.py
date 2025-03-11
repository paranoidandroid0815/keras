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

# Bedingtes Filtern:
#
# df["richtung"] == "links" erzeugt eine boolesche Maske, d. h. eine Serie mit True für Zeilen, in denen der Wert der Spalte "richtung" "links" ist, und False für alle anderen Zeilen.
# Auswahl der passenden Zeilen:

# df[df["richtung"] == "links"] wendet diese Maske auf df an und gibt nur die Zeilen zurück, bei denen die Bedingung erfüllt ist.
# Speicherung des gefilterten DataFrames:

# Das Ergebnis wird in df_links gespeichert, sodass dieser neue DataFrame nur noch die Zeilen mit "richtung" == "links" enthält.


df_links = df[df["richtung"] == "L"]
#ich möchte einen Dataframe mit den Rechtsumläufen

#ich möchte einen Dataframe mit den Linksumläufen
df_rechts= df[df["richtung"] == "R"]
## print(df.iloc[3])

print(f"{df_rechts} \n")



#Leistung für jeden Umlauf über Zeit
leistung=[]
for _, row in df.iterrows():
    leistungprozeile=np.trapezoid(row["werte"])
    leistung.append(leistungprozeile)

#Leistung für jeden Umlauf über Zeit
leistung_rechts=[]
for _, row in df_rechts.iterrows():
    leistungprozeile=np.trapezoid(row["werte"])
    leistung_rechts.append(leistungprozeile)

#Leistung für jeden Umlauf über Zeit
leistung_links=[]
for _, row in df_links.iterrows():
    leistungprozeile=np.trapezoid(row["werte"])
    leistung_links.append(leistungprozeile)
    
#work=np.trapezoid(position)
#Gesamtzeit=len(position)*0.02
#print(f"{leistung} \n")

# Initialise the subplot function using number of rows and columns
# figure, axis = plt.subplots(4, 4)


plt.figure(figsize=(10, 5))
plt.subplot(3, 2, 1) # (Zeilen, Spalten, Index)
# Zeitreihe plotten
for _, row in df.iterrows():
    plt.plot(range(len(row["werte"])), row["werte"], label=f"{row['timestamp']} ({row['richtung']})")
plt.title("Alles")


plt.subplot(3, 2, 2) # (Zeilen, Spalten, Index)
plt.plot(leistung, label="Leistung")
plt.title("Leistung")
position = row["werte"]  # Positionsdaten (z.B. in Metern)

plt.subplot(3, 2, 3) # (Zeilen, Spalten, Index)
# Zeitreihe plotten
for _, row in df_rechts.iterrows():
    plt.plot(range(len(row["werte"])), row["werte"], label=f"{row['timestamp']} ({row['richtung']})")
plt.title("Rechts")

plt.subplot(3, 2, 4) # (Zeilen, Spalten, Index)
# Zeitreihe plotten
plt.plot(leistung_rechts, label="Leistung")
plt.title("Leistung Rechts")


plt.subplot(3, 2, 5) # (Zeilen, Spalten, Index)
# Zeitreihe plotten
for _, row in df_links.iterrows():
    plt.plot(range(len(row["werte"])), row["werte"], label=f"{row['timestamp']} ({row['richtung']})")
plt.title("Links")

plt.subplot(3, 2, 6) # (Zeilen, Spalten, Index)
# Zeitreihe plotten
plt.plot(leistung_links, label="Leistung")
plt.title("Leistung Links")




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