#Exámen 2do parcial. Código 1.2. Hecho por Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2.
import math

def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

setosa_data = []
versicolor_data = []
virginica_data = []

with open('IrisData.data', 'r') as file:
    lines = file.readlines()
    for line in lines:
        values = line.strip().split(',')
        features = [float(value) for value in values[:4]]
        plant_type = values[4]

        if plant_type == 'setosa':
            setosa_data.append(features)
        elif plant_type == 'versicolor':
            versicolor_data.append(features)
        elif plant_type == 'virginica':
            virginica_data.append(features)

correct_predictions = 0
total_instances = 0

# Clasificar cada instancia
for plant_type, data in [('setosa', setosa_data), ('versicolor', versicolor_data), ('virginica', virginica_data)]:
    for i in range(len(data)):
        # Obtener la instancia actual para clasificar
        instance_to_classify = data[i]

        # Crear listas para almacenar las distancias y los tipos de planta
        distances = []
        types = []

        # Calcular la distancia entre la instancia actual y las demás instancias del mismo tipo de planta
        for j in range(len(data)):
            if i != j:
                distance = euclidean_distance(instance_to_classify, data[j])
                distances.append(distance)
                types.append(plant_type)

        # Encontrar el tipo de planta con la distancia mínima
        min_distance_index = distances.index(min(distances))
        predicted_type = types[min_distance_index]

        # Verificar si la clasificación es correcta
        if predicted_type == plant_type:
            correct_predictions += 1
        total_instances += 1

        # Imprimir el proceso de prueba solo para el LOO de la matriz
        if i == len(data) - 1:
            print(f"Instance: {instance_to_classify}")
            print(f"Distances: {distances}")
            print(f"Predicted Type: {predicted_type}")
            print(f"Actual Type: {plant_type}")
            print("---")

# Calcular el porcentaje de precisión
accuracy = correct_predictions / total_instances * 100

# Imprimir el resultado
print("Accuracy:", accuracy)
