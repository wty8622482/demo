from Base.base import BasePage
from Page.pageElement import PageElement

class LoginPage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def login_users(self,uesrname,password):
        """登陆页面"""
        self.send_element(PageElement.login_username,uesrname)
        self.send_element(PageElement.login_password,password)
        self.click_element(PageElement.login_btn)

    def find_login_btn(self):
        """判断登陆按钮"""
        try:
            self.get_element(PageElement.login_btn)
            return True
        except:
            return False

    def close_login_btn(self):
        """关闭登陆页面"""
        self.click_element(PageElement.login_close)