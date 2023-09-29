import pygame


class Button:
    def __init__(self, window, x, y,
                 width=100,
                 height=50,
                 text='button',
                 border_radius=5,
                 font_family='Arial',
                 font_size=24,
                 fill_color=(160, 99, 160),
                 border_color=(44, 27, 44),
                 font_color=(255, 255, 255)
                 ):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.fill_color = fill_color
        self.border_color = border_color
        font = pygame.font.SysFont(font_family, font_size)
        self.text_surface = font.render(text, True, font_color)

    def draw(self):
        pygame.draw.rect(self.window, self.fill_color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.window, self.border_color, (self.x, self.y, self.width, self.height), self.border_radius)
        self.window.blit(self.text_surface, (self.x, self.y))


class Slider:
    def __init__(self):
        pass
