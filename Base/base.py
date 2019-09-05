import os
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=10, poll_frequency=1.0):
        """定位单个元素"""
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=10, poll_frequency=1.0):
        """定位一组元素"""
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """点击元素方法"""
        self.get_element(loc).click()

    def send_element(self, loc, text):
        """输入方法"""
        input_text = self.get_element(loc)
        # 清空输入框
        input_text.clear()
        # 输入内容
        input_text.send_keys(text)

    def scroll_screen(self, tag=1):
        """
        滑动操作
        :param tag: 1向上 2向下 3向左 4向右
        :return:
        """
        screen = self.driver.get_window_size()
        # 取宽
        width = screen.get("width")
        # 取高
        height = screen.get("height")
        time.sleep(2)

        if tag == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, duration=2000)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, duration=2000)
        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, duration=2000)
        if tag == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, duration=2000)

    def get_toast(self, message):
        """获取提示信息"""
        mess_xpath = "//*[contains(@text,'%s')]" % message
        return self.get_element((By.XPATH, mess_xpath), timeout=3, poll_frequency=0.3).text

    def get_screenshot(self):
        """截图方法"""
        png_name = "./image/" + os.sep + "%d.png" % int(time.time())
        self.driver.get_screenshot_as_file(png_name)
        with open(png_name, "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
