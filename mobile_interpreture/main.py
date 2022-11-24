from mobile.md import UIApp

import os


class MobileApp(UIApp):
    """ Mobile app сombines methods of two classes using inheritance """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        if "mobile_interpreture" not in os.listdir():
            os.mkdir("mobile_interpreture")
        if "assets" not in os.listdir(path="mobile_interpreture"):
            os.mkdir("mobile_interpreture/assets")
        if len(os.listdir(path="mobile_interpreture/assets")) == 0:
            with open("mobile_interpreture/assets/p1.py", "w"):
                pass
        
    
    def build(self):
        return super().build()


def main():
    mobile = MobileApp()

    mobile.run()


if __name__ == "__main__":
    main()