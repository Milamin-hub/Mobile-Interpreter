from mobile.logic import Interpreture
from mobile.md import UIApp, Container

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

import os


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MobileApp(UIApp):
    """ Mobile app сombines methods of two classes using inheritance """
    def __init__(self) -> None:
        super().__init__()
    
    def build(self) -> Container:
        return super().build()

    def on_start(self):
        for file in os.listdir(path="files"):
            self.root.ids.tabs.add_widget(Tab(title="%s" % file))

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        file = open('files/%s' % tab_text, "r").readlines()
        text = ""
        for i in file:
            text += i
        instance_tab.ids.label.text = text


def main():
    mobile = MobileApp()
    mobile.run()


if __name__ == "__main__":
    main()