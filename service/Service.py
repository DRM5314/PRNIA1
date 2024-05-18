import validations.Validations as Validations
from model.Layer import Layer
from model.Training import Training
class Service:
    layers = None
    entries = None
    training = None
    iterations = None
    def askPamateters(self):
        print("\n1.Entradas   2.Capas ocultas     3.Capas de salida\n")
        value = Validations.askNumber()

    def initProgram(self):
        print("\nEntry number of entry:")
        self.entries = Validations.askNumber()
        print("\nEntry number of layers (included output layer) :")
        layers = Validations.askNumber()
        self.layers = self.createLayers(layers)
    def createLayers(self,numberLayers):
        if numberLayers <= 0:
            return None
        layers = []
        for i in range(numberLayers):
            print(f"\nIn layer # {i}, insert number of neurons:")
            neurons = Validations.askNumber()

            if i == numberLayers - 1:
                print("\n\nConfigure layer out!!\n\n")
                print(f"In final layer (OUT) select activation 1:Step(Default) 2:Identity")
                activation = Validations.askNumber()
                if activation == 2:
                    activation = 4
                    print("Step")
                else:
                    activation = 3
                layers.append(Layer(neurons, activation))
                layers[i].endLayer = True
                break

            print(f"\nInsert type of activation in layer #{i}, 1:Sigmode(Default) 2:hyperbolic tangent")
            activation = Validations.askNumber()
            if activation == 2:
                print("Select hyperbolic tangent")
            else:
                activation = 1
                print("Select sigmode")
            print("\n")
            layers.append(Layer(neurons,activation))
            if i == 0:
                layers[i].initLayer = True
        print("\n\nEnd configuration!")
        return layers

    def trainingTickets(self):
        trainingTickets = []
        print("\nInsert # of training tickets")
        numberTraining = Validations.askNumber()
        print("\n\n\n--------------------------------- ")
        print("\nPlease for the following inputs, you have to enter the input values and the expected value [X1,...XN] next [Expected]")
        for i in range(numberTraining):
            trainingActually = []
            for j in range(self.entries):
                print(f"\nInsert value for X{j} for training #{i}")
                trainingActually.append(Validations.askNumber())
            print("\nInsert value expected")
            expected = Validations.askNumber()
            trainingTickets.append(Training(trainingActually,expected))
            print(self.showTrainingTickets(trainingTickets))
        print("\nEnd of training entries.....\n")
        self.training = trainingTickets
        return trainingTickets

    def showTrainingTickets(self,trainingTickets):
        out = ""
        for entry in trainingTickets:
            entries = entry.entries
            for entries in entries:
                out += (f"{entries}  ")
            out += f":{entry.output}\n"
        return out
    def askIterations(self):
        print("\nInsert number of iterations:")
        numberIterations = Validations.askNumber()
        self.iterations = numberIterations
        print("Iterations configured!")
        return numberIterations

