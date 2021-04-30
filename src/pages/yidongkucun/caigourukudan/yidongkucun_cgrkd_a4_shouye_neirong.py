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


class neirong_page(Base_page.Base_page):
    by = mobileby.MobileBy ()

    # --------------------点击任意的入库单------------------
    # 点击订单内容（通过xpath进行定位）
    cgrk_shouye_dingdan_neirong = (by.XPATH, "//*[@class='android.view.View'][@content-desc='仓库：']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_dingdan_neirong(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_dingdan_neirong).click()
            self.dy_cgrk_shouye_dingdan_neirong = 1
            print("点击订单内容点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_dingdan_neirong = 2
            print("点击订单内容点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_dingdan_neirong.png")

