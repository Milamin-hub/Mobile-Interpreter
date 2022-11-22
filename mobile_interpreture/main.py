from mobile.md import UIApp

import os


class MobileApp(UIApp):
    """ Mobile app сombines methods of two classes using inheritance """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def build(self):
        return super().build()


def main():
    mobile = MobileApp()
    mobile.run()


if __name__ == "__main__":
    main()