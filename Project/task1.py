from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Single Layer Perceptron Task1")

features = ['X1', 'X2', 'X3', 'X4']
classes = ['C1', 'C2', 'C3']

tkdropdownFeature1 = StringVar()
tkdropdownFeature2 = StringVar()
tkdropdownClass1 = StringVar()
tkdropdownClass2 = StringVar()
learning_rate_input = Entry(root)
number_epochs_input = Entry(root)
CheckBias = IntVar()


def drawFeature1():
    tkdropdownFeature1.set('X1')
    Label(root, text="Choose a first feature").grid(row=0, column=0, sticky=W, padx=20, pady=20)
    OptionMenu(root, tkdropdownFeature1, *features).grid(row=0, column=1)


def drawFeature2():
    tkdropdownFeature2.set('X1')
    Label(root, text="Choose a second feature").grid(row=1, column=0, sticky=W, padx=20, pady=20)
    OptionMenu(root, tkdropdownFeature2, *features).grid(row=1, column=1)


def drawClass1():
    tkdropdownClass1.set('C1')
    Label(root, text="Choose a first class").grid(row=2, column=0, sticky=W, padx=20, pady=20)
    OptionMenu(root, tkdropdownClass1, *classes).grid(row=2, column=1)


def drawClass2():
    tkdropdownClass2.set('C1')
    Label(root, text="Choose a second class").grid(row=3, column=0, sticky=W, padx=20, pady=20)
    OptionMenu(root, tkdropdownClass2, *classes).grid(row=3, column=1)


def drawLearningRate():
    Label(root, text="Learning rate: ").grid(row=4, column=0, sticky=W, padx=20, pady=20)
    learning_rate_input.grid(row=4, column=1)


def drawNumberEpochs():
    Label(root, text="Number of epochs: ").grid(row=5, column=0, sticky=W, padx=20, pady=20)
    number_epochs_input.grid(row=5, column=1)


def drawCheckBoxBias():
    C1 = Checkbutton(root, text="Bias", variable=CheckBias, onvalue=1, offvalue=0)
    C1.grid(row=6, column=0, sticky=W, padx=20, pady=20)


def showJustForTest(*args):
    print("Feature1: " + tkdropdownFeature1.get())
    print("Feature2: " + tkdropdownFeature2.get())
    print("Class1: " + tkdropdownClass1.get())
    print("Class2: " + tkdropdownClass2.get())
    print("Learning Rate: " + learning_rate_input.get())
    print("Number of epochs: " + number_epochs_input.get())
    print("Check Bias: " + str(CheckBias.get()))


def Training(*args):
    return


def Test(*args):
    return


def Plotting(*args):
    return


drawFeature1()
drawFeature2()
drawClass1()
drawClass2()
drawLearningRate()
drawNumberEpochs()
drawCheckBoxBias()

Button(root, text='Training', command=Training).grid(row=7, column=0, sticky=W, padx=20, pady=20)
Button(root, text='Test', command=Test).grid(row=7, column=1, sticky=W, padx=20, pady=20)
Button(root, text='Plotting', command=Plotting).grid(row=7, column=2, sticky=W, padx=20, pady=20)

# Button(root, text='Show', command=showJustForTest).grid(row=8, column=1, sticky=W, padx=20, pady=20)

root.mainloop()
