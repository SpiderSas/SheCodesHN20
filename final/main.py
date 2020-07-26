# Demo ver only

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    dateofbirth = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


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


class MainWindow(Screen):
    def logOut(self):
        sm.current = "login"
    pass


class EventsWindow(Screen):
    pass


class ProfileWindow(Screen):
    pass


class NotificationsWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Khong hop le',
                  content=Label(text='Email hoac mat khau khong hop le.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Khong hop le',
                content=Label(text="Can dien day du thong tin hop le de dang ki tai khoan."),
                size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"), EventsWindow(name="events"), ProfileWindow(name="profile"), NotificationsWindow(name="notifications"), ReportWindow(name="report"), WatchWindow(name="watch")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class AncoraApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    AncoraApp().run()
