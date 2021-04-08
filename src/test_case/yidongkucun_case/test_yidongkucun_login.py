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

        #------------------------直接启动云苍穹个人首页，进入应用页-------------------------
        #从云苍穹个人首页进入应用首页
        self.login.click_login_yingyong()
        self.assertEqual(self.login.dy_login_yingyong, 1, '断言失败，从云苍穹个人首页进入应用首页失败')

        #从应用首页进入库存查询页
        self.login.click_login_yingyong_kccx()
        self.assertEqual(self.login.dy_login_yingyong_kccx, 1, '断言失败，从云苍穹个人首页进入应用首页失败')


        #---------判断是否登陆成功
        #查找右上角的方案按钮
        self.login.noclick_login_kccx_fangan()
        #如果查找成功，判断为成功
        if self.login.dy_no_login_kccx_fangan == 1:
            print("登陆成功")
        #如果查询不成功，判断为失败
        else:
            self.assertEqual(self.login.dy_no_login_kccx_fangan, 1, '断言失败，从云苍穹个人首页进入应用首页失败，test_case_1执行失败！')




    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()