from Base.base import BasePage
from Page.pageElement import PageElement

class GotoLoginPage(BasePage):
    """已有账号去登录页面"""
    def __init__(self,driver):
        BasePage.__init__(self,driver)
    #点击已有账号去登录
    def click_goto_login(self):
        self.click_element(PageElement.goto_login)