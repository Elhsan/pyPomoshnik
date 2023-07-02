import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[0, 0, 1],
                          [1, 1, 1],
                          [1, 0, 1],
                          [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1


for i in range(10000):
    input_layer = training_inputs
    output =  sigmoid(np.dot(input_layer, synaptic_weights) )

    err = training_outputs - output
    adjustments = np.dot( input_layer.T, err * (output * (1 - output)))

    synaptic_weights += adjustments

def chat():
    while True:
        user_input = input("Введите вопрос (например 1 0 1 =>) да: ")
        try:
            input_data = np.array([[int(x) for x in user_input.split()]])
            output = sigmoid(np.dot(input_data, synaptic_weights))
            response = "Да" if output >= 0.5 else "Нет"
            print("Ответ: ", response)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числа разделенные пробелами.")
            
chat()