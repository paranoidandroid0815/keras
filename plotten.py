import matplotlib.pyplot as plt
import numpy as np

# Beispiel: Erstelle Daten für den Graphen
x = np.linspace(0, 10, 100)  # 100 Werte zwischen 0 und 10
y = np.sin(x)  # Sinus-Funktion

# Plot erstellen
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="sin(x)", color="blue", linewidth=2)

# Titel und Achsenbeschriftungen
plt.title("Beispiel: Sinus-Funktion", fontsize=14)
plt.xlabel("x-Werte", fontsize=12)
plt.ylabel("sin(x)", fontsize=12)

# Gitter und Legende hinzufügen
plt.grid(True)
plt.legend()

# Graph anzeigen
plt.show()
