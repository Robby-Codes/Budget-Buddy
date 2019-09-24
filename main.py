from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    pass


class ForgotScreen(Screen):
    pass


class DashboardScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('gui.kv')


class BudgetBuddyApp(App):
    def build(self):
        self.title = 'Budget Buddy'
        return kv


if __name__ == '__main__':
    Config.set('graphics', 'window_state', 'maximized')
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    BudgetBuddyApp().run()
