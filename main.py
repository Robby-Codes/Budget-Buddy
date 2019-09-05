from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('gui.kv')

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class BudgetBuddyApp(App):
    def build(self):
        self.title = 'Budget Buddy'
        return kv


if __name__ == '__main__':
    BudgetBuddyApp().run()
