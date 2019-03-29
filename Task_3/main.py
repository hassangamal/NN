from tkinter import *


def drawNumberHiddenLayers():
    Label(root, text="Number of hidden layers: ").grid(row=1, column=0, sticky=W, padx=20, pady=20)
    number_hidden_layers_input.grid(row=1, column=1)


def drawNumberNeuronEachHiddenLayer():
    Label(root, text="Number of neurons in each hidden layer: ").grid(row=2, column=0, sticky=W, padx=20, pady=20)
    number_neurons_each_hidden_layer_input.grid(row=2, column=1)


def drawLearningRate():
    Label(root, text="Learning rate: ").grid(row=3, column=0, sticky=W, padx=20, pady=20)
    learning_rate_input.grid(row=3, column=1)


def drawNumberEpochs():
    Label(root, text="Number of epochs: ").grid(row=4, column=0, sticky=W, padx=20, pady=20)
    number_epochs_input.grid(row=4, column=1)


def drawCheckBoxBias():
    C1 = Checkbutton(root, text="Bias", variable=CheckBias, onvalue=1, offvalue=0)
    C1.grid(row=5, column=0, sticky=W, padx=20, pady=20)


def drawDropDownActivationFunctions():
    tkDropDownActivationFunctions.set('Sigmoid')
    Label(root, text="Choose the Activation Function").grid(row=6, column=0, sticky=W, padx=20, pady=20)
    OptionMenu(root, tkDropDownActivationFunctions, *activationFunctions).grid(row=6, column=1)


def Training():
    return


def Test():
    return


root = Tk()
root.geometry("500x500")
root.title("BackPropagation Algorithm Task3")

activationFunctions = ['Sigmoid', 'Hyperbolic']

number_hidden_layers_input = Entry(root)
number_neurons_each_hidden_layer_input = Entry(root)
learning_rate_input = Entry(root)
number_epochs_input = Entry(root)
CheckBias = IntVar()
tkDropDownActivationFunctions = StringVar()

drawNumberHiddenLayers()
drawNumberNeuronEachHiddenLayer()
drawLearningRate()
drawNumberEpochs()
drawCheckBoxBias()
drawDropDownActivationFunctions()

Button(root, text='Training', command=Training).grid(row=8, column=0, sticky=W, padx=20, pady=20)
Button(root, text='Test', command=Test).grid(row=8, column=1, sticky=W, padx=20, pady=20)

root.mainloop()
