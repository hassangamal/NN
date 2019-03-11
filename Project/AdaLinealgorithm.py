import numpy as np


class AdaLine:
    def __init__(self):
        pass

    def AdaLinealgorithm(self, featureX, featureY, classlabel, eta, m, bias,erroTh):

        global w1, w2, b
        epoch = 0
        errorMSE=0,
        weights = [np.random.rand(1)[0], np.random.rand(1)[0], np.random.rand(1)[0]]

        while epoch < m:

            for i in range(0, len(featureX)):
                out = self.net_input([featureX[i], featureY[i]], weights, bias)

                d = classlabel[i]

                error = d - out

                weights[0] = weights[0] + eta * error
                weights[1] = weights[1] + eta * error * featureX[i]
                weights[2] = weights[2] + eta * error * featureY[i]

            errorMSE = self.Updateerror(featureX, featureY, classlabel,weights, bias)
            w1 = weights[1]
            w2 = weights[2]
            b = weights[0] * bias
            epoch = epoch + 1
            if errorMSE < erroTh:
                break
        print(errorMSE)
        return (w1, w2, b)

    def Updateerror(self,featureX, featureY, classlabel, weights, bias):
        RES=0
        for i in range(0, len(featureX)):
            out = self.net_input([featureX[i], featureY[i]], weights, bias)

            d = classlabel[i]

            error = d - out
            ANS= (error**2)/2
            RES=RES+ANS
        MSE = RES/(len(featureX))
        return  MSE
    def net_input(self, Input, weight, bias):
        output = bias * weight[0] + weight[1] * Input[0] + weight[2] * Input[1]
        return output