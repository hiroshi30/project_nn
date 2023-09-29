import random

from library import *


class Convolution:
    def __init__(self, channels, height, width,
                 matrix_c=3,
                 matrix_h=3,
                 matrix_w=3,
                 padding=1,
                 stride_h=1,
                 stride_w=1,
                 activation=ReLU(),
                 learning_rate=0.7,
                 momentum=0.5
                 ):

        self.channels = channels
        self.height = height + 2 * padding
        self.width = width + 2 * padding

        self.padding = padding

        self.matrix_c = matrix_c
        self.matrix_h = matrix_h
        self.matrix_w = matrix_w

        self.stride_h = stride_h
        self.stride_w = stride_w

        self.activation = activation
        self.learning_rate = learning_rate
        self.momentum = momentum

        self.data_input = []
        for c in range(self.channels):
            self.data_input.append([])
            for h in range(self.height):
                self.data_input[c].append([])
                for w in range(self.width):
                    self.data_input[c][h].append(0)

        self.x = []
        for mc in range(self.matrix_c):
            self.x.append([])
            for hh in range(1 + (self.height - self.matrix_h) // self.stride_h):
                self.x[mc].append([])
                for ww in range(1 + (self.width - self.matrix_w) // self.stride_w):
                    self.x[mc][hh].append(0)

        self.w = []
        for mc in range(self.matrix_c):
            self.w.append([])
            for c in range(self.channels):
                self.w[mc].append([])
                for mh in range(self.matrix_h):
                    self.w[mc][c].append([])
                    for mw in range(self.matrix_w):
                        self.w[mc][c][mh].append(random.uniform(-1, 1))

        self.bias = []
        for mc in range(self.matrix_c):
            self.bias.append([])
            for hh in range(1 + (self.height - self.matrix_h) // self.stride_h):
                self.bias[mc].append([])
                for ww in range(1 + (self.width - self.matrix_w) // self.stride_w):
                    self.bias[mc][hh].append(random.uniform(-1, 1))

    def define_err(self):
        self.err = []
        for c in range(self.channels):
            self.err.append([])
            for hp in range(self.height - 2 * self.padding):
                self.err[c].append([])
                for wp in range(self.width - 2 * self.padding):
                    self.err[c][hp].append(0)

        self.delta_w = []
        for mc in range(self.matrix_c):
            self.delta_w.append([])
            for c in range(self.channels):
                self.delta_w[mc].append([])
                for mh in range(self.matrix_h):
                    self.delta_w[mc][c].append([])
                    for mw in range(self.matrix_w):
                        self.delta_w[mc][c][mh].append(0)

        self.delta_bias = []
        for mc in range(self.matrix_c):
            self.delta_bias.append([])
            for hh in range(1 + (self.height - self.matrix_h) // self.stride_h):
                self.delta_bias[mc].append([])
                for ww in range(1 + (self.width - self.matrix_w) // self.stride_w):
                    self.delta_bias[mc][hh].append(0)

    def forward(self, data_input):
        for c in range(self.channels):
            for hp in range(self.height - 2 * self.padding):
                for wp in range(self.width - 2 * self.padding):
                    self.data_input[c][self.padding + hp][self.padding + wp] = data_input[c][hp][wp]

        for mc in range(self.matrix_c):
            for hh in range(1 + (self.height - self.matrix_h) // self.stride_h):
                for ww in range(1 + (self.width - self.matrix_w) // self.stride_w):
                    self.x[mc][hh][ww] = self.bias[mc][hh][ww]
                    for c in range(self.channels):
                        for mh in range(self.matrix_h):
                            for mw in range(self.matrix_w):
                                self.x[mc][hh][ww] += self.data_input[c][hh * self.stride_h + mh][ww * self.stride_w + mw] * self.w[mc][c][mh][mw]
                    self.x[mc][hh][ww] = self.activation.f(self.x[mc][hh][ww])

    def backward(self, err):
        for mc in range(self.matrix_c):
            for c in range(self.channels):
                for mh in range(self.matrix_h):
                    for mw in range(self.matrix_w):
                        self.delta_w[mc][c][mh][mw] *= self.momentum

        for mc in range(self.matrix_c):
            for hh in range(1 + (self.height - self.matrix_h) // self.stride_h):
                for ww in range(1 + (self.width - self.matrix_w) // self.stride_w):
                    for c in range(self.channels):
                        for mh in range(self.matrix_h):
                            for mw in range(self.matrix_w):
                                self.delta_w[mc][c][mh][mw] += -self.learning_rate * self.data_input[c][hh * self.stride_h + mh][ww * self.stride_w + mw] * err[mc][hh][ww]
                    self.delta_bias[mc][hh][ww] = -self.learning_rate * err[mc][hh][ww] + self.momentum * self.delta_bias[mc][hh][ww]
                    self.bias[mc][hh][ww] += self.delta_bias[mc][hh][ww]

        for mc in range(self.matrix_c):
            for c in range(self.channels):
                for mh in range(self.matrix_h):
                    for mw in range(self.matrix_w):
                        self.w[mc][c][mh][mw] += self.delta_w[mc][c][mh][mw]

        for c in range(self.channels):
            for hp in range(self.height - 2 * self.padding):
                for wp in range(self.width - 2 * self.padding):
                    self.err[c][hp][wp] = 0

        for mc in range(self.matrix_c):
            for hh in range(1 + (self.height - self.matrix_h) // self.stride_h):
                for ww in range(1 + (self.width - self.matrix_w) // self.stride_w):
                    for c in range(self.channels):
                        for mh in range(self.matrix_h):
                            for mw in range(self.matrix_w):
                                if self.padding <= hh * self.stride_h + mh < self.height - self.padding:
                                    if self.padding <= ww * self.stride_w + mw < self.width - self.padding:
                                        self.err[c][hh * self.stride_h + mh - self.padding][ww * self.stride_w + mw - self.padding] += err[mc][hh][ww] * self.w[mc][c][mh][mw]  # * self.activation.df(self.x[mc][hh][ww])
