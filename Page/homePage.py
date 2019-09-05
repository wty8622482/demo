from Base.base import BasePage
from Page.pageElement import PageElement

class HomePage(BasePage):
    """首页"""
    def __init__(self, driver):
        BasePage.__init__(self, driver)
    #关闭更新
    def close_update(self):
        try:
            self.click_element(PageElement.home_close)
        except:
            pass
    #点击我的
    def click_my_home_btn(self):
        self.click_element(PageElement.home_my_btn)



