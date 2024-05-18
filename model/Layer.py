from model.Perceptron import Perceptron
class Layer:
    neurons = None
    functionActivation = None
    endLayer = False
    initLayer = False
    def __init__(self,neurons,functionActivation):
        self.neurons = []
        for i in range(neurons):
            self.neurons.append(Perceptron())
        self.functionActivation = self.typeActivation(functionActivation)

    def typeActivation (self,type):
        match type:
            case 1:
                return "sigmode"
            case 2:
                return "tanh"
            case 3:
                return "step"
            case 4:
                return "identity"