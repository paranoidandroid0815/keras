import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report

#  1. Daten simulieren (ersetzbar durch echte Daten!)
np.random.seed(42)

n_samples = 1000  # Anzahl der Datenpunkte

data = {
    "Leistung_MW": np.random.normal(50, 10, n_samples),
    "Dauer": np.random.normal(10, 2, n_samples),
    "Beschleunigung_MW": np.random.normal(0.5, 0.1, n_samples),
    "Ausfall": np.random.choice([0, 1], size=n_samples, p=[0.95, 0.05])  # 5% Ausfälle
}

df = pd.DataFrame(data)

#  2. Daten normalisieren
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df.iloc[:, :-1]), columns=df.columns[:-1])
df_scaled["Ausfall"] = df["Ausfall"]  # Zielvariable bleibt unberührt

#  3. Funktion zur Sequenz-Erstellung für LSTM
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data.iloc[i:i+seq_length, :-1].values)  # Features (ohne "Ausfall")
        y.append(data.iloc[i+seq_length, -1])  # Zielwert ("Ausfall" der Zukunft)
    return np.array(X), np.array(y)

sequence_length = 10  # Anzahl der vergangenen Zeitschritte, die als Input dienen

X, y = create_sequences(df_scaled, sequence_length)

#  4. Train-Test-Split (80% Training, 20% Test)
split_idx = int(0.8 * len(X))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

#  5. LSTM-Modell erstellen
model = Sequential([
    LSTM(50, activation='relu', return_sequences=True, input_shape=(sequence_length, 3)),
    Dropout(0.2),
    LSTM(30, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid')  # Sigmoid für Klassifikation
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#  6. Modell trainieren
history = model.fit(X_train, y_train, epochs=30, batch_size=16, validation_data=(X_test, y_test))

#  7. Vorhersagen auf Testdaten
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int)

#  8. Modellbewertung
print("\nKlassifikationsbericht:")
print(classification_report(y_test, y_pred))

#  9. Visualisierung der Vorhersagen
plt.figure(figsize=(10, 5))
plt.plot(y_test[:100], label="Tatsächlicher Ausfall (0/1)")
plt.plot(y_pred[:100], label="Vorhergesagter Ausfall (0/1)", linestyle="dashed", color="red")
plt.legend()
plt.title("Vergleich: Tatsächlicher vs. vorhergesagter Ausfall")
plt.show()
