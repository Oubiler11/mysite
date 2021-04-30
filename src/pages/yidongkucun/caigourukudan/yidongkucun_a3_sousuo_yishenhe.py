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


class buxian_page(Base_page.Base_page):
    by = mobileby.MobileBy ()

    # --------------------下拉菜单，选择不限------------------
    # 暂存选项（通过xpath进行定位）
    cgrk_shouye_zancun= (by.XPATH, "//*[@class='android.view.View'][@index='5'][@content-desc='暂存']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_zancun(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_zancun).click()
            self.dy_cgrk_shouye_zancun = 1
            print("暂存选项点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_zancun = 2
            print("暂存选项点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_zancun.png")

    # 业务日期（通过xpath进行定位）
    cgrk_shouye_yewuriqi = (by.XPATH, "//*[@class='android.view.View'][@content-desc='本周']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_yewuriqi(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_yewuriqi).click()
            self.dy_cgrk_shouye_yewuriqi = 1
            print("业务日期点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_yewuriqi = 2
            print("业务日期点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_yewuriqi.png")

    # 业务日期（通过xpath进行定位）
    cgrk_shouye_yewuriqi_buxian = (by.XPATH, "//*[@class='android.view.View'][@index='3'][@content-desc='不限']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_yewuriqi_buxian(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_yewuriqi_buxian).click()
            self.dy_cgrk_shouye_yewuriqi_buxian = 1
            print("不限点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_yewuriqi_buxian = 2
            print("不限点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_yewuriqi.png")

    # 判断页面是否存在已审核按钮（通过xpath进行定位）
    cgrk_yingyong_yishenhe = (by.XPATH, "//*[@class='android.view.View'][@content-desc='已审核']")

    # 封装操作（不操作，只是进行定位）
    def noclick_cgrk_yingyong_yishenhe(self):
        # 判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.cgrk_yingyong_yishenhe)
            self.dy_no_cgrk_yingyong_yishenhe = 1
            print ("test_case,执行成功")
        # 如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_no_cgrk_yingyong_yishenhe = 2
            print ("test_case,执行失败")
            self.driver.get_screenshot_as_file (
                "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\noclick_cgrk_yingyong_yishenhe.png")













