# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.window import Window

# Глобальные настройки
Window.size = (720,1080)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = "Конвертер"


class MyApp(App):

    # Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()
        self.label = Label(text='Умный Дом')
        self.btn=Button(text="сигналка")

MyApp().run()