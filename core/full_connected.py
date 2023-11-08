import random

from library import *


class FullConnected:
    def __init__(self, size,
                 activation=None,
                 loss=MSE(),
                 learning_rate=0.5,
                 momentum=0.3
                 ):

        self.size = size

        self.activation = activation
        if self.activation is None:
            self.activation = [ReLU() for i in range(len(size) - 1)] + [SoftMax()]

        self.loss = loss

        self.learning_rate = learning_rate
        self.momentum = momentum

        self.x = [[0 for j in range(self.size[i])] for i in range(len(self.size))]
        self.w = [[[random.uniform(-0.5, 0.5) for l in range(self.size[i + 1])] for j in range(self.size[i])] for i in range(len(self.size) - 1)]
        self.bias = [[random.uniform(-0.5, 0.5) for j in range(self.size[i + 1])] for i in range(len(self.size) - 1)]

    def define_err(self):
        self.err = [[0 for j in range(self.size[i])] for i in range(len(self.size))]
        self.delta_w = [[[0 for l in range(self.size[i + 1])] for j in range(self.size[i] + 1)] for i in range(len(self.size) - 1)]
        self.delta_bias = [[0 for j in range(self.size[i + 1])] for i in range(len(self.size) - 1)]

    def forward(self, data_input, dropout=False):
        for i in range(len(data_input)):
            self.x[0][i] = data_input[i]

        for i in range(len(self.size) - 1):
            for l in range(self.size[i + 1]):
                self.x[i + 1][l] = self.bias[i][l]
                for j in range(self.size[i]):
                    self.x[i + 1][l] += self.x[i][j] * self.w[i][j][l]

                if i + 1 < len(self.size) - 1 or self.activation[-1].__class__ != SoftMax:
                    self.x[i + 1][l] = self.activation[i + 1].f(self.x[i + 1][l])

        if self.activation[-1].__class__ == SoftMax:
            self.x[-1] = self.activation[-1].f(self.x[-1])

    def backward(self, data_output):
        for i in range(len(data_output)):
            self.err[-1][i] = self.loss.df(data_output[i], self.x[-1][i]) * self.activation[-1].df(self.x[-1][i])

        for i in range(len(self.size) - 2, -1, -1):
            for j in range(self.size[i]):
                self.err[i][j] = 0
                for l in range(self.size[i + 1]):
                    self.err[i][j] += self.err[i + 1][l] * self.w[i][j][l] * self.activation[i].df(self.x[i][j])

        for i in range(len(self.size) - 1):
            for j in range(self.size[i + 1]):
                for l in range(self.size[i]):
                    self.delta_w[i][l][j] = -self.learning_rate * self.x[i][l] * self.err[i + 1][j] + self.momentum * self.delta_w[i][l][j]
                    self.w[i][l][j] += self.delta_w[i][l][j]

                self.delta_bias[i][j] = -self.learning_rate * self.err[i + 1][j] + self.momentum * self.delta_bias[i][j]
                self.bias[i][j] += self.delta_bias[i][j]
