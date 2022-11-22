from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

import sys
import os


# Add methods
class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def input_text(self) -> str:
        txt = self.ids.fname.text
        print(txt)


class Container(MDBoxLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def on_create(self):
        with open('mobile_interpreture/assets/%s' % self.ids.cfile.text, "w"):
            return "Успешно создан"
    
    def take_name_tabs(self) -> str:
        return self.ids.tabs.title
    
    def on_save(self):
        try:
            print(self.take_name_tabs())
        except ValueError as e:
            print(e)
        

class UIApp(MDApp):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def build(self) -> Container:
        """build window from class container to which 
        the file with styles and components is attached interpreture.kv """
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Container()
        

if __name__ == '__main__':
    UIApp().run()