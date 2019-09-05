from Page.homePage import HomePage
from Page.gotoLoginPage import GotoLoginPage
from Page.loginPage import LoginPage
from Page.myHomePage import MyHomePage
from Page.settingPage import MySetting


class PortPage():
    """统一入口类"""
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        return HomePage(self.driver)

    def goto_login_page(self):
        return GotoLoginPage(self.driver)

    def login_page(self):
        return LoginPage(self.driver)

    def myhome_page(self):
        return MyHomePage(self.driver)

    def my_setting(self):
        return MySetting(self.driver)
