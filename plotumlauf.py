import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv('deine_datei.csv', sep=';', header=None)

# Spalten benennen
df.columns = [
    'Identifier', 'Datum', 'Uhrzeit', 'Status', 'Wert1', 'Wert2', 
    'Leer', 'Zusatz', 'Wert3', 'Liste'
]

# Numerische Werte konvertieren
df['Wert1'] = df['Wert1'].str.replace(',', '.').astype(float)
df['Wert2'] = df['Wert2'].str.replace(',', '.').astype(float)
df['Wert3'] = df['Wert3'].str.replace(',', '.').astype(float)

# Liste der numerischen Werte verarbeiten
df['Liste'] = df['Liste'].apply(lambda x: [float(i.replace(',', '.')) for i in x.split(',')])

# Funktion, um ausgewählte Zeilen zu visualisieren
def plot_zeilen(zeilen_indices):
    plt.figure(figsize=(12, 6))
    
    for idx in zeilen_indices:
        if idx < 0 or idx >= len(df):
            print(f"Zeile {idx} existiert nicht in der Tabelle.")
            continue
        
        werte = df['Liste'].iloc[idx]
        plt.plot(werte, marker='o', linestyle='-', label=f"Zeile {idx+1}")
    
    plt.title("Numerische Werte ausgewählter Zeilen")
    plt.xlabel("Index")
    plt.ylabel("Wert")
    plt.legend()
    plt.grid(True)
    plt.show()

# Beispielaufruf: Zeilen 0 und 1 (erste und zweite Zeile) visualisieren
plot_zeilen([0, 1])

