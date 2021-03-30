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

class TestLong1(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()


    def test_case_2(self):
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
        #断言：如果在用户登陆页，那么就输入账号密码进行登陆，如果已经是库存首页，输出进入首页成功
        try:
            self.login.click_land_username()
            self.login.send_land_username()

            self.login.click_land_password()
            self.login.send_land_password()

            self.login.click_land_denglu()
            print ("登陆成功")
            time.sleep (1)
        except:
            print ("库存首页登陆成功")
            time.sleep (1)

        #------------------------库存首页搜索--------------------------
        #点击搜索框
        self.search.click_kucun_shouye_search()
        #进行全量搜索
        self.search.click_kucun_shouye_truesearch()
        time.sleep(10)
        try:
            self.search.click_kucun_shouye_duanyan_search()
            print ("库存首页-搜索功能，执行成功")
        except:
            print ("库存首页-搜索功能，执行失败")



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()