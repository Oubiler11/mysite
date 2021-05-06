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


class guolv (Base_page.Base_page,unittest.TestCase):
    by = mobileby.MobileBy ()

    # ------------------------采购收货单页面------------------------
    # 采购收货单-下拉菜单-已提交图标（通过xpath进行定位）
    cgshd_yitijiao_guolv = (by.XPATH, "//*[@class='android.view.View'][@content-desc='已提交'][@index='3']")

    # 封装操作（点击操作）
    def click_cgshd_yitijiao_guolv(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgshd_yitijiao_guolv).click()
            self.dy_cgshd_yitijiao_guolv = 1
            print("下拉菜单-已提交图标，点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgshd_yitijiao_guolv = 2
            print("下拉菜单-已提交图标，点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgshd_yitijiao_guolv.png")


    # 采购收货单-暂存菜单-已提交图标（通过xpath进行定位）
    cgshd_zancun_guolv = (by.XPATH, "//*[@class='android.view.View'][@content-desc='暂存'][@index='5']")

    # 封装操作（点击操作）
    def click_cgshd_zancun_guolv(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgshd_zancun_guolv).click()
            self.dy_cgshd_zancun_guolv = 1
            print("下拉菜单-暂存图标，点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgshd_zancun_guolv = 2
            print("下拉菜单-暂存图标，点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgshd_zancun_guolv.png")


    # 采购收货单-下拉列表-已提交图标（通过xpath进行定位）
    cgshd_yitijiao_xialaliebiao = (by.XPATH, "//*[@class='android.view.View'][@content-desc='已提交'][@index='7']")

    # 封装操作（点击操作）
    def click_cgshd_yitijiao_xialaliebiao(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgshd_yitijiao_xialaliebiao).click()
            self.dy_cgshd_yitijiao_xialaliebiao = 1
            print("下拉列表-已提交图标，点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgshd_yitijiao_xialaliebiao= 2
            print("下拉列表-已提交图标，点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgshd_yitijiao_xialaliebiao.png")


    # 采购收货单-下拉列表-确认图标（通过xpath进行定位）
    cgshd_queding_xialaliebiao = (by.XPATH, "//*[@class='android.view.View'][@content-desc='确定'][@index='11']")

    # 封装操作（点击操作）
    def click_cgshd_queding_xialaliebiao(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgshd_queding_xialaliebiao).click()
            self.dy_cgshd_queding_xialaliebiao = 1
            print("下拉列表-确定按钮，点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgshd_queding_xialaliebiao = 2
            print("下拉列表-确定按钮，点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgshd_yitijiao_xialaliebiao.png")


    # 采购收货单-下拉菜单-本周图标（通过xpath进行定位）
    cgshd_benzhou_xialacaidan = (by.XPATH, "//*[@class='android.view.View'][@content-desc='本周'][@index='7']")

    # 封装操作（点击操作）
    def click_cgshd_benzhou_xialacaidan(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgshd_benzhou_xialacaidan).click()
            self.dy_cgshd_benzhou_xialacaidan = 1
            print("下拉菜单-本周按钮，点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgshd_benzhou_xialacaidan = 2
            print("下拉菜单-本周按钮，点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgshd_benzhou_xialacaidan.png")

    # 采购收货单-下拉列表-不限图标（通过xpath进行定位）
    cgshd_buxian_xialaliebiao_sj= (by.XPATH, "//*[@class='android.view.View'][@content-desc='不限']")

    # 封装操作（点击操作）
    def click_cgshd_buxian_xialaliebiao_sj(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgshd_buxian_xialaliebiao_sj).click()
            self.dy_cgshd_buxian_xialaliebiao_sj = 1
            print("下拉菜单-本周按钮，点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgshd_buxian_xialaliebiao_sj = 2
            print("下拉菜单-本周按钮，点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgshd_buxian_xialaliebiao_sj.png")