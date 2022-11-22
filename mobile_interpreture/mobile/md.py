from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.app import MDApp

import sys
import os


class Container(MDBoxLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True
        )

    def file_manager_open(self):
        self.file_manager.show("mobile_interpreture/assets")

    def select_path(self, path):
        self.exit_manager()
        
    def exit_manager(self, *args):
        self.file_manager.close()
        

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