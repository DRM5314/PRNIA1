from view.View import View
from controller.Controller import Controller
from model.Training import Training
view = View()
view.initialConfiguration()
# view.traininfTickets()
# view.askIterations()
training  = []
training.append(Training([0,0],0))
training.append(Training([0,1],1))
training.append(Training([1,0],1))
training.append(Training([1,1],0))
view.service.training = training
view.service.iterations = 100
controller = Controller(view.service)
controller.run()
view.showErrors(controller.errors)
