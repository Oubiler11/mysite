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


class Login_page (Base_page.Base_page,unittest.TestCase):
    by = mobileby.MobileBy ()

    #通过云之家进入
    #移动库存（通过ID进行定位）
    cq_yunzhijia_yidongkucun = (by.XPATH, "//*[@resource-id='com.kdweibo.client:id/ic_app_name'][@text='移动库存_b1']")

    # 封装操作（点击操作）
    def click_cq_yunzhijia_yidongkucun (self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.cq_yunzhijia_yidongkucun ).click()
            self.dy_cq_yunzhijia_yidongkucun = 1
            print("移动库存点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cq_yunzhijia_yidongkucun  = 2
            print("移动库存点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\cq_yunzhijia_yingyong.png")







    # ------------------------采购收货单页面------------------------
    # 采购收货图标（通过xpath进行定位）
    cgshd_yingyong_tubiao = (by.XPATH, "//*[@class='android.view.View'][@content-desc='收货单']")

    # 封装操作（点击操作）
    def click_cgshd_yingyong_tubiao(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgshd_yingyong_tubiao).click()
            self.dy_cgshd_yingyong_tubiao = 1
            print("采购收货单点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgshd_yingyong_tubiao = 2
            print("采购收货单点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgshd_yingyong_tubiao.png")

