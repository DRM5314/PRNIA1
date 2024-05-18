import model.activations.Activations_Derivations as activations

def activation_function(type,value):
    match type:
        case "sigmode":
            return activations.sigmoid(value)
        case "tanh":
            return activations.tanh(value)
        case "identity":
            return activations.identity(value)
        case "step":
            return activations.step(value)
def activation_function_derivated(type,value):
    match type:
        case "sigmode":
            return activations.sigmoid_derivative(value)
        case "tanh":
            return activations.tanh_derivative(value)
        case "identity":
            return activations.identity_derivative(value)
        case "step":
            return activations.step_derivative(value)

def meanSquareError(yOriginal, yPredicted):
    return ((yOriginal - yPredicted) ** 2)/2