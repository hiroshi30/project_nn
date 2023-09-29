from library import *

class FullConnected:
    def __init__(self, size):
        self.x = None
        self.err = None

        self.size = size

        self.activation = Sigmoid()
        self.loss = MSE()

        self.w = [[[uniform(-1, 1) for l in range(self.size[i + 1])] for j in range(self.size[i])] for i in range(len(self.size) - 1)]
        self.delta_w = [[[0 for l in range(self.size[i + 1])] for j in range(self.size[i] + 1)] for i in range(len(self.size) - 1)]

        self.bias = [[uniform(-1, 1) for j in range(self.size[i + 1])] for i in range(len(self.size) - 1)]
        self.delta_bias = [[0 for j in range(self.size[i + 1])] for i in range(len(self.size) - 1)]

    def forward(self, data_input):
        self.x = [[0 for j in range(self.size[i])] for i in range(len(self.size))]
        self.x[0] = [*data_input]

        for i in range(len(self.size) - 1):
            for j in range(self.size[i + 1]):
                for l in range(self.size[i]):
                    self.x[i + 1][j] += self.x[i][l] * self.w[i][l][j]
                self.x[i + 1][j] += self.bias[i][j]
                if i != len(self.size) - 2:
                    self.x[i + 1][j] = self.activation.f(self.x[i + 1][j])
        self.x[-1] = SoftMax().f(self.x[-1])

    def backward(self, data_output, n=0.7, m=0.5):
        self.err = [[0 for _1 in range(self.size[i])] for i in range(len(self.size))]

        for i in range(len(data_output)):
            self.err[-1][i] = self.loss.df(data_output[i], self.x[-1][i]) * SoftMax().df(self.x[-1][i])

        for i in range(len(self.size) - 2, 0, -1):
            for j in range(self.size[i]):
                for l in range(self.size[i + 1]):
                    self.err[i][j] += self.err[i + 1][l] * self.w[i][j][l] * self.activation.df(self.x[i][j])

        print(f'err = {self.err}')

        for i in range(len(self.size) - 1):
            for j in range(self.size[i + 1]):
                for l in range(self.size[i]):
                    self.delta_w[i][l][j] = -n * self.x[i][l] * self.err[i + 1][j] + m * self.delta_w[i][l][j]
                    self.w[i][l][j] += self.delta_w[i][l][j]

                self.delta_bias[i][j] = -n * self.err[i + 1][j] + m * self.delta_bias[i][j]
                self.bias[i][j] += self.delta_bias[i][j]
        
        print(f'w = {self.w}\ndelta_w = {self.delta_w}\nbias = {self.bias}\ndelta_bias = {self.delta_bias}')