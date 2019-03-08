from tkinter import *

from Project.DrawData import DrawData
from Project.FileData import FileData
from Project.Perceptronalgorithm import Perceptron
from Project.ReadData import ReadData


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


def Training():
    featureX, featureY, ClassLabel = rd1.GuiData(idxFeature(tkdropdownFeature1.get()),
                                                 idxFeature(tkdropdownFeature2.get()),
                                                 idxClass(tkdropdownClass1.get()), idxClass(tkdropdownClass2.get()))
    w1, w2, b = perceptron_algo.Perceptronalgorithm(featureX, featureY, ClassLabel, float(learning_rate_input.get()),
                                                    float(number_epochs_input.get()), int(CheckBias.get()))


def Test():
    return


def Plotting():
    dr.plot(rd.Feature[idxFeature(tkdropdownFeature1.get())], rd.Feature[idxFeature(tkdropdownFeature2.get())])
    dr.draw()


def idxFeature(_feature):
    if _feature == 'X1':
        return 0
    elif _feature == 'X2':
        return 1
    elif _feature == 'X3':
        return 2
    elif _feature == 'X4':
        return 3


def idxClass(_class):
    if _class == 'C1':
        return 1
    elif _class == 'C2':
        return 2
    elif _class == 'C3':
        return 3


root = Tk()
root.geometry("1000x500")
root.title("Single Layer Perceptron Task1")

features = ['X1', 'X2', 'X3', 'X4']
classes = ['C1', 'C2', 'C3']

# init GUI
tkdropdownFeature1 = StringVar()
tkdropdownFeature2 = StringVar()
tkdropdownClass1 = StringVar()
tkdropdownClass2 = StringVar()
learning_rate_input = Entry(root)
number_epochs_input = Entry(root)
CheckBias = IntVar()

# read Data
rd = FileData()
rd.fileData()
rd1 = ReadData()

# plot Data
dr = DrawData()

# init Perceptron
perceptron_algo = Perceptron()

# Drawing GUI
drawFeature1()
drawFeature2()
drawClass1()
drawClass2()
drawLearningRate()
drawNumberEpochs()
drawCheckBoxBias()

# init Buttons
Button(root, text='Training', command=Training).grid(row=7, column=0, sticky=W, padx=20, pady=20)
Button(root, text='Test', command=Test).grid(row=7, column=1, sticky=W, padx=20, pady=20)
Button(root, text='Plotting', command=Plotting).grid(row=7, column=2, sticky=W, padx=20, pady=20)

root.mainloop()
