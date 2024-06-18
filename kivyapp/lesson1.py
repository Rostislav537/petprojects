from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.core.window import Window
Window.size=(300, 400)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Test"
class MyApp(App):
    def __init__(self):
        super().__init__()
        self.btn=Button(text="Fsdfsd", on_press=self.btn1)
        self.metres = Label(text='')
    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.btn)
        box.add_widget(self.metres)
        return box
    def btn1(self, argument):
        self.metres.text="sdfdsdfsdffsd"
        #Animation(x=100, y=100, t='in_quad').start(self.metres)
        anim = Animation(x=100, y=100)
        anim &= Animation(size=(200, 200), duration=2)
        anim.start(self.metres)
if __name__ == "__main__":
    MyApp().run()