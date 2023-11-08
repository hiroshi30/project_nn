import os
import sys
import json

import numpy
from PIL import Image


def make_json(resolution='20x10', save_name='data'):
    pth = os.path.abspath(os.path.join(sys.path[0], os.pardir))
    pth = os.path.abspath(os.path.join(pth, os.pardir))
    pth += os.sep + 'images' + os.sep + resolution

    data = []

    index = 0
    count = 0

    for name in os.listdir(pth):
        data_output = [0] * len(os.listdir(pth))
        data_output[index] = 1
        index += 1
        for img in os.listdir(pth + os.sep + name):
            count += 1
            print(count, 'Loaded', pth + os.sep + name + os.sep + img)
            image = Image.open(pth + os.sep + name + os.sep + img).convert('RGB')
            image = numpy.array(image, dtype=numpy.uint8)
            data_input = [[], [], []]

            for i in range(len(image)):
                data_input[0].append([])
                data_input[1].append([])
                data_input[2].append([])
                for j in range(len(image[0])):
                    data_input[0][i].append(image[i][j][0] / 255)
                    data_input[1][i].append(image[i][j][2] / 255)
                    data_input[2][i].append(image[i][j][2] / 255)

            data.append([data_input, data_output])

    with open(f'{sys.path[0]}\\{save_name}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    print(f'Saved {count} images in {save_name}.json')


if __name__ == '__main__':
    make_json()
