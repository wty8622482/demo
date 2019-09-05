from selenium.webdriver.common.by import By


class PageElement(object):
    """登录页面元素"""
    """首页"""
    #跳过
    # home_skip = (By.ID,"com.yunmall.lc: id / view_mask")
    home_close = (By.ID,"com.yunmall.lc:id/img_close")
    home_my_btn = (By.ID, "com.yunmall.lc:id/tab_me")

    """去登陆页面"""
    #已有账号去登陆
    goto_login = (By.ID, "com.yunmall.lc:id/textView1")

    """登录页"""
    #用户名
    login_username = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    #密码
    login_password = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    #登录按钮
    login_btn = (By.ID, "com.yunmall.lc:id/logon_button")
    #关闭登录页面按钮
    login_close = (By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """个人中心页面"""
    #我的收藏
    my_collect = (By.ID, "com.yunmall.lc:id/txt_my_shoppingcart")
    #设置
    my_setting = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """设置页面"""
    #退出
    setting_go_back = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 退出
    setting_affirm_btn = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    # 取消
    setting_cancle_btn = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
