from mobile.logic import Interpreture
from mobile.interface import InterpretureApp


class MobileApp(InterpretureApp, Interpreture):
    """ Mobile app сombines methods of two classes using inheritance """
    def __init__(self) -> None:
        super().__init__()


def main():
    mobile = MobileApp()
    mobile.run()


if __name__ == "__main__":
    main()