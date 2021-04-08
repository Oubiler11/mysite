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

    # -------------金蝶云苍穹个人首页的元素组件和实际操作封装-----------
    # 应用按钮（通过ID进行定位）
    login_yingyong = (by.ID, "com.kdweibo.client:id/iv_app_store")

    # 封装操作（点击操作）
    def click_login_yingyong(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_yingyong).click ()
            self.dy_login_yingyong = 1
            print ("应用按钮点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_login_yingyong = 2
            print ("应用按钮点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_login_yingyong_image.png")




    # -------------应用首页的元素组件和实际操作封装---------------------
    # 库存查询入口（通过ID进行定位）
    login_yingyong_kccx = (by.XPATH, "//*[@resource-id='com.kdweibo.client:id/ic_app_name'][@text='库存查询']")

    # 封装操作（点击操作）
    def click_login_yingyong_kccx(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_yingyong_kccx).click()
            self.dy_login_yingyong_kccx = 1
            print ("库存查询入口点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_login_yingyong_kccx = 2
            print ("库存查询入口失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_login_yingyong_kccx_image.png")


    # 移动库存入口（通过ID进行定位）
    login_yingyong_ydkc = (by.XPATH, "//*[@resource-id='com.kdweibo.client:id/ic_app_name'][@text='移动库存']")

    # 封装操作（点击操作）
    def click_login_yingyong_ydkc(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_yingyong_ydkc).click()
            self.dy_login_yingyong_ydkc = 1
            print ("移动库存入口点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.login_yingyong_ydkc = 2
            print ("移动库存入口点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_login_yingyong_ydkc_image.png")


    # 移动协同入口（通过ID进行定位）
    login_yingyong_ydgyxt = (by.XPATH, "//*[@resource-id='com.kdweibo.client:id/ic_app_name'][@text='移动供应协同']")

    # 封装操作（点击操作）
    def click_login_yingyong_ydgyxt(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_yingyong_ydgyxt).click()
            self.dy_login_yingyong_ydgyxt = 1
            print ("移动协同入口点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.login_yingyong_ydgyxt = 2
            print ("移动协同入口点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\click_login_yingyong_ydgyxt.png")


    # 移动采购协同入口（通过ID进行定位）
    login_yingyong_ydcgxt = (by.XPATH, "//*[@resource-id='com.kdweibo.client:id/ic_app_name'][@text='移动采购协同']")

    # 封装操作（点击操作）
    def click_login_yingyong_ydcgxt(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_yingyong_ydcgxt).click()
            self.dy_login_yingyong_ydcgxt = 1
            print ("移动采购协同入口点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.login_yingyong_ydcgxt = 2
            print ("移动采购协同入口点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\click_login_yingyong_ydcgxt.png")




    # -------------库存查询的元素组件和实际操作封装-----------
    # 库存查询首页的搜索框（通过class和text进行定位）
    login_kccx_sousuo = (by.XPATH, "//*[@class='android.widget.EditText'][@text='请搜索物料名称/物料编码']")

    # 封装操作（点击操作）
    def click_login_kccx_sousuo(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_kccx_sousu).click()
            self.dy_login_kccx_sousu = 1
            print ("库存查询首页的搜索框点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.login_kccx_sousu = 2
            print ("库存查询首页的搜索框点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_login_kccx_sousu.png")

    # 封装操作（不操作，只是进行定位）
    def noclick_login_kccx_sousuo(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_kccx_sousu).click()
            self.dy_no_login_kccx_sousu = 1
            print ("库存查询首页的搜索框定位成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_no_login_kccx_sousu = 2
            print ("库存查询首页的搜索框定位失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\noclick_login_kccx_sousu.png")

    # 库存查询首页右上角的方案图标
    login_kccx_fangan = (by.XPATH, "//*[@class='android.view.View'][@index='3']")

    # 封装操作（点击操作）
    def click_login_kccx_fangan(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_kccx_fangan).click()
            self.dy_login_kccx_fangan = 1
            print ("库存查询首页右上角的方案图标点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.login_kccx_fangan = 2
            print ("库存查询首页右上角的方案图标点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_login_kccx_fangan.png")

    # 封装操作（不操作，只是进行定位）
    def noclick_login_kccx_fangan(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.login_kccx_fangan).click()
            self.dy_no_login_kccx_fangan = 1
            print ("库存查询首页右上角的方案图标定位成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_no_login_kccx_fangan= 2
            print ("库存查询首页右上角的方案图标定位失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\noclick_login_kccx_fangan.png")
