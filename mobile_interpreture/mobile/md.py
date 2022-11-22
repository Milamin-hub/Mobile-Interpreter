from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.app import MDApp

import sys
import os


class Container(MDBoxLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.file_manager_obj = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager,
            preview=True
        )
    
    def select_path(self, path):
        print(path)
        self.exit_manager()

    def open_file_manager(self):
        self.file_manager_obj.show("mobile_interpreture/assets")

    def exit_manager(self):
        self.file_manager_obj.close()

    def on_create(self):
        try:
            with open('mobile_interpreture/assets/%s' % self.ids.cfile.text, "w"):
                return "Успешно создан"
        except Exception as e:
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