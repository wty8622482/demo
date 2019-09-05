import sys,os
sys.path.append(os.getcwd())
from Base.getDriver import get_android_driver
import allure

class Test_001:
    def test_001(self):
        driver = get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        driver.get_screenshot_as_file("./image/jietu.png")

        #添加图片  添加描述信息text
        with open("./image/jietu.png","rb") as f:
            allure.attach("jietu",f.read(),allure.attach_type.PNG)
            assert True


