from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import (Color, Line)

import os
import sys


class Paint(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(255, 255, 255)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


class Main(App):
    def build(self):
        self.lb = Label(size=(100, 50), text='OK', pos=(700, 0))
        parent = Widget()
        self.painter = Paint()
        parent.add_widget(self.painter)
        parent.add_widget(Button(size=(100, 50), text='Clear', on_press=self.clear_canvas))
        parent.add_widget(Button(size=(100, 50), text='Save as 1', on_press=self.save_as_1, pos=(100, 0)))
        parent.add_widget(Button(size=(100, 50), text='Save as 0', on_press=self.save_as_0, pos=(200, 0)))
        parent.add_widget(Button(size=(100, 50), text='Train', on_press=lambda: print('dont work'), pos=(300, 0)))
        parent.add_widget(Button(size=(100, 50), text='Save weights', on_press=lambda: print('dont work'), pos=(400, 0)))
        parent.add_widget(Button(size=(100, 50), text='Load weights', on_press=lambda: print('dont work'), pos=(500, 0)))
        parent.add_widget(Button(size=(100, 50), text='Check', on_press=lambda: print('dont work'), pos=(600, 0)))
        parent.add_widget(self.lb)

        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save_as_1(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        x = os.listdir(sys.path[0] + '\\..\\images\\1')
        x = len(x) - 1
        self.painter.export_to_png(sys.path[0] + f'\\..\\images\\1\\{x}.png')

    def save_as_0(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        x = os.listdir(sys.path[0] + '\\..\\images\\0')
        x = len(x) - 1
        self.painter.export_to_png(sys.path[0] + f'\\..\\images\\0\\{x}.png')


Main().run()
