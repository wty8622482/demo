from Base.base import BasePage
from Page.pageElement import PageElement


class MySetting(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)


    def click_back_btn(self,tar=1):
        # 向上滑动页面
        self.scroll_screen()
        #点击退出
        self.click_element(PageElement.setting_go_back)
        # 点击退出按钮 1确认退出 2取消
        if tar == 1:
            self.click_element(PageElement.setting_affirm_btn)
        else:
            self.click_element(PageElement.setting_cancle_btn)

    # def click_setting_cancle_btn(self):
    #     self.click_element(PageElement.setting_cancle_btn)
