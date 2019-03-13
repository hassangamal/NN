import numpy as np

from Project.Perceptronalgorithm import Perceptron
from Project.AdaLinealgorithm import AdaLine


class Testing:
    def testingPerceptron(self, featureX, featureY, classLabel, w1, w2, bais):
        perceptron = Perceptron()
        res = np.zeros([2, 2], dtype='int32')
        for i in range(0, len(featureX)):
            y = perceptron.PerceptronalgorithmTest(featureX[i], featureY[i], w1, w2, bais)
            if y == 1 and classLabel[i] == 1:
                res[0, 0] = res[0, 0] + 1
            elif y == 1 and classLabel[i] == -1:
                res[1, 0] = res[1, 0] + 1
            elif y == -1 and classLabel[i] == 1:
                res[0, 1] = res[0, 1] + 1
            elif y == -1 and classLabel[i] == -1:
                res[1, 1] = res[1, 1] + 1

        print(res)
        print("Test of Success C1 = ", (res[0, 0] / 20) * 100)
        print("Test of Success C2 = ", (res[1, 1] / 20) * 100)
        print("Test of total = ", ((res[1, 1]+res[0, 0]) / 40) * 100)

    def testingAdaline(self, featureX, featureY, classLabel, w1, w2, bais):
        adaline = AdaLine()
        res = np.zeros([2, 2], dtype='int32')
        for i in range(0, len(featureX)):
            y = adaline.AdalinealgorithmTest(featureX[i], featureY[i], w1, w2, bais)
            if y == 1 and classLabel[i] == 1:
                res[0, 0] = res[0, 0] + 1
            elif y == 1 and classLabel[i] == -1:
                res[1, 0] = res[1, 0] + 1
            elif y == -1 and classLabel[i] == 1:
                res[0, 1] = res[0, 1] + 1
            elif y == -1 and classLabel[i] == -1:
                res[1, 1] = res[1, 1] + 1

        print(res)
        print("Test of Success C1 = ", (res[0, 0] / 20) * 100)
        print("Test of Success C2 = ", (res[1, 1] / 20) * 100)
        print("Test of total = ", ((res[1, 1]+res[0, 0]) / 40) * 100)

