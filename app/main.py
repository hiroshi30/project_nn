# 1 - save image as 1
# 0 - save image as 0
# q - show/hide grid
# w - clear field
# e - make prediction
# r - save all pictures to data
# left mouse button - draw
# right mouse button - erase

import os
import sys

import numpy
import pygame
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(sys.path[0], os.pardir)))

from core import *


pygame.init()

data = []
with open(sys.path[0] + os.sep + 'data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

nn = nn(file_path=f'~{os.sep}tmp_model1.json')
nn.load()

nn.info()

nn.calculate_error(data)
print(nn.error)

window_size = (1000, 600)
canvas_size = (600, 600)
block_size = (60, 30)

background_color = (0, 0, 0)
paint_color = (255, 255, 255)

font = pygame.font.SysFont('Arial', 32)
font_color = (255, 255, 255)

pth = sys.path[0] + os.sep + '../..'

if 'images' not in os.listdir(pth):
    os.mkdir(pth + os.sep + 'images')

pth += os.sep + 'images'

if f'{canvas_size[1] // block_size[1]}x{canvas_size[0] // block_size[0]}' not in os.listdir(pth):
    os.mkdir(pth + os.sep + f'{canvas_size[1] // block_size[1]}x{canvas_size[0] // block_size[0]}')

pth += os.sep + f'{canvas_size[1] // block_size[1]}x{canvas_size[0] // block_size[0]}'

for i in '0', '1':
    if i not in os.listdir(pth):
        os.mkdir(pth + os.sep + i)

window = pygame.display.set_mode(window_size)

arr = numpy.zeros([canvas_size[1] // block_size[1], canvas_size[0] // block_size[0], 3], dtype=numpy.uint8)
grid = True
paint = False
erase = False

size = [0, 0]
x0 = 0
y0 = 0
text_surface = []

while True:

    window.fill(background_color)

    for y in range(canvas_size[1] // block_size[1]):
        for x in range(canvas_size[0] // block_size[0]):
            pygame.draw.rect(window, arr[y][x], (x * block_size[0], y * block_size[1], block_size[0], block_size[1]))

    if grid:
        for i in range(0, canvas_size[0] + 1, block_size[0]):
            pygame.draw.aaline(window, (150, 150, 150), (i, 0), (i, canvas_size[1]))

        for i in range(0, canvas_size[1] + 1, block_size[1]):
            pygame.draw.aaline(window, (150, 150, 150), (0, i), (canvas_size[0], i))

    for y in range(len(text_surface)):
        window.blit(text_surface[y], (x0, y0 + y * size[1]))

    if paint:
        pos = pygame.mouse.get_pos()
        x = pos[0] // block_size[0]
        y = pos[1] // block_size[1]
        if 0 <= x < canvas_size[0] // block_size[0]:
            if 0 <= y < canvas_size[1] // block_size[1]:
                arr[y][x] = numpy.array(paint_color)

    if erase:
        pos = pygame.mouse.get_pos()
        x = pos[0] // block_size[0]
        y = pos[1] // block_size[1]
        if 0 <= x < canvas_size[0] // block_size[0]:
            if 0 <= y < canvas_size[1] // block_size[1]:
                arr[y][x] = numpy.array(background_color)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            paint = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            paint = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            erase = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            erase = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_0:
                image = Image.fromarray(arr)
                name = 0
                for i in os.listdir(pth + os.sep + '0'):
                    name = max(name, int(i[:i.find('.')]))
                name += 1
                image.save(pth + os.sep + '0' + os.sep + f'{name}.png')

            if event.key == pygame.K_1:
                image = Image.fromarray(arr)
                name = 0
                for i in os.listdir(pth + os.sep + '1'):
                    name = max(name, int(i[:i.find('.')]))
                name += 1
                image.save(pth + os.sep + '1' + os.sep + f'{name}.png')

            if event.key == pygame.K_q:
                grid = not grid

            if event.key == pygame.K_w:
                for y in range(canvas_size[1] // block_size[1]):
                    for x in range(canvas_size[0] // block_size[0]):
                        arr[y][x] = numpy.array(background_color)

            if event.key == pygame.K_e:
                new_arr = []
                for i in range(len(arr[0][0])):
                    new_arr.append([])
                    for j in range(len(arr)):
                        new_arr[i].append([])
                        for l in range(len(arr[0])):
                            new_arr[i][j].append(arr[j][l][i])

                nn.forward(new_arr)
                text_surface = [
                    font.render(f'0 = {nn.result()[0]}', True, font_color),
                    font.render(f'1 = {nn.result()[1]}', True, font_color)
                ]

                size = text_surface[0].get_rect().size
                x0 = canvas_size[0] + (window_size[0] - canvas_size[0] - size[0]) // 2
                y0 = (window_size[1] - len(text_surface) * size[1]) // 2

            if event.key == pygame.K_r:
                make_json()

    pygame.display.update()
    pygame.display.flip()
