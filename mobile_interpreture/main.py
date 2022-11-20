from mobile.md import UIApp, Container, Tab

import os


class MobileApp(UIApp):
    """ Mobile app сombines methods of two classes using inheritance """
    def __init__(self) -> None:
        super().__init__()
    
    def build(self) -> Container:
        return super().build()

    def on_start(self):
        for file in os.listdir(path="files")[::-1]:
            self.root.ids.tabs.add_widget(Tab(title="%s" % file))

    # Change
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        self.root.ids.tabs.title = tab_text
        

def main():
    mobile = MobileApp()
    mobile.run()


if __name__ == "__main__":
    main()