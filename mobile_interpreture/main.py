from mobile.logic import Interpreture
from mobile.interface import InterpretureApp
from mobile.interface import Container
from kivy.config import Config


Config.set("kivy", "keyboardmode", 
"systemandnock")

class MobileApp(InterpretureApp):
    """ Mobile app сombines methods of two classes using inheritance """
    def __init__(self) -> None:
        super().__init__()
    
    def build(self) -> Container:
        return super().build()


def main():
    mobile = MobileApp()
    mobile.run()


if __name__ == "__main__":
    main()