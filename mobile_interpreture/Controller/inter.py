from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from io import StringIO
from kivy.lang import Builder


import sys
import os

class MyContainer(MDBoxLayout):
    def __init__(self, **kwargs):
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
            self.save_file()
            with open("mobile_interpreture/assets/%s" % name, "r") as file:
                text = ""
                for i in file:
                    text += i
                old_stdout = sys.stdout
                redirected_output = sys.stdout = StringIO()
                exec(text)
                sys.stdout = old_stdout
                self.ids.run.text = redirected_output.getvalue().strip()
        except Exception as e:
            print(e)
    
    def create_file(self):
        name = "p%s.py" % (int(len(os.listdir(path="mobile_interpreture/assets/"))) + 1)
        if '%s' % name not in os.listdir(path="mobile_interpreture/assets/"):
            with open('mobile_interpreture/assets/%s' % name, "w"):
                pass

    def delete_file(self):
        name = os.path.basename(self.path)
        text = "Welcome"
        self.ids.fname.opacity = 0
        self.ids.fname.enabled = False
        if '%s' % name in os.listdir(path="mobile_interpreture/assets/"):
            os.remove("mobile_interpreture/assets/%s" % name)
            self.ids.filen.text = text
            