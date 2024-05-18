import random
import controller.Operations as operations

class Perceptron:
    functionZ = None
    functionActivation = None
    functionZDerivate = None
    functionActivationDerivated = None

    error = None

    weights = None
    umbral = None
    typeActivation = None

    def preFunctionZAnalice(self, entries, position, typeActivation,layers):
        result = 0
        if position == 0:
            self.evaluateWeights(entries)
            for i in range(len(entries)):
                preResult = entries[i] * self.weights[i]
                result += preResult
        else:
            self.evaluateWeights(entries.neurons)
            neuronsAnt = layers[position-1].neurons
            for i in range(len(neuronsAnt)):
                activation = neuronsAnt[i].functionActivation
                preResult = activation * self.weights[i]
                result += preResult
        # Sesgo!
        self.functionZ = result - self.umbral
        self.functionActivation = self.activationFunction(typeActivation)
        self.functionActivationDerivated = self.activationFunctionDerivated(typeActivation)

    def randomWights(self,numberEntrys):
        self.weights = []
        for i in range(len(numberEntrys)):
            randomValue = random.random()
            for i in range(5):
                randomValue = random.random()
            self.weights.append(round(randomValue,3))
            self.umbral = round(random.random(),3)

    def activationFunction(self,typeActivation):
        if typeActivation is not None:
            return operations.activation_function(typeActivation,self.functionZ)

    def activationFunctionDerivated(self,typeActivation):
        if typeActivation is not None:
            return operations.activation_function_derivated(typeActivation,self.functionZ)

    def evaluateWeights(self,entries):
        if self.functionZ is None:
            self.randomWights(entries)

