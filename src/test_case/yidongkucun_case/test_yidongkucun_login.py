import pytest
import unittest
from src.data.data import *
from src.pages.yidongkucun import yidongkucun_login
from src.pages.yidongkucun import yidongkucun_search
from src.common import driver_config
from config.globalparameter import img_name
from appium import webdriver
# noinspection PyUnresolvedReferences
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType
from appium.webdriver.extensions.android.nativekey import AndroidKey
# noinspection PyUnresolvedReferences
import time
import unittest#引用自动化测试框架
import os
# noinspection PyUnresolvedReferences
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import HTMLTestRunner
import random
from src.common import Base_page
from appium.webdriver.common import mobileby

class TestLong(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()


    def test_case_1(self):
        #引入页面元素
        self.login = yidongkucun_login.Login_page(self.driver)
        self.search = yidongkucun_search.search_page(self.driver)

        #------------------------从搜狗首页进入库存首页-------------------------
        #搜狗首页-点击网址栏
        self.login.click_sougou_website_button()
        #网址页点击网址栏
        self.login.click_sougou_website_column()
        #网址栏输入网址
        self.login.send_sougou_website_column()
        #点击前往
        self.login.click_sougou_website_qianwang()
        #判断：如果在用户登陆页，那么就输入账号密码进行登陆，如果已经是库存首页，输出进入首页成功
        try:
            #点击和输入用户名
            self.login.click_land_username()
            self.login.send_land_username()

            #点击和输入密码
            self.login.click_land_password()
            self.login.send_land_password()

            #点击登陆
            self.login.click_land_denglu()
            print("登陆成功")
        except:
            print("库存首页登陆成功")

            self.login.test_land_denglu()

        try:
            self.login.click_land_username()
            i = 1
            print("首页方案按钮获取成功")
        except:
            i = 2
            print("首页方案按钮获取失败")


        self.assertEqual(i,1,'断言失败，未成功登陆首页，test_case_1执行异常')



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()