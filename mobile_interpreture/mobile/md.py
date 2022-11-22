from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from plyer import filechooser
from kivymd.toast import toast

from kivymd.app import MDApp

import sys
import os


class Container(MDBoxLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.path = ""
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=False,
        )

    def file_manager_open(self):
        self.file_manager.show("mobile_interpreture/assets/")

    def select_path(self, path) -> str:
        try:
            self.exit_manager()
            file = open('%s' % path, "r").readlines()
            text = ""
            for i in file:
                text += i
            self.ids.fname.opacity = 1
            self.ids.fname.enabled = True
            self.ids.fname.text = text
            self.path = path
        except IsADirectoryError:
            pass
        
    def exit_manager(self, *args):
        self.file_manager.close()

    def save_file(self):
        name = os.path.basename(self.path)
        with open('mobile_interpreture/assets/%s' % name, "w") as file:
            file.write(self.ids.fname.text)
    
        

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