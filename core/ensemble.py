from library import *


class Ensemble:
    def __init__(self, type, count, *args):
        self.networks = [type(*args) for i in range(count)]
        self.type = type

    def for_each(self, *args):
        action.replace('self', 'network')
        for network in self.networks:
            for action in args.split(' self'):
                exec('network' + action)

    def forward(self, *args):
        results = [0] * self.networks[0].size[-1]
        for network in self.networks:
            network.forward(*args)
            result = network.x[-1]
            for i in range(len(result)):
                results[i] += result[i]
        for i in range(len(result)):
            results[i] /= len(self.networks)
        self.x = [results]

    def backward(self, *args):
        for network in self.networks:
            network.backward(*args)
