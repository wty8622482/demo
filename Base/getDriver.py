from appium import webdriver

"""手机驱动对象"""


def get_android_driver(pac, act):
    """
    返回android手机驱动对象
    :param pac: 包名
    :param act: 启动名
    :return: 返回手机驱动对象
    """
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['automationName'] = 'Uiautomator2'
    # app的信息
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act

    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)