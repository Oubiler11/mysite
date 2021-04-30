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


class guolv_page(Base_page.Base_page):
    by = mobileby.MobileBy()

    # --------------------点击任意的入库单------------------
    # 订单状态下拉列表里面的暂存选项
    cgrk_shouye_tijiao_zancun = (by.XPATH, "//*[@class='android.view.View'][@content-desc='暂存'][@index='5']")

    def click_cgrk_shouye_tijiao_zancun(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_tijiao_zancun).click()
            self.dy_cgrk_shouye_tijiao_zancun= 1
            print("暂存选项点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_tijiao_zancun = 2
            print("暂存选项点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_tijiao_zancun .png")


    # 订单状态下拉列表里面的提交选项
    cgrk_shouye_tijiao_tijiao = (by.XPATH, "//*[@class='android.view.View'][@content-desc='已提交']")

    def click_cgrk_shouye_tijiao_tijiao(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_tijiao_tijiao).click()
            self.dy_cgrk_shouye_tijiao_tijiao = 1
            print("提交选项点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_tijiao_tijiao = 2
            print("提交选项点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_tijiao_tijiao .png")


    # 订单状态下拉列表里面的确定选项
    cgrk_shouye_tijiao_queding = (by.XPATH, "//*[@class='android.view.View'][@content-desc='确定']")

    def click_cgrk_shouye_tijiao_queding(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_tijiao_queding).click()
            self.dy_cgrk_shouye_tijiao_queding = 1
            print("确定选项点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_tijiao_queding = 2
            print("确定选项点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_tijiao_queding.png")

    # 已提交选项断言
    cgrk_shouye_tijiao_yitijiao = (by.XPATH, "//*[@class='android.view.View'][@content-desc='已提交']")

    def click_cgrk_shouye_tijiao_yitijiao(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_tijiao_yitijiao).click()
            self.dy_cgrk_shouye_tijiao_yitijiao= 1
            print("test_case,执行成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_tijiao_yitijiao= 2
            print("test_case,执行失败")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_tijiao_queding.png")