from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class InterpretureApp(App):
    """ Interface app """
    def __init__(self) -> None:
        super().__init__()

    def create_button(self, txt, btn, font_s=30):
        """ Build button on interface"""
        return Button(
            text=txt,
            font_size=font_s,
            on_press = btn
        )

    def build(self) -> BoxLayout:
        """ Build button on interface"""
        bl = BoxLayout()
        btn1 = self.create_button("button", self.btn_press)
        btn2 = self.create_button("button 2", self.btn_press)
        bl.add_widget(btn1)
        bl.add_widget(btn2)
        return bl
    
    def btn_press(self, instance) -> None:
        """ 
        If you press the button, the function is activated 

        :param instance: Handling a button click
        """
        pass


if __name__ == '__main__':
    InterpretureApp().run()