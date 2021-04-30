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


class chexiao_page(Base_page.Base_page):
    by = mobileby.MobileBy()

    # --------------------点击任意的入库单------------------
    # 订单状态下拉列表里面的暂存选项
    cgrk_shouye_tijiao_chexiao_dingdan = (by.XPATH, "//*[@class='android.view.View'][@content-desc='已提交'][@resource-id='labelapsubmit']")

    def click_cgrk_shouye_tijiao_chexiao_dingdan(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_tijiao_chexiao_dingdan).click()
            self.dy_cgrk_shouye_tijiao_chexiao_dingdan= 1
            print("已提交点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_tijiao_chexiao_dingdan = 2
            print("已提交点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_tijiao_chexiao_dingdan.png")

    #提交订单的撤回
    cgrk_shouye_tijiao_chexiao_chehui = (by.XPATH, "//*[@class='android.view.View'][@content-desc='撤销']")

    def click_cgrk_shouye_tijiao_chexiao_chehui (self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_tijiao_chexiao_chehui ).click()
            self.dy_cgrk_shouye_tijiao_chexiao_chehui = 1
            print("撤回点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_tijiao_chexiao_chehui  = 2
            print("撤回点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_tijiao_chexiao_chehui.png")