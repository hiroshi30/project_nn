import os
import sys
import json
import time
import copy

sys.path.append(sys.path[-1] + os.sep + 'core')
print(sys.path)

from library import *
from full_connected import *
from convolution import *
from max_pooling import *
# from ensemble import *
from loader_images import *


os.system('color')

endc = '\033[0m'
reset = '\033[0m'
bold = '\033[01m'
disable = '\033[02m'
underline = '\033[04m'
reverse = '\033[07m'
strikethrough = '\033[09m'
invisible = '\033[08m'

black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'

# background
bg_black = '\033[40m'
bg_red = '\033[41m'
bg_green = '\033[42m'
bg_orange = '\033[43m'
bg_blue = '\033[44m'
bg_purple = '\033[45m'
bg_cyan = '\033[46m'
bg_lightgrey = '\033[47m'


class nn:
    def __init__(self, layers=[],
                 file_path=None,
                 debug=False
                 ):
        self.layers = layers

        self.file_path = file_path
        if self.file_path is None:
            self.file_path = '~' + os.sep + 'dt1.json'
        self.file_path = self.file_path.replace('~', sys.path[0])

        self.debug = debug

        self.epochs = 0

        self.error = 1
        self.error_min = 1
        self.error_start = 1

        self.data_min = []
        self.data_start = []

    def save(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            data = []
            for layer in self.layers:
                data.append(dict(type=layer.__class__.__name__))
                if layer.__class__ == FullConnected:
                    data[-1]['size'] = layer.size
                    data[-1]['learning_rate'] = layer.learning_rate
                    data[-1]['momentum'] = layer.momentum
                    data[-1]['activation'] = [i.__class__.__name__ for i in layer.activation]
                    data[-1]['loss'] = layer.loss.__class__.__name__
                    data[-1]['weights'] = layer.w
                    data[-1]['biases'] = layer.bias
                elif layer.__class__ == Convolution:
                    data[-1]['channels'] = layer.channels
                    data[-1]['height'] = layer.height - 2 * layer.padding
                    data[-1]['width'] = layer.width - 2 * layer.padding
                    data[-1]['matrix_c'] = layer.matrix_c
                    data[-1]['matrix_h'] = layer.matrix_h
                    data[-1]['matrix_w'] = layer.matrix_w
                    data[-1]['padding'] = layer.padding
                    data[-1]['stride_h'] = layer.stride_h
                    data[-1]['stride_w'] = layer.stride_w
                    data[-1]['activation'] = layer.activation.__class__.__name__
                    data[-1]['learning_rate'] = layer.learning_rate
                    data[-1]['momentum'] = layer.momentum
                    data[-1]['weights'] = layer.w
                    data[-1]['biases'] = layer.bias
                elif layer.__class__ == MaxPooling:
                    data[-1]['channels'] = layer.channels
                    data[-1]['height'] = layer.height
                    data[-1]['width'] = layer.width
                    data[-1]['matrix_h'] = layer.matrix_h
                    data[-1]['matrix_w'] = layer.matrix_w

            json.dump(data, file)

    def load(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.layers = []

            for layer in json.load(file):
                if layer['type'] == 'FullConnected':
                    self.layers.append(FullConnected(
                        size=layer['size'],
                        activation=[eval(i + '()') for i in layer['activation']],
                        loss=eval(layer['loss'] + '()'),
                        learning_rate=layer['learning_rate'],
                        momentum=layer['momentum']
                    ))
                    self.layers[-1].w = layer['weights']
                    self.layers[-1].b = layer['biases']
                elif layer['type'] == 'Convolution':
                    self.layers.append(Convolution(
                        channels=layer['channels'],
                        height=layer['height'],
                        width=layer['width'],
                        matrix_c=layer['matrix_c'],
                        matrix_h=layer['matrix_h'],
                        matrix_w=layer['matrix_w'],
                        padding=layer['padding'],
                        stride_h=layer['stride_h'],
                        stride_w=layer['stride_w'],
                        activation=eval(layer['activation'] + '()'),
                        learning_rate=layer['learning_rate'],
                        momentum=layer['momentum']
                    ))
                    self.layers[-1].w = layer['weights']
                    self.layers[-1].b = layer['biases']
                elif layer['type'] == 'MaxPooling':
                    self.layers.append(MaxPooling(
                        channels=layer['channels'],
                        height=layer['height'],
                        width=layer['width'],
                        matrix_h=layer['matrix_h'],
                        matrix_w=layer['matrix_w']
                    ))

    def result(self):
        return [*self.layers[-1].x[-1]]

    def define_err(self):
        for layer in self.layers:
            layer.define_err()

    def forward(self, data_input):
        for layer in self.layers:
            if layer.__class__ == FullConnected and len(self.layers) > 1:
                x = []
                for chanel in data_input:
                    for row in chanel:
                        x += row
                data_input = x

            layer.forward(data_input)
            data_input = layer.x

    def backward(self, data_output):
        for layer in self.layers[::-1]:
            layer.backward(data_output)
            data_output = layer.err

            if layer.__class__ == FullConnected and len(self.layers) > 1:
                data_output = data_output[0]
                channels = len(self.layers[-2].x)
                height = len(self.layers[-2].x[0])
                width = len(self.layers[-2].x[0][0])
                err = []
                for i in range(channels):
                    err.append([])
                    for j in range(height):
                        err[i].append([])
                        for l in range(width):
                            err[i][j].append(data_output[i * height * width + j * width + l])
                data_output = err

    def calculate_error(self, data):
        self.error = 0

        for i in range(len(data)):
            self.forward(data[i][0])
            for j in range(len(data[i][1])):
                self.error += abs(data[i][1][j] - self.layers[-1].x[-1][j])
            self.error /= len(data[i][1])
        self.error /= len(data)

    def train(self, data, epochs=10000):
        for epoch in range(epochs):
            # start_epoch = time.time()
            i = random.randint(0, len(data) - 1)
            self.forward(data[i][0])
            self.backward(data[i][1])
            # if self.debug:
            #     print(f'time {round(time.time() - start_epoch, 2)}')
        self.epochs += epochs
        self.calculate_error(data)

    def train_alpha(self, data, alpha=0.001):
        for i in range(len(data)):
            self.forward(data[i][0])
            self.data_start.append(self.result())
            print(cyan, i, self.result(), '->', data[i][1], endc)
        self.calculate_error(data)
        self.error_start = self.error
        print(cyan, self.error_start, endc)

        start = time.time()
        while self.error > alpha:

            if self.error < self.error_min:
                self.error_min = self.error
                self.data_min = copy.deepcopy(self.data_start)
                self.file_path = self.file_path[:self.file_path.rfind(os.sep)] + os.sep + 'tmp_' + self.file_path[self.file_path.rfind(os.sep) + 1:]
                self.save()
                self.file_path = self.file_path.replace('tmp_', '')

            self.train(data, 100)
            self.save()

            if self.debug:
                for j in range(len(data)):
                    self.forward(data[j][0])
                    print(green, j, self.data_start[j], '->', self.data_min[j], '->', self.layers[-1].x[-1], '->', data[j][1], endc)
                print(self.error_start, '->', self.error_min, '->', self.error)
                print(self.epochs)

        print(yellow + f'time {round(time.time() - start, 2)}' + endc)

    def info(self):
        print(f'error = {self.error},')
        print(f'epochs = {self.epochs},')
        for layer in self.layers:
            print(layer.__class__.__name__ + ':')
            if layer.__class__ == FullConnected:
                print(f'    size = {layer.size},')
                print(f'    activation = {", ".join([i.__class__.__name__ for i in layer.activation])}')
                print(f'    loss = {layer.loss.__class__.__name__}')
                print(f'    learning_rate = {layer.learning_rate}')
                print(f'    momentum = {layer.momentum}')
            elif layer.__class__ == Convolution:
                print(f'    data_input_size = {layer.channels} x {layer.height - 2 * layer.padding} x {layer.width - 2 * layer.padding},')
                print(f'    size = {layer.matrix_c} x {1 + (layer.height - layer.matrix_h) // layer.stride_h} x {1 + (layer.width - layer.matrix_w) // layer.stride_w}')
                print(f'    matrix_size = {layer.matrix_c} x {layer.matrix_h} x {layer.matrix_w}')
                print(f'    stride_size = {layer.stride_h} x {layer.stride_w}')
                print(f'    padding = {layer.padding}')
                print(f'    activation = {layer.activation.__class__.__name__}')
                print(f'    learning_rate = {layer.learning_rate}')
                print(f'    momentum = {layer.momentum}')
            elif layer.__class__ == MaxPooling:
                print(f'    data_input_size = {layer.channels} x {layer.height} x {layer.width}')
                print(f'    size = {layer.channels} x {layer.height // layer.matrix_h} x {layer.width // layer.matrix_w}')
                print(f'    matrix_size = {layer.matrix_h} x {layer.matrix_w}')
