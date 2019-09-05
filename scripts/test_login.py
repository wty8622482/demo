import sys, os

from selenium.common.exceptions import TimeoutException

sys.path.append(os.getcwd())
import pytest
from Base.getDriver import get_android_driver
from Base.getPort import PortPage
from Base.getData import GetData


def date():
    # 成功数据列表
    suc_list = []
    # 失败数据列表
    fail_list = []
    # 实例化数据读取文件
    value = GetData().get_yml_data("login_data.yml")
    for i in value.keys():
        if value.get(i).get("toast"):
            fail_list.append((i, value.get(i).get("user"), value.get(i).get("pwd"),
                              value.get(i).get("toast"), value.get(i).get("excep")))
        else:
            suc_list.append((i, value.get(i).get("user"), value.get(i).get("pwd"),
                             value.get(i).get("excep")))
    return {"suc": suc_list, "fail": fail_list}



class TestLogin:
    def setup_class(self):
        """初始化Android驱动"""
        self.port_page = PortPage(get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))
        self.port_page.get_home_page().close_update()

    def teardown_class(self):
        """关闭驱动"""
        self.port_page.driver.quit()

    def login_out(self):
        """个人中心——>退出"""
        self.port_page.myhome_page().click_my_setting()
        self.port_page.my_setting().click_back_btn()

    @pytest.fixture(autouse=True)
    def goto_login_page(self):
        #点击我
        self.port_page.get_home_page().click_my_home_btn()
        #点击已有账号去登陆
        self.port_page.goto_login_page().click_goto_login()

    @pytest.mark.parametrize("case_num, user, pwd, excep", date().get("suc"))
    def test_login_suc(self, case_num, user, pwd, excep):
        """正向用列方法"""
        # 登录
        self.port_page.login_page().login_users(user, pwd)
        try:
            # 我的收藏-查找
            my_collecr = self.port_page.myhome_page().get_my_collect()
            try:
            # 断言
                assert my_collecr == excep
            except AssertionError:
                self.port_page.myhome_page().get_screenshot()
                assert False
            finally:
                self.login_out()
        # 退出操作
        except TimeoutException:
            # 截图
            self.port_page.login_page().get_screenshot()
            # 判断登录按钮
            if  self.port_page.login_page().find_login_btn():
            # 关闭登录页面
                self.port_page.login_page().close_login_btn()
            else:
            # 退出操作
                self.login_out()
            assert  False

    @pytest.mark.parametrize("case_num, user, pwd, toast, excep", date().get("fail"))
    def test_login_fail(self, case_num, user, pwd, toast, excep):
        """反向用列方法"""
        #登录
        self.port_page.login_page().login_users(user,pwd)
        try:
            #获取toast消息
            message =  self.port_page.login_page().get_toast(toast)
            #断言toast
            try:
                #断言成功
                assert message == excep
            except AssertionError:
                #断言失败   截图
                self.port_page.login_page().get_screenshot()
                assert False
        except TimeoutException:
            #找不到toast消息
            #截图
            self.port_page.login_page().get_screenshot()
            assert False
        finally:
            try:
                #断言登录按钮
                assert self.port_page.login_page().find_login_btn()
                #关闭登录页面
                self.port_page.login_page().close_login_btn()
            except AssertionError:
                #不在登录页面 截图
                self.port_page.login_page().get_screenshot()
                #退出操作
                self.login_out()
                assert False




