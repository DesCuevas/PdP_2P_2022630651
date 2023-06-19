#Exámen 2do parcial. Código 2.2. Hecho por Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2.
import math

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(squared_distance)

# Clasificador 1-NN
def one_nn_classifier(training_data, test_data):
    predicted_labels = []
    for test_point in test_data:
        min_distance = float('inf')
        predicted_label = None
        for train_point, label in training_data:
            distance = euclidean_distance(test_point, train_point)
            if distance < min_distance:
                min_distance = distance
                predicted_label = label
        predicted_labels.append(predicted_label)
    return predicted_labels

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
            setosa_data.append((features, plant_type))
        elif plant_type == 'versicolor':
            versicolor_data.append((features, plant_type))
        elif plant_type == 'virginica':
            virginica_data.append((features, plant_type))

# Unir las matrices de datos de entrenamiento
training_data = setosa_data + versicolor_data + virginica_data

# Aplicar Leave One Out a cada tipo de planta
accuracy = 0
for plant_data in [setosa_data, versicolor_data, virginica_data]:
    for i in range(len(plant_data)):
        test_point, true_label = plant_data[i]
        training_subset = plant_data[:i] + plant_data[i+1:]
        predicted_labels = one_nn_classifier(training_subset, [test_point])
        if i == len(plant_data) - 1:
            print("Test Point:", test_point)
            print("True Label:", true_label)
            print("Predicted Label:", predicted_labels[0])
            if predicted_labels[0] == true_label:
                print("Correct Classification!")
            else:
                print("Misclassification!")
        if predicted_labels[0] == true_label:
            accuracy += 1

# Calcular el accuracy
accuracy /= len(training_data)
accuracy *= 100

print("Accuracy:", accuracy)
