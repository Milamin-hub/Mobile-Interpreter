from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class InterpretureApp(App):
    """ Interface app """
    def __init__(self) -> None:
        super().__init__()

    def build(self) -> Button:
        """ Build button on interface"""
        return Button(
            text="button",
            font_size=30,
            on_press = self.btn_press
        )
    
    def btn_press(self, instance) -> None:
        """ 
        If you press the button, the function is activated 

        :param instance: Handling a button click
        """
        pass


if __name__ == '__main__':
    InterpretureApp().run()