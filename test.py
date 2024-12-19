import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# 1. Daten laden und vorbereiten
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalisierung der Pixelwerte auf [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Labels in One-Hot-Encoding umwandeln
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 2. Modell definieren
model = Sequential([
    Flatten(input_shape=(28, 28)),   # Wandelt 28x28-Bilder in einen 1D-Vektor um
    Dense(128, activation='relu'),  # Vollständig verbundene Schicht mit 128 Neuronen
    Dense(10, activation='softmax') # Ausgangsschicht mit 10 Klassen (0-9)
])

# 3. Modell kompilieren
model.compile(
    optimizer='adam',                # Optimierungsalgorithmus
    loss='categorical_crossentropy', # Verlustfunktion für Klassifikation
    metrics=['accuracy']             # Genauigkeit als Metrik
)

# 4. Modell trainieren
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# 5. Modell evaluieren
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"Testgenauigkeit: {test_accuracy:.2f}")

# 6. Beispielvorhersage
import numpy as np
example = np.expand_dims(x_test[0], axis=0) # Erstes Testbild als Beispiel
prediction = model.predict(example)
print(f"Vorhergesagte Klasse: {np.argmax(prediction)}")
