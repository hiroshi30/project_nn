import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(sys.path[0], os.pardir)))

from core import *


# make_json(resolution="20x10", save_name="data")

data = []
with open(sys.path[0] + os.sep + 'data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# nn = nn(file_path='~' + os.sep + 'test1.json', debug=True)
# nn.load()

nn = nn(layers=[
    Convolution(
        channels=3,
        height=20,
        width=10,
        matrix_c=8,
        matrix_h=3,
        matrix_w=3,
        learning_rate=0.09,
        momentum=0.03
    ),
    MaxPooling(
        channels=8,
        height=20,
        width=10,
        matrix_h=2,
        matrix_w=2
    ),
    Convolution(
        channels=8,
        height=10,
        width=5,
        matrix_c=1,
        matrix_h=2,
        matrix_w=3,
        learning_rate=0.03,
        momentum=0.01,
        stride_w=2
    ),
    FullConnected(
        size=[8 * 5 * 2, 16, 4, 2],
        activation=[ReLU(), Sigmoid(), Sigmoid(), SoftMax()],
        loss=MSE(),
        learning_rate=0.4,
        momentum=0.1
    )
], file_path=f'~{os.sep}model1.json', debug=True)

nn.info()

nn.define_err()
nn.train_alpha(data, alpha=1e-4)

for i in range(len(data)):
    print(i, data[i][1])

while True:
    x = int(input())
    nn.forward(data[x][0])
    print(nn.result(), data[x][1])
