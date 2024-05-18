from service.Service import Service
import matplotlib.pyplot as plt
class View:
    service = Service()
    def setConfiguration(self):
        print("Edit configuration: \n")

    def initialConfiguration(self):
        self.service.initProgram()

    def traininfTickets(self):
        self.service.trainingTickets()

    def askIterations(self):
        return self.service.askIterations()

    def showErrors(self,errors):
        # errors = errors[10:]
        x = range(len(errors))
        plt.plot(x,errors,marker='o',linestyle='-', color='b', label='Valores')
        plt.title("Errors vs Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Error")
        plt.legend()
        plt.show()
