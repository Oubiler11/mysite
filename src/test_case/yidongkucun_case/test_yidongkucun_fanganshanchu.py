import pytest
import unittest
from src.data.data import *
from src.pages.yidongkucun import yidongkucun_login
from src.pages.yidongkucun import yidongkucun_search
from src.pages.yidongkucun import yidongkucun_fangan
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

class TestLong(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()


    def test_case_2(self):
        #引入页面元素
        self.login = yidongkucun_login.Login_page(self.driver)
        self.fangan = yidongkucun_fangan.search_page(self.driver)

        # ------------------------直接启动云苍穹个人首页，进入应用页-------------------------
        # 从云苍穹个人首页进入应用首页
        self.login.click_login_yingyong()

        # 从应用首页进入库存查询页
        self.login.click_login_yingyong_kccx()

        # ------------------------方案新增和切换-------------------------
        self.login.click_login_kccx_fangan()

        try:
            self.fangan.click_fangan_kccx_xinzengan()
            self.fangan.click_fangan_kccx_fanganminceng()
            self.fangan.send_fangan_kccx_fanganminceng()
            self.fangan.click_fangan_kccx_baocunan()
            print("新增方案成功")
        except:
            self.fangan.click_fangan_kccx_fanganminceng()
            self.fangan.send_fangan_kccx_fanganmincenggd()
            self.fangan.click_fangan_kccx_jinrucangku()
            self.fangan.click_fangan_kccx_xuanzecangku()
            self.fangan.click_fangan_kccx_baocuncangku()
            self.fangan.click_fangan_kccx_baocunan()
            print("第一次新增方案成功")


        try:
            self.login.click_login_kccx_fangan()
            i=1
            print("断言，新增方案成功")
        except:
            i=2
            print("断言，新增方案失败")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\test_case2_image.png")
        self.assertEqual(i, 1, '断言失败，方案新增失败，test_case_2执行异常')



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()