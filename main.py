import kivy
from kivy.app import App
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        return Label(text='Hello, Kivy!')

if __name__ == '__main__':
    SimpleApp().run()
