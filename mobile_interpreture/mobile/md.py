from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

import sys
import os


# Add path for logic
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from mobile.logic import Interpreture


class Container(MDBoxLayout, Interpreture):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class UIApp(MDApp):
    def __init__(self) -> None:
        super().__init__()

    def build(self) -> Container:
        """build window from class container to which 
        the file with styles and components is attached interpreture.kv """
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Container()


if __name__ == '__main__':
    UIApp().run()