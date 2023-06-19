#Exámen 2do parcial. Código 1.1. Hecho por Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2.
import random
from math import sqrt

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += (point1[i] - point2[i]) ** 2
    return sqrt(squared_distance)

# Función para clasificar un punto de prueba utilizando el clasificador euclidiano
def classify_euclidean(test_point, training_data, training_labels):
    min_distance = float('inf')
    min_label = None
    for i in range(len(training_data)):
        distance = euclidean_distance(test_point, training_data[i])
        if distance < min_distance:
            min_distance = distance
            min_label = training_labels[i]
    return min_label

# Crear matrices para cada tipo de planta
setosa_data = []
versicolor_data = []
virginica_data = []

# Abrir el archivo
with open('IrisData.data', 'r') as file:
    # Leer cada línea del archivo
    lines = file.readlines()
    for line in lines:
        # Dividir la línea en valores separados por comas
        values = line.strip().split(',')
        # Obtener los valores de las características y el tipo de planta
        features = [float(value) for value in values[:4]]
        plant_type = values[4]
        
        # Agregar los valores a la matriz correspondiente
        if plant_type == 'setosa':
            setosa_data.append(features)
        elif plant_type == 'versicolor':
            versicolor_data.append(features)
        elif plant_type == 'virginica':
            virginica_data.append(features)

# Definir el tamaño de entrenamiento y prueba (70% y 30% respectivamente)
train_size = 0.7
test_size = 0.3

# Separar los datos de cada tipo de planta en conjuntos de entrenamiento y prueba
setosa_train = random.sample(setosa_data, int(len(setosa_data) * train_size))
setosa_test = [data for data in setosa_data if data not in setosa_train]

versicolor_train = random.sample(versicolor_data, int(len(versicolor_data) * train_size))
versicolor_test = [data for data in versicolor_data if data not in versicolor_train]

virginica_train = random.sample(virginica_data, int(len(virginica_data) * train_size))
virginica_test = [data for data in virginica_data if data not in virginica_train]

# Unir los conjuntos de entrenamiento y prueba
train_data = setosa_train + versicolor_train + virginica_train
test_data = setosa_test + versicolor_test + virginica_test

# Crear las etiquetas correspondientes a los datos de entrenamiento y prueba
train_labels = ['setosa'] * len(setosa_train) + ['versicolor'] * len(versicolor_train) + ['virginica'] * len(virginica_train)
test_labels = ['setosa'] * len(setosa_test) + ['versicolor'] * len(versicolor_test) + ['virginica'] * len(virginica_test)

# Realizar clasificación para los datos de prueba
correct_predictions = 0
for i in range(len(test_data)):
    test_instance = test_data[i]
    predicted_label = classify_euclidean(test_instance, train_data, train_labels)
    if predicted_label == test_labels[i]:
       correct_predictions += 1
    print(f"Instance {i+1}: Test Data: {test_instance}, Actual: {test_labels[i]}, Predicted: {predicted_label}")

# Calcular la precisión del clasificador
accuracy = correct_predictions / len(test_data) * 100
print(f"Accuracy: {accuracy}%")
