'''
页面;方案页面
'''

from appium.webdriver.webdriver import WebDriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from src.common import Base_page
from appium.webdriver.common import mobileby
import random
import time


class dingdan_page(Base_page.Base_page):
    by = mobileby.MobileBy ()

    # --------------------点击任意的入库单------------------
    # 暂存订单详情里面的提交按钮
    cgrk_shouye_zancun_tijiao = (by.XPATH, "//*[@class='android.view.View'][@content-desc='提交']")

    def click_cgrk_shouye_zancun_tijiao(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_zancun_tijiao).click()
            self.dy_cgrk_shouye_zancun_tijiao = 1
            print("提交按钮点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_zancun_tijiao = 2
            print("提交按钮点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_zancun_tijiao.png")

