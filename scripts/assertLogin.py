import time

from selenium.webdriver.common.by import By

from Base.getDriver import get_android_driver
from Base.getPort import PortPage

# 声明driver
driver = get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")

# 实例化统一入口类
port_page = PortPage(driver)

port_page.get_home_page().close_update()

#点击我
port_page.get_home_page().click_my_home_btn()

#点击登录已有账号
port_page.goto_login_page().click_goto_login()

#登录操作
port_page.login_page().login_users("18221628089","8622482wty")
print(port_page.login_page().get_toast("错误"))

# #获取我的收藏
# port_page.myhome_page().get_my_collect()
# #点击设置
# port_page.myhome_page().click_my_setting()
# #退出登录
# port_page.my_setting().click_back_btn()
#退出driver
time.sleep(2)
driver.quit()