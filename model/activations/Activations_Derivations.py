import numpy as np
# Función Sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Función Tangente Hiperbólica y su derivada
def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x) ** 2

# Función Identidad (lineal) y su derivada
def identity(x):
    return x

def identity_derivative(x):
    return 1

# Función Step (escalón) y su derivada
def step(x):
    if x >= 0:
        return 1
    return 0

def step_derivative(x):
    return 0  # No definido para la mayoría de los valores de x en la función de paso

