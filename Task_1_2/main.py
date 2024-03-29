from tkinter import *

import numpy as np

from Task_1_2.AdaLinealgorithm import AdaLine
from Task_1_2.DrawData import DrawData
from Task_1_2.FileData import FileData
from Task_1_2.ReadData import ReadData
from Task_1_2.Testing import Testing
from Task_1_2.TrainingModel import TrainingModel


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


def drawError():
    Label(root, text="Error: ").grid(row=6, column=0, sticky=W, padx=20, pady=20)
    error_input.grid(row=6, column=1)


def drawCheckBoxBias():
    C1 = Checkbutton(root, text="Bias", variable=CheckBias, onvalue=1, offvalue=0)
    C1.grid(row=7, column=0, sticky=W, padx=20, pady=20)


def Training():
    featureX, featureY, ClassLabel = rd1.GUIData(idxFeature(tkdropdownFeature1.get()),
                                                 idxFeature(tkdropdownFeature2.get()),
                                                 idxClass(tkdropdownClass1.get()), idxClass(tkdropdownClass2.get()))
    w1, w2, b = adaLine_algo.AdaLinealgorithm(featureX, featureY, ClassLabel, float(learning_rate_input.get()),
                                              float(number_epochs_input.get()), int(CheckBias.get()),
                                              float(error_input.get()))
    trainModel.set_w1(w1)
    trainModel.set_w2(w2)
    trainModel.set_b(b)

    f1 = int(np.max(featureX))
    f2 = int(np.max(featureY))
    Xmax = max(f1, f2)
    f1 = int(np.min(featureX))
    f2 = int(np.min(featureY))
    Xmin = min(f1, f2)
    dr.line(Xmin, Xmax, w1, w2, b)
    dr.plot(rd.Feature[idxFeature(tkdropdownFeature1.get())], rd.Feature[idxFeature(tkdropdownFeature2.get())])
    dr.draw()


def Test():
    featureX, featureY, ClassLabel = rd1.TestingData(idxFeature(tkdropdownFeature1.get()),
                                                     idxFeature(tkdropdownFeature2.get()),
                                                     idxClass(tkdropdownClass1.get()), idxClass(tkdropdownClass2.get()))
    test = Testing()
    test.testingAdaline(featureX, featureY, ClassLabel, trainModel.get_w1(), trainModel.get_w2(), trainModel.get_b())


def Plotting():
    for i in range(0, 4):
        for j in range(i + 1, 4):
            dr.plot1(rd.Feature[i], rd.Feature[j])
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
root.geometry("500x500")
root.title("Single Layer AdaLine Task2")

features = ['X1', 'X2', 'X3', 'X4']
classes = ['C1', 'C2', 'C3']

# init GUI
tkdropdownFeature1 = StringVar()
tkdropdownFeature2 = StringVar()
tkdropdownClass1 = StringVar()
tkdropdownClass2 = StringVar()
learning_rate_input = Entry(root)
number_epochs_input = Entry(root)
error_input = Entry(root)
CheckBias = IntVar()

# read Data
rd = FileData()
rd.fileData()
rd1 = ReadData()

# plot Data
dr = DrawData()

# training model
trainModel = TrainingModel()

# init AdaLine
adaLine_algo = AdaLine()

# Drawing GUI
drawFeature1()
drawFeature2()
drawClass1()
drawClass2()
drawLearningRate()
drawNumberEpochs()
drawError()
drawCheckBoxBias()

# init Buttons
Button(root, text='Training', command=Training).grid(row=8, column=0, sticky=W, padx=20, pady=20)
Button(root, text='Test', command=Test).grid(row=8, column=1, sticky=W, padx=20, pady=20)
Button(root, text='Plotting', command=Plotting).grid(row=8, column=2, sticky=W, padx=20, pady=20)

root.mainloop()
