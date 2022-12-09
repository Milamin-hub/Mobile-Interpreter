from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.boxlayout import MDBoxLayout

from io import StringIO
from View.config import path, red, white 

import sys
import os


class InterpretureView(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path = ""
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=False,
        )

    def file_manager_open(self):
        self.file_manager.show(path)

    def select_path(self, path) -> str:
        try:
            p, file_ext = os.path.splitext(path)
            if file_ext == ".py":
                self.exit_manager()
                file = open("%s" % path, "r").readlines()
                text = ""
                for i in file:
                    text += i
                self.ids.codeinput.opacity = 1
                self.ids.codeinput.enabled = True
                self.ids.codeinput.text = text
                self.path = path
                n = os.path.basename(self.path)
                self.ids.filen.text = n
            else:
                pass
        except IsADirectoryError as e:
            self.ids.terminal.color = red
            self.ids.terminal.text = str(e)
        
    def exit_manager(self, *args):
        self.file_manager.close()

    def save_file(self):
        try:
            name = os.path.basename(self.path)
            with open(path + name, "w") as file:
                file.write(self.ids.codeinput.text)
        except IsADirectoryError as e:
            self.ids.terminal.color = red
            self.ids.terminal.text = str(e)
        
    def run_file(self):
        name = os.path.basename(self.path)
        try:
            self.save_file()
            with open(path + name, "r") as file:
                text = ""
                for i in file:
                    text += i
                if not "input" in text and not "sleep" in text:
                    redirected_output = sys.stdout = StringIO()
                    compile(path + name, "test", "exec")
                    exec(text)
                    self.ids.terminal.text = redirected_output.getvalue().strip()
                    self.ids.terminal.color = white
                else:
                    self.ids.terminal.color = red
                    self.ids.terminal.text = "input or sleep don't work"
        except Exception as e:
            self.ids.terminal.color = red
            self.ids.terminal.text = str(e)
            
    
    def create_file(self):
        name = "p%s.py" % (int(len(os.listdir(path))) + 1)
        if '%s' % name not in os.listdir(path):
            with open(path + name, "w"):
                pass

    def delete_file(self):
        name = os.path.basename(self.path)
        text = "Welcome"
        self.ids.codeinput.opacity = 0
        self.ids.codeinput.enabled = False
        if '%s' % name in os.listdir(path):
            os.remove(path + name)
            self.ids.filen.text = text