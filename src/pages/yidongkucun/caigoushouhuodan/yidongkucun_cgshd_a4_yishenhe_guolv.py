'''
页面;登录页面
'''
from appium.webdriver.webdriver import WebDriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from src.common import Base_page
from appium.webdriver.common import mobileby
import random
import time


class yishenhe (Base_page.Base_page,unittest.TestCase):
    by = mobileby.MobileBy ()

    # ------------------------采购收货单页面------------------------
    # 采购收货单-下拉菜单-已提交图标（通过xpath进行定位）
    cgshd_yishenhe_guolv = (by.XPATH, "//*[@class='android.view.View'][@content-desc='已审核'][@index='9']")

    # 封装操作（点击操作）
    def click_cgshd_yishenhe_guolv(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgshd_yishenhe_guolv).click()
            self.dy_cgshd_yishenhe_guolv = 1
            print("下拉菜单-已审核图标，点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgshd_yishenhe_guolv = 2
            print("下拉菜单-已审核图标，点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgshd_yishenhe_guolv.png")
