import sys
import os

sys.path.append(sys.path[0][:sys.path[0].rfind(os.sep)])

from core import *


x = [
    [[1, 1, 1], [1, 0]],
    [[1, 1, 0], [1, 0]],
    [[1, 0, 0], [0, 1]],
    [[0, 0, 0], [0, 1]],
    [[0, 0, 1], [0, 1]],
    [[0, 1, 1], [0, 1]],
    [[1, 0, 1], [0, 1]],
    [[0, 1, 0], [0, 1]]
]

y = [
    [[1, 1, 1], [1]],
    [[1, 1, 0], [1]],
    [[1, 0, 0], [0]],
    [[0, 0, 0], [0]],
    [[0, 0, 1], [0]],
    [[0, 1, 1], [0]],
    [[1, 0, 1], [0]],
    [[0, 1, 0], [0]]
]

z = [
    [[1, 0, 1], [1, 0]],
    [[1, 0, 0], [1, 0]],
    [[0, 1, 1], [0, 1]],
    [[1, 1, 1], [1, 0]],
    [[0, 0, 0], [0, 1]],
    [[0, 1, 0], [0, 1]]
]

b = z

nn = nn(layers=[
    FullConnected(
        size=[3, 2],
        activation=[ReLU(), SoftMax()],
        loss=MSE()
    )
], debug=False)

nn.define_err()

# nn.train_alpha(b, 1e-3)
nn.train(b, 500)
nn.info()

for i in b:
    nn.forward(i[0])
    print(nn.layers[-1].x[-1], i[1])
