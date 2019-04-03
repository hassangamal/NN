import math

import numpy as np


class BackPropagation:
    def __init__(self):
        pass

    def BackPropagationalgorithm(self, featureX1, featureX2, featureX3, featureX4, classLabel, eta, epochs, bias,
                                 activation_function, num_hidden_layer, num_neurons_layer):
        if activation_function == "Sigmoid":
            activation_function = 1
        else:
            activation_function = 2

        weights, weights_inputs = self.initialize(num_hidden_layer, num_neurons_layer)
        # print(weights)
        # print(weights_inputs)

        for i in range(epochs):
            for j in range(len(featureX1)):
                input = [featureX1[j], featureX2[j],
                         featureX3[j], featureX4[j]]
                y = classLabel[j]

                weights_inputs = self.net_input(input, weights, weights_inputs,
                                                bias, num_hidden_layer,
                                                num_neurons_layer,
                                                activation_function)

                error = self.propagate_error(weights_inputs,
                                             num_hidden_layer,
                                             num_neurons_layer,
                                             y, activation_function)

                weights = self.update_weights(weights_inputs, weights, num_hidden_layer
                                              , num_neurons_layer, eta, error, bias, input)

        return weights, weights_inputs

    def net_input(self, X, weight, weights_inputs, bias, num_hidden_layer,
                  num_neurons_layer, activation_function):
        index = 1
        index_weight = 0
        for i in range(num_hidden_layer + 1):
            if i == 0:
                for j in range(num_neurons_layer):
                    Z = bias * weight[index][0] \
                        + X[0] * weight[index][1] \
                        + X[1] * weight[index][2] \
                        + X[2] * weight[index][3] \
                        + X[3] * weight[index][4]
                    Y = self.activate(activation_function, Z)
                    weights_inputs[index - 1] = Y
                    index += 1
            elif i == num_hidden_layer:
                for j in range(3):
                    Z = bias * weight[index][0]
                    for k in range(1, num_neurons_layer + 1):
                        Z += weights_inputs[index_weight + k - 1] * weight[index][k]

                    Y = self.activate(activation_function, Z)
                    weights_inputs[index - 1] = Y
                    index += 1
            else:
                for j in range(num_neurons_layer):
                    Z = bias * weight[index][0]
                    for k in range(1, num_neurons_layer + 1):
                        Z += weights_inputs[index_weight + k - 1] * weight[index][k]
                    Y = self.activate(activation_function, Z)
                    weights_inputs[index - 1] = Y
                    index += 1
                index_weight += num_neurons_layer
        return weights_inputs

    def propagate_error(self, weights_inputs, num_hidden_layer,
                        num_neurons_layer, y, activation_function):
        error = [0] * len(weights_inputs)
        index = len(weights_inputs) - 1
        for i in reversed(range(num_hidden_layer + 1)):
            if i != num_hidden_layer:
                for j in range(num_neurons_layer):
                    sum = 0.0
                    if i + 1 == num_hidden_layer:
                        for k in range(3):
                            sum += weights_inputs[(i + 1) * num_neurons_layer + k] * error[
                                (i + 1) * num_neurons_layer + k]
                    else:
                        for k in range(num_neurons_layer):
                            sum += weights_inputs[(i + 1) * num_neurons_layer + k] * error[
                                (i + 1) * num_neurons_layer + k]
                    error[index] = sum * self.drivative(activation_function, weights_inputs[index])
                    index -= 1

            else:
                for j in range(3):
                    y = y - weights_inputs[index]
                    error[index] = y * self.drivative(activation_function, weights_inputs[index])
                    index -= 1

        return error

    def update_weights(self, weights_inputs, weight, num_hidden_layer
                       , num_neurons_layer, eta, error, bias, X):
        index = len(weight)
        index_WInput = len(weights_inputs) - 4
        index_error = len(error) - 1
        for i in reversed(range(num_hidden_layer + 1)):
            # output layer weights
            if i == num_hidden_layer:
                for j in reversed(range(3)):
                    for k in reversed(range(num_neurons_layer + 1)):
                        if k == 0:
                            weight[index][k] = eta * bias * error[index_error]
                        else:
                            weight[index][k] = eta * weights_inputs[index_WInput] * error[index_error]
                            index_WInput -= 1
                    index -= 1
                    index_WInput += num_neurons_layer
                    index_error -= 1
            elif i == 0:
                for j in reversed(range(num_neurons_layer)):
                    for k in reversed(range(5)):
                        if k == 0:
                            weight[index][k] = eta * bias * error[index_error]
                        else:
                            weight[index][k] = eta * X[k - 1] * error[index_error]
                    index -= 1
                    index_error -= 1
            else:
                index_WInput -= num_neurons_layer

                for j in range(num_neurons_layer):
                    for k in reversed(range(num_neurons_layer + 1)):
                        if k == 0:
                            weight[index][k] = eta * bias * error[index_error]
                        else:
                            # if index_error < 0:
                            #     print("err ", index_error)
                            weight[index][k] = eta * weights_inputs[index_WInput] * error[index_error]
                            index_WInput -= 1
                    index -= 1
                    index_WInput += num_neurons_layer
                    index_error -= 1
        return weight

    def initialize(self, num_hidden_layer, num_neurons_layer):
        weights = {}
        weights_inputs = []
        index = 1
        for i in range(num_hidden_layer + 1):
            if i == 0:
                for j in range(num_neurons_layer):
                    weights[index] = [np.random.rand(1)[0] for k in range(5)]
                    weights_inputs.append(0)
                    index += 1
            elif i == num_hidden_layer:
                for j in range(3):
                    weights[index] = [np.random.rand(1)[0] for k in range(num_neurons_layer + 1)]
                    weights_inputs.append(0)
                    index += 1
            else:
                for j in range(int(num_neurons_layer)):
                    weights[index] = [np.random.rand(1)[0] for k in range(num_neurons_layer + 1)]
                    weights_inputs.append(0)
                    index += 1
        return weights, weights_inputs

    def drivative(self, activation_function, x):
        if activation_function == 1:
            return self.sigmoid_derivative(x)
        else:
            return self.Hyperbolic_tangent_derivative(x)

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def Hyperbolic_tangent_derivative(self, x):
        return 1 - np.power(np.tanh(x), 2)

    def activate(self, activation_function, x):
        if activation_function == 1:
            return self.sigmoid(x)
        else:
            return self.Hyperbolic_tangent(x)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def Hyperbolic_tangent(self, x):
        return np.tanh(x)

    def BackPropagationalgorithmTesting(self, weightss, weights_inputss, featureX1, featureX2, featureX3, featureX4,
                                        bias, activation_function, num_hidden_layer, num_neurons_layer):
        res = []

        for j in range(len(featureX1)):
            # getting input vector
            input = [featureX1[j], featureX2[j],
                     featureX3[j], featureX4[j]]
            weights_inputs = self.net_input(input, weightss, weights_inputss,
                                            bias, num_hidden_layer,
                                            num_neurons_layer,
                                            activation_function)
            Length = len(weights_inputs)
            if weights_inputs[Length - 1] > weights_inputs[Length - 2] and \
                    weights_inputs[Length - 1] > weights_inputs[Length - 3]:
                res.append(1)
            elif weights_inputs[Length - 2] > weights_inputs[Length - 1] and \
                    weights_inputs[Length - 2] > weights_inputs[Length - 3]:
                res.append(2)
            else:
                res.append(3)
        return res
