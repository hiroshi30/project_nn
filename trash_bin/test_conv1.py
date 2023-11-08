from core import *


# path = r"C:\Users\takayama\Desktop\project\Images\Snejok.jpg"
# # image = asarray(Image.open(path).convert('RGB'))
# image = asarray(Image.open(path))

# black_white = [[sum(image[y][x]) / (3 * 255) for x in range(len(image[0]))] for y in range(len(image))]

# rgb = [[[x * 255] * 3 for x in y] for y in black_white]

# rgb = array(rgb, dtype=uint8)

# # new_image = Image.fromarray(rgb, 'RGB')
# new_image = Image.fromarray(rgb)
# new_image.save(r"C:\Users\takayama\Desktop\project\Images\1212.jpg")


os.system('color')

GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

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

convolution_arr = [
    [
        [0, 0, 0, 0],
        [21, 37, 48, 30],
        [34, 57, 48, 24],
        [21, 35, 52, 32]
    ],
    [
        [25, 37, 37, 26],
        [23, 45, 45, 21],
        [25, 28, 42, 28],
        [29, 55, 46, 34]
    ]
]

maxpooling_arr = [
    [
        [37, 48],
        [57, 52]
    ],
    [
        [45, 45],
        [55, 46]
    ]
]

fullconnected_arr = [
    [37, 48, 57, 52, 45, 45, 55, 46],
    [385, 385, 385, 385],
    [1540, 1540]
]

output = [750, 0]

ai = AI(layers=[
    Convolution(
        height=7,
        width=7,
        chanels=3,
        matrix_h=3,
        matrix_w=3,
        matrix_c=2,
        stride_h=2,
        stride_w=2
    ),
    MaxPooling(
        height=4,
        width=4,
        chanels=2,
        matrix_w=2,
        matrix_h=2
    ),
    FullConnected(
        size=[8, 4, 2],
        activation=[ReLU(), ReLU(), ReLU()]
    )
], debug=False)

ai.layers[0].w = [
    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
]

ai.layers[0].bias = [0, 0]

ai.layers[2].w = [
    [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ],
    [
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1]
    ]
]

ai.layers[2].bias = [
    [0, 0, 0, 0],
    [0, 0]
]

ai.forward(arr)
ai.backward(output)

tmp = ai.layers[0].x == convolution_arr
print(f'Convolution forward {tmp * GREEN + (not tmp) * RED}{tmp}{ENDC}')

if not tmp:
    print('data_input')
    pprint(ai.layers[0].data_input)
    print('ai.x')
    pprint(ai.layers[0].x)

tmp = ai.layers[1].x == maxpooling_arr
print(f'MaxPooling forward {tmp * GREEN + (not tmp) * RED}{tmp}{ENDC}')

if not tmp:
    print('data_input')
    pprint(ai.layers[1].data_input)
    print('ai.x')
    pprint(ai.layers[1].x)

tmp = ai.layers[2].x == fullconnected_arr
print(f'FullConnected forward {tmp * GREEN + (not tmp) * RED}{tmp}{ENDC}')
if not tmp:
    print('ai.x')
    pprint(ai.layers[2].x)
