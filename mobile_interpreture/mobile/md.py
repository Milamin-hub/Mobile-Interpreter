from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.app import MDApp
from io import StringIO

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
            p, file_ext = os.path.splitext(path)
            if file_ext == ".py":
                self.exit_manager()
                file = open("%s" % path, "r").readlines()
                text = ""
                for i in file:
                    text += i
                self.ids.fname.opacity = 1
                self.ids.fname.enabled = True
                self.ids.fname.text = text
                self.path = path
                n = os.path.basename(self.path)
                self.ids.filen.text = n
            else:
                pass
        except IsADirectoryError:
            pass
        
    def exit_manager(self, *args):
        self.file_manager.close()

    def save_file(self):
        try:
            name = os.path.basename(self.path)
            with open("mobile_interpreture/assets/%s" % name, "w") as file:
                file.write(self.ids.fname.text)
        except IsADirectoryError as e:
            print(e)
        
    def run_file(self):
        name = os.path.basename(self.path)
        try:
            with open("mobile_interpreture/assets/%s" % name, "r") as file:
                text = ""
                for i in file:
                    text += i
                old_stdout = sys.stdout
                redirected_output = sys.stdout = StringIO()
                exec(text)
                sys.stdout = old_stdout
                self.ids.run.text = redirected_output.getvalue().strip()
        except FileNotFoundError as e:
            print(e)
        except IsADirectoryError as e:
            print(e)
    
    def create_file(self):
        pass

    def delete_file(self):
        pass
        

class UIApp(MDApp):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def build(self) -> Container:
        """build window from class container to which 
        the file with styles and components is attached interpreture.kv """
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Container()
        

if __name__ == "__main__":
    UIApp().run()