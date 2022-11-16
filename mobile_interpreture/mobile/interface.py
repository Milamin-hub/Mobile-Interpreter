from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Container(BoxLayout):
    pass


class InterpretureApp(App):
    """ Interface app """
    def __init__(self) -> None:
        super().__init__()

    def build(self) -> Container:
        """ ... """
        return Container()


if __name__ == '__main__':
    InterpretureApp().run()