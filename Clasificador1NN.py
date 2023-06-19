#Exámen 2do parcial. Código 2.1. Hecho por Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2.
import random
import math

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i])**2
    return math.sqrt(distance)

# Función para clasificar un punto utilizando el método 1NN
def classify_1nn(train_data, test_point):
    # Inicializar la distancia mínima y el vecino más cercano
    min_distance = float('inf')
    nearest_neighbor = None
    
    # Calcular la distancia entre el punto de prueba y cada punto de entrenamiento
    for train_point in train_data:
        distance = euclidean_distance(train_point[:-1], test_point[:-1])
        
        # Actualizar la distancia mínima y el vecino más cercano
        if distance < min_distance:
            min_distance = distance
            nearest_neighbor = train_point
        
        # Imprimir el proceso de prueba en cada iteración
        print(f"Distancia entre {test_point} y {train_point}: {distance}")
    
    # Imprimir el vecino más cercano seleccionado
    print(f"Vecino más cercano: {nearest_neighbor}")
    
    # Devolver la clase del vecino más cercano como la clasificación
    return nearest_neighbor[-1]

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
            setosa_data.append(features + [plant_type])
        elif plant_type == 'versicolor':
            versicolor_data.append(features + [plant_type])
        elif plant_type == 'virginica':
            virginica_data.append(features + [plant_type])

# Mezclar los datos de cada tipo de planta
random.shuffle(setosa_data)
random.shuffle(versicolor_data)
random.shuffle(virginica_data)

# Calcular el número de datos para entrenamiento y prueba (70% y 30%)
setosa_train_size = int(0.7 * len(setosa_data))
versicolor_train_size = int(0.7 * len(versicolor_data))
virginica_train_size = int(0.7 * len(virginica_data))

# Dividir los datos en conjuntos de entrenamiento y prueba
setosa_train_data = setosa_data[:setosa_train_size]
setosa_test_data = setosa_data[setosa_train_size:]

versicolor_train_data = versicolor_data[:versicolor_train_size]
versicolor_test_data = versicolor_data[versicolor_train_size:]

virginica_train_data = virginica_data[:virginica_train_size]
virginica_test_data = virginica_data[virginica_train_size:]

# Concatenar los conjuntos de entrenamiento en un solo conjunto
train_data = setosa_train_data + versicolor_train_data + virginica_train_data

# Clasificar los puntos de prueba y calcular la precisión
correct_predictions = 0
total_predictions = len(setosa_test_data) + len(versicolor_test_data) + len(virginica_test_data)

for test_point in setosa_test_data + versicolor_test_data + virginica_test_data:
    predicted_type = classify_1nn(train_data, test_point)
    if predicted_type == test_point[-1]:
        correct_predictions += 1

#Calcular la precisión
accuracy = correct_predictions / total_predictions

# Imprimir resultados
print("Total de predicciones:", total_predictions)
print("Predicciones correctas:", correct_predictions)
print("Precisión:", accuracy)
