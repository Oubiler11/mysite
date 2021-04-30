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


class wushuju_page(Base_page.Base_page):
    by = mobileby.MobileBy()

    # --------------------仓库过滤------------------
    # 下拉菜单栏的仓库选项
    cgrk_cangku_guolv_youshuju = (by.XPATH, "//*[@class='android.view.View'][@index='9']")

    def click_cgrk_cangku_guolv_youshuju(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_cangku_guolv_youshuju).click()
            self.dy_cgrk_cangku_guolv_youshuju= 1
            print("仓库选项点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_cangku_guolv_youshuju= 2
            print("仓库选项点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_cangku_guolv_youshuju.png")

    # 仓库搜索栏
    cgrk_cangku_guolv_sousuo = (by.XPATH, "//*[@class='android.widget.EditText'][@text='请搜索供应商名称/库管员/单据编号']")

    def click_cgrk_cangku_guolv_sousuo(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_cangku_guolv_sousuo).click()
            self.dy_cgrk_cangku_guolv_sousuo = 1
            print("搜索栏点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_cangku_guolv_sousuo = 2
            print("搜索栏点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_cangku_guolv_youshuju.png")

    # 输入搜索内容
    cgrk_cangku_guolv_sousuo = (by.XPATH, "//*[@class='android.widget.EditText'][@index='0']")

    def click_cgrk_cangku_guolv_sousuo(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_cangku_guolv_sousuo).click()
            self.dy_cgrk_cangku_guolv_sousuo = 1
            print("搜索栏点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_cangku_guolv_sousuo = 2
            print("搜索栏点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_cangku_guolv_youshuju.png")


    # 再次点击搜索框
    cgrk_cangku_guolv_dianjisousuo = (by.XPATH, "//*[@class='android.widget.EditText'][@text='搜索']")


    def send_cgrk_cangku_guolv_dianjisousuo(self,sousuo="cdy"):
        #判断能否进行输入操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.send_keys(sousuo, *self.cgrk_cangku_guolv_dianjisousuo)
            self.dy_send_cgrk_cangku_guolv_dianjisousuo = 1
            print("搜索内容输入成功")
        #如果不能进行输入操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_send_cgrk_cangku_guolv_dianjisousuo = 2
            print("搜索内容输入失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\send_cgrk_cangku_guolv_dianjisousuo.png")

    # 点击cdy深圳
    cgrk_cangku_guolv_cdyshenzhen = (by.XPATH, "//*[@class='android.view.View'][@content-desc='cdy深圳仓']")

    def click_cgrk_cangku_guolv_cdyshenzhen(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_cangku_guolv_cdyshenzhen).click()
            self.dy_cgrk_cangku_guolv_cdyshenzhen = 1
            print("cdy深圳点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_cangku_guolv_cdyshenzhen = 2
            print("cdy深圳点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_cangku_guolv_cdyshenzhen.png")

    # 点击确定按钮
    cgrk_cangku_guolv_queding = (by.XPATH, "//*[@class='android.view.View'][@resource-id='confirm']")

    def click_cgrk_cangku_guolv_queding (self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_cangku_guolv_queding).click()
            self.dy_cgrk_cangku_guolv_queding = 1
            print("确定按钮点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_cangku_guolv_queding = 2
            print("确定按钮点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_cangku_guolv_queding .png")