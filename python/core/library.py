import math


# L1 Loss
class MAE:
    def f(self, ideal, output):
        return abs(ideal - output)

    def df(self, ideal, output):
        if ideal >= output:
            return -1
        else:
            return 1


# L2 Loss
class MSE:
    def f(self, ideal, output):
        return (ideal - output) ** 2

    def df(self, ideal, output):
        return 2 * (output - ideal)


# Log Loss
class CrossEntropy:
    def f(self, ideal, output):
        return -ideal * math.log(output) - (1 - ideal) * math.log(1 - output)
        # return -ideal * math.log(output)

    def df(self, ideal, output):
        return -ideal / output + (1 - ideal) / (1 - output)
        # return -ideal / output


class HingeLoss:
    def f(self, ideal, output):
        return max(0, 1 - ideal * output)

    def df(self, ideal, output):
        if 1 - ideal * output > 0:
            return -ideal
        else:
            return 0


class HuberLoss:
    def __init__(self, delta=0.5):
        self.delta = delta

    def f(self, ideal, output):
        if abs(output - ideal) <= self.delta:
            return 1 / 2 * (output - ideal) ** 2
        else:
            return self.delta * abs(output - ideal) - 1 / 2 * self.delta ** 2

    def df(self, ideal, output):
        if abs(ideal - output) <= self.delta:
            return output - ideal
        else:
            if output >= ideal:
                return self.delta
            else:
                return -self.delta


class Sigmoid:
    def f(self, x):
        try:
            return 1 / (1 + math.exp(-x))
        except:
            return 0.5

    def df(self, x):
        return (1 - x) * x


class Tanh:
    def f(self, x):
        return (math.exp(2 * x) - 1) / (math.exp(2 * x) + 1)

    def df(self, x):
        return 1 - x ** 2


class ReLU:
    def f(self, x):
        return max(0, x)

    def df(self, x):
        if x > 0:
            return 1
        else:
            return 0


class LeakyReLU:
    def f(self, x):
        return max(0.01 * x, x)

    def df(self, x):
        if x > 0:
            return 1
        else:
            return 0.01


class SoftMax:
    def f(self, layer):
        try:
            layer = [math.exp(x) for x in layer]
        except OverflowError:
            print(red, 'OverflowError', layer, endc)
            alpha = min(layer)
            if alpha < 0:
                alpha = abs(alpha)
                layer = [x + alpha for x in layer]

        s = sum(layer)

        return [x / s for x in layer]

    def df(self, x):
        return x * (1 - x)
