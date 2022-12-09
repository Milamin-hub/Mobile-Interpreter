from View.inter import InterpretureView
from kivymd.app import MDApp
import os


class InterpretureApp(MDApp):

    running = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        if "mobile_interpreture" not in os.listdir():
            os.mkdir("mobile_interpreture")
        if "assets" not in os.listdir(path="mobile_interpreture"):
            os.mkdir("mobile_interpreture/assets")
        
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return InterpretureView()

    def on_stop(self):
        self.running = False


if __name__ == '__main__':
    InterpretureApp().run()