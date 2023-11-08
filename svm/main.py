# ESC - quit programm
# 1 - place red dot
# 2 - place blue dot
# q - make prediction dot
# w - make prediction for all dots of field
# e - change preset
# r - clear field
# z - train nn
# x - train_alpha nn

import sys

delimetr = '\\'
if '/' in sys.path[0]:
    delimetr = '/'

sys.path.append(sys.path[0][:sys.path[0].rfind(delimetr)])

import json

import pygame
pygame.init()

from core import *


epochs = 0


def train(nn, data, epochs=0):
    for i in range(10000):
        index = random.randint(0, len(data) - 1)
        nn.forward(data[index][0])
        nn.backward(data[index][1])

        epochs += 1

    error = 0
    for i in range(len(data)):
        nn.forward(data[i][0])
        for j in range(len(nn.x[-1])):
            error += abs(data[i][1][j] - nn.x[-1][j])
        error /= len(nn.x[-1])
    error /= len(data)

    return epochs, error


size = [2, 4, 2, 2]
activation = [Sigmoid(), Sigmoid(), Sigmoid(), SoftMax()]
loss = CrossEntropy()

nn = FullConnected(
    size=size,
    activation=activation,
    loss=loss
)
nn.define_err()

window_size = (500, 500)
preset = 0
count_preset = 2

background_color = (255, 255, 255)
colors = [
    (255, 0, 0),
    (0, 0, 255)
]
colors0 = [
    (255, 100, 100),
    (100, 200, 255)
]
_color = (0, 0, 0)
border_color = (100, 255, 100)
border_standart_color = (0, 0, 0)

radius = 15
border_width = 5
border_standart_width = 2
background_radius = 2

window = pygame.display.set_mode(window_size)


def load_preset(name):
    data = None
    with open(f'{sys.path[0]}\\{name}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def save_preset(name, data):
    with open(f'{sys.path[0]}\\{name}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)


arr_background = []
arr_border = []
data = []

while True:

    window.fill(background_color)

    for i in arr_background:
        pygame.draw.circle(window, i[0], i[1], background_radius)

    for i in data:
        pos = i[0]
        pos = [int(pos[0] * window_size[0]), int(pos[1] * window_size[1])]

        color = _color
        if i[1][0] == 1:
            color = colors[0]
        elif i[1][1] == 1:
            color = colors[1]

        pygame.draw.circle(window, border_standart_color, pos, radius + border_standart_width)
        pygame.draw.circle(window, color, pos, radius)

    for i in arr_border:
        pygame.draw.circle(window, border_color, i[1], radius + border_width)
        pygame.draw.circle(window, i[0], i[1], radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_1:
                pos = pygame.mouse.get_pos()
                data_input = [normalize(pos[0], window_size[0]), normalize(pos[1], window_size[1])]
                data.append([data_input, [1, 0]])

            elif event.key == pygame.K_2:
                pos = pygame.mouse.get_pos()
                data_input = [normalize(pos[0], window_size[0]), normalize(pos[1], window_size[1])]
                data.append([data_input, [0, 1]])

            elif event.key == pygame.K_z:
                print('epochs', epochs, '->', end=' ')
                epochs, error = train(nn, data, epochs)
                print(epochs, 'error', error)
                print(green + 'COMPLETE' + endc)

            elif event.key == pygame.K_x:
                error = 1
                while error > 1e-5:
                    print('epochs', epochs, '->', end=' ')
                    epochs, error = train(nn, data, epochs)
                    print(epochs, 'error', error)
                print(green + 'COMPLETE' + endc)

            elif event.key == pygame.K_q:
                pos = pygame.mouse.get_pos()
                x = [normalize(pos[0], window_size[0]), normalize(pos[1], window_size[1])]
                nn.forward(x, False)
                x = nn.x[-1]

                color = _color
                if x[0] > 0.5:
                    color = colors[0]
                elif x[1] > 0.5:
                    color = colors[1]

                arr_border.append([color, pos])
                print(f'x = {nn.x}\nelse = {[color, pos]}')

            elif event.key == pygame.K_w:
                for x in range(0, window_size[0] + 1, background_radius * 2):
                    for y in range(0, window_size[1] + 1, background_radius * 2):
                        data_input = [normalize(x, window_size[0]), normalize(y, window_size[1])]
                        nn.forward(data_input, False)
                        data_input = nn.x[-1]

                        color = _color
                        if data_input[0] > 0.5:
                            color = colors0[0]
                        elif data_input[1] > 0.5:
                            color = colors0[1]
                        print(x, y)

                        arr_background.append([color, (x, y)])

            elif event.key == pygame.K_e:
                preset += 1

                preset %= count_preset + 1

                arr_background = []
                arr_border = []

                if preset == 0:
                    data = []
                else:
                    data = load_preset(str(preset))

            elif event.key == pygame.K_r:
                arr_background = []
                arr_border = []
                data = []
                nn = FullConnected(
                    size=size,
                    activation=activation,
                    loss=loss
                )
                nn.define_err()

    pygame.display.flip()
    pygame.display.update()
