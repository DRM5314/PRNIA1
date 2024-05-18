import controller.Operations as operations
class Controller:
    errors = []
    def __init__(self,service):
        self.training = service.training
        self.layers = service.layers
        self.iterations = service.iterations

    def forward(self,dataTraining):
        errorSum = 0
        for i in range(len(self.layers)):
            layer = self.layers[i]
            for j in range(len(layer.neurons)):
                neuron = layer.neurons[j]
                if i == 0:
                    neuron.preFunctionZAnalice(dataTraining.entries, i, layer.functionActivation,self.layers)
                else:
                    layerP = self.layers[i-1]
                    neuron.preFunctionZAnalice(layerP, i, layer.functionActivation,self.layers)
                if layer.endLayer:
                    error = operations.meanSquareError(dataTraining.output,neuron.functionActivation)
                    print(f"Expected: {dataTraining.showEntries()}, result: {neuron.functionActivation}, error is: {error}")
                    errorSum += error
        return errorSum

    def backward(self,expectation,entries):
        for i,layer in enumerate(reversed(self.layers)):
            print(f"\t\tChange W In layer {(len(self.layers)-1) - i}")
            neurons = layer.neurons
            for j, neuron in enumerate(neurons):
                if i == 0:
                    neuron.error = (expectation - neuron.functionActivation) * neuron.functionActivationDerivated
                else:
                    preEnd = len(self.layers) - i
                    nextLayer = self.layers[preEnd]
                    error_sum = sum(next_neuron.weights[j] * next_neuron.error for next_neuron in nextLayer.neurons)
                    neuron.error = error_sum * neuron.functionActivationDerivated

                if not layer.initLayer:
                    activationPrev = (len(self.layers) - 2) - i
                    neuronPrev = self.layers[activationPrev].neurons
                    for i3 in range(len(neuron.weights)):
                        preActivation = neuronPrev[i3].functionActivation
                        neuron.weights[i3] = neuron.weights[i3] + (neuron.error * preActivation*0.2)
                if layer.initLayer:
                    for i2 in range(len(neuron.weights)):
                        neuron.weights[i2] = neuron.weights[i2] + (neuron.error * entries[i2] * 0.2)
                neuron.umbral = neuron.umbral - (0.2*neuron.error)


    def showInfoLayers(self):
        out = ""
        for j,layer in enumerate(self.layers):
            neurons = layer.neurons
            out += f"\t\t\t\t\t\t\t\tIn layer {j}:\n"
            for i, neuron in enumerate(neurons):
                out += f"N{i} :\n"
                for j, weights in enumerate(neuron.weights):
                    out += f"W{j} : {weights}\n"
                out +=f"Sesgo is: {neuron.umbral}\n\n"
        return out
    def run(self):
        count = 0
        while count <= self.iterations:
            print(f"--------------------------------------------- Iteration: {count} -------------------------------------------\n")
            errorSum = 0
            for training in self.training:
                errorSum += self.forward(training)
                print("Aplication backForward........")
                self.backward(training.output,training.entries)
            self.errors.append(errorSum)
            print(f"\nError: {errorSum}\n")
            print(self.showInfoLayers())
            if errorSum == 0:
                print("Solution is find!!")
            count += 1

