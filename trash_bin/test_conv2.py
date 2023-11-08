from core import *


arr = [
    [
        [6, 6, 1, 8, 6, 0, 10],
        [3, 2, 1, 1, 1, 3, 7],
        [6, 8, 4, 10, 10, 8, 1],
        [5, 9, 5, 10, 2, 3, 1],
        [7, 0, 3, 4, 7, 6, 8],
        [1, 4, 1, 5, 5, 9, 7],
        [8, 9, 5, 5, 10, 6, 2]
    ],
    [
        [4, 5, 4, 1, 2, 4, 6],
        [3, 8, 6, 7, 8, 6, 2],
        [2, 3, 10, 0, 3, 3, 0],
        [5, 6, 4, 9, 1, 9, 8],
        [4, 5, 4, 5, 5, 3, 8],
        [3, 0, 0, 4, 5, 8, 5],
        [3, 1, 10, 3, 1, 10, 4]
    ],
    [
        [4, 0, 7, 5, 6, 5, 1],
        [0, 5, 0, 7, 8, 7, 5],
        [2, 2, 4, 4, 3, 4, 5],
        [3, 6, 7, 1, 10, 3, 0],
        [9, 0, 2, 5, 6, 1, 2],
        [8, 5, 9, 7, 6, 3, 0],
        [0, 8, 10, 4, 1, 6, 6]
    ]
]

output = [1, 0]

ai = AI(layers=[
    Convolution(
        height=7,
        width=7,
        chanels=3,
        matrix_h=3,
        matrix_w=3,
        matrix_c=2,
        stride_h=2,
        stride_w=2,
        padding=1
    ),
    MaxPooling(
        height=4,
        width=4,
        chanels=2,
        matrix_w=2,
        matrix_h=2
    ),
    FullConnected(
        size=[8, 4, 2]
    )
], debug=False)

pprint(ai.layers[-1].x[-1])

for i in range(10):
    ai.forward(arr)
    ai.backward(output)

pprint(output)
pprint(ai.layers[-1].x[-1])
