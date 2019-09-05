from Base.base import BasePage
from Page.pageElement import PageElement

class MyHomePage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_my_collect(self):
        return self.get_element(PageElement.my_collect).text

    def click_my_setting(self):
        self.click_element(PageElement.my_setting)

