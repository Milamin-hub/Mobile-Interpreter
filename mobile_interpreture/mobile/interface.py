from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import sys
import os
# Add path for logic
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from mobile.logic import Interpreture


class Container(BoxLayout, Interpreture):
    pass


class InterpretureApp(App):
    """ Interface app """
    def __init__(self) -> None:
        super().__init__()

    def build(self) -> Container:
        """build window from class container to which 
        the file with styles and components is attached interpreture.kv """
        return Container()


if __name__ == '__main__':
    InterpretureApp().run()