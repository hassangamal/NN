import numpy as np

class Perceptron:
    def __init__(self):
        pass

    def Perceptronalgorithm(self,featureX,featureY,classlabel,eta,m,bias):

        epoch = 0
        weights = [np.random.rand(1)[0], np.random.rand(1)[0], np.random.rand(1)[0]]

        while epoch < m:

            for i in range(0,len(featureX)+len(featureY)):

                out = self.net_input([featureX[i],featureY[i]],weights,bias)
                y = self.predict(out)
                d=classlabel[i]

                '''
                if d == y:
                    d = 1
                else:
                    d = -1
                '''

                error = d - y

                weights[0] = weights[0] + eta * error
                weights[1] = weights[1] + eta * error * featureX[i]
                weights[2] = weights[2] + eta * error * featureY[i]

            w1 = weights[1]
            w2 = weights[2]
            b = weights[0] * bias
            epoch = epoch + 1
        print(w1, w2, b)
        return (w1,w2,b)

    def net_input(self, Input, weight, bias):
        output = bias * weight[0] + weight[1] * Input[0] + weight[2] * Input[1]
        return output

    def predict(self,out):
        if(out>=0.0):
            return 1
        return -1