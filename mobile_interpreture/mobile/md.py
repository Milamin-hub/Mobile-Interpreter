from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

import sys
import os


# Add path for logic
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from mobile_interpreture.mobile.fmanager import Interpreture


# Add methods
class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Container(MDBoxLayout, Interpreture):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def on_create(self):
        self.create_file(self.ids.cfile.text)
    
    def take_name(self):
        return self.ids.tabs.title
    
    def on_save(self):
        pass
        


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