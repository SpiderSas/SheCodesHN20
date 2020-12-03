from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class P(FloatLayout):
    pass


class B(FloatLayout):
    pass


def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()


class ReportWindow(Screen):
    dia_chi = ObjectProperty(None)
    su_viec = ObjectProperty(None)
    str = " "

    def btn(self):
        show_popup()
        self.str = self.dia_chi.text + " " + ":" + " " + self.su_viec.text
        file = open("dtbase.txt", "a")
        file.write(self.str + "\n")
        file.close()
        self.dia_chi.text = " "
        self.su_viec.text = " "


class WatchWindow(Screen):
    text = Label()

    def Xem(self):
        show_popup()

    def texting(self):
        file = open("dtbase.txt", "r")
        self.text = file.read()
        return self.text


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("your.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
