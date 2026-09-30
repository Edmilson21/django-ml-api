import joblib # esto es para cargar o subir los modelos en django
from sklearn.ensemble import RandomForestClassifier
import numpy as np


# Datos simples de ejemplo
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0, 1, 0, 1])

modelo = RandomForestClassifier()
modelo.fit(X, y)

joblib.dump(modelo, 'modelo.pkl')
print("Modelo guardado")