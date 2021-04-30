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


class tijiao_page(Base_page.Base_page):
    by = mobileby.MobileBy ()

    # --------------------点击任意的入库单------------------
    # 采购入库单列表，暂存的订单（通过xpath进行定位）
    cgrk_shouye_zancun_shanchu = (by.XPATH, "//*[@resource-id='labelapsave'][@content-desc='暂存']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_zancun_shanchu(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_zancun_shanchu).click()
            self.dy_cgrk_shouye_zancun_shanchu = 1
            print("暂存的订单点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_zancun_shanchu = 2
            print("暂存的订单点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_zancun_shanchu.png")


    # 暂存订单详情里面的保存按钮
    cgrk_shouye_zancun_baocun = (by.XPATH, "//*[@class='android.view.View'][@content-desc='保存'][@index='3']")

    def click_cgrk_shouye_zancun_baocun(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_zancun_baocun).click()
            self.dy_cgrk_shouye_zancun_baocun = 1
            print("保存按钮点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_zancun_baocun = 2
            print("保存按钮点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_zancun_baocun.png")

