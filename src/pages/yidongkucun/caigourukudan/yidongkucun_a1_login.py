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
    #云之家应用按钮（通过ID进行定位）
    cq_yunzhijia_yingyong = (by.ID,"com.kdweibo.client:id/iv_app_store")

    # 封装操作（点击操作）
    def click_cq_yunzhijia_yingyong(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.cq_yunzhijia_yingyong).click()
            self.dy_cq_yunzhijia_yingyong = 1
            print("应用按钮点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cq_yunzhijia_yingyong = 2
            print("应用按钮点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\cq_yunzhijia_yingyong.png")

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

    #采购入库（通过ID进行定位）
    cq_yunzhijia_caigouruku = (by.XPATH, "//*[@class='android.view.View'][@content-desc='采购入库单']")

    # 封装操作（点击操作）
    def click_cq_yunzhijia_caigouruku  (self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cq_yunzhijia_caigouruku).click()
            self.dy_cq_yunzhijia_caigouruku = 1
            print("采购入库点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cq_yunzhijia_caigouruku = 2
            print("采购入库点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\cq_yunzhijia_caigouruku.png")




    # ------------------------搜狗浏览器，进入库存查询页------------------------
    # 搜狗浏览器的地址栏（通过ID进行定位）
    sougou_shouye_wangzhi = (by.ID,"sogou.mobile.explorer:id/as_")

    # 封装操作（点击操作）
    def click_sougou_shouye_wangzhi(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.sougou_shouye_wangzhi).click()
            self.dy_sougou_shouye_wangzhi = 1
            print("搜狗地址栏点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_sougou_shouye_wangzhi = 2
            print("搜狗地址栏点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_sougou_shouye_wangzhi.png")

    # 输入网址（通过ID进行定位）
    sougou_dizhi_shuru = (by.ID,"sogou.mobile.explorer:id/ru")

    # 封装操作（点击操作）
    def click_sougou_dizhi_shuru(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.sougou_dizhi_shuru).click()
            self.dy_sougou_dizhi_shuru = 1
            print("网址栏点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_sougou_dizhi_shuru = 2
            print("网址栏点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_sougou_dizhi_shuru_image.png")

    # 封装操作（输入操作）
    def send_sougou_dizhi_shuru(self,fangan="https://feature.kingdee.com:2024/baseline_a/mobile.html?accountId=666522411780278272#/form/mobim_homepage?accountId=666522411780278272"):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.send_keys(fangan, *self.sougou_dizhi_shuru)
            self.dy_send_sougou_dizhi_shuru = 1
            print("地址输入成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_send_sougou_dizhi_shuru = 2
            print("地址输入失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\send_sougou_dizhi_shuru.png")


    # 前往网址（通过xpath进行定位）
    sougou_dizhi_qianwang = (by.ID,"sogou.mobile.explorer:id/apk")

    # 封装操作（点击操作）
    def click_sougou_dizhi_qianwang(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.sougou_dizhi_qianwang).click()
            self.dy_sougou_dizhi_qianwang = 1
            print("前往网址点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_sougou_dizhi_qianwang = 2
            print("前往网址点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_sougou_dizhi_qianwang_image.png")




    # ------------------------登录页------------------------
    #用户名（通过xpath进行定位）
    cq_denglu_yonghuming = (by.XPATH, "//*[@class='android.widget.EditText'][@text='请输入用户名/手机号/邮箱']")

    # 封装操作（点击操作）
    def click_cq_denglu_yonghuming(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cq_denglu_yonghuming).click()
            self.dy_cq_denglu_yonghuming = 1
            print("用户名点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cq_denglu_yonghuming = 2

    # 封装操作（输入操作）
    def send_cq_denglu_yonghuming(self,yonghuming="17299999999"):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.send_keys(yonghuming, *self.cq_denglu_yonghuming)
            self.dy_send_cq_denglu_yonghuming = 1
            print("用户名输入成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_send_cq_denglu_yonghuming = 2

    #密码（通过xpath进行定位）
    cq_denglu_mima = (by.XPATH, "//*[@class='android.widget.EditText'][@index='5']")

    # 封装操作（点击操作）
    def click_cq_denglu_mima(self):
        # 判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.cq_denglu_mima).click ()
            self.dy_cq_denglu_mima = 1
            print("密码点击成功")
        # 如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cq_denglu_mima = 2

    # 封装操作（输入操作）
    def send_cq_denglu_mima(self,mima="1234567"):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.send_keys(mima, *self.cq_denglu_mima)
            self.dy_send_cq_denglu_mima = 1
            print("密码输入成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_send_cq_denglu_mima = 2

    #登陆（通过xpath进行定位）
    cq_denglu_denglu = (by.XPATH, "//*[@class='android.view.View'][@content-desc='登录']")

    # 封装操作（点击操作）
    def click_cq_denglu_denglu(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cq_denglu_denglu).click()
            self.dy_cq_denglu_denglu= 1
            print("登陆点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cq_denglu_denglu = 2



    # ------------------------采购入库页面------------------------
    # 采购入库图标（通过xpath进行定位）
    cgrk_yingyong_tubiao = (by.XPATH, "//*[@class='android.view.View'][@content-desc='采购入库单']")

    # 封装操作（点击操作）
    def click_cgrk_yingyong_tubiao(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_yingyong_tubiao).click()
            self.dy_cgrk_yingyong_tubiao = 1
            print("采购入库图标点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_yingyong_tubiao = 2
            print("采购入库点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_sougou_dizhi_qianwang_image.png")

    # 暂存下拉菜单（通过xpath进行定位）
    cgrk_shouye_zancun= (by.XPATH, "//*[@class='android.view.View'][@index='3'][@content-desc='暂存']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_zancun(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_zancun).click()
            self.dy_cgrk_shouye_zancun = 1
            print("暂存下拉菜单点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_zancun = 2
            print("暂存下拉菜单点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_sougou_dizhi_qianwang_image.png")

    # 不限下拉菜单（通过xpath进行定位）
    cgrk_shouye_buxian= (by.XPATH, "//*[@class='android.view.View'][@index='3'][@content-desc='不限']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_buxian(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_buxian).click()
            self.dy_cgrk_shouye_buxian = 1
            print("不限下拉菜单点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_buxian = 2
            print("不限下拉菜单点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_buxian.png")


    # 下拉菜单的已审核（通过xpath进行定位）
    cgrk_shouye_xiala_yishenhe= (by.XPATH, "//*[@class='android.view.View'][@content-desc='已审核']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_xiala_yishenhe(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_xiala_yishenhe).click()
            self.dy_cgrk_shouye_xiala_yishenhe = 1
            print("下拉菜单已审核点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_xiala_yishenhe = 2
            print("下拉菜单已审核点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_xiala_yishenhepng")

    # 确定按钮（通过xpath进行定位）
    cgrk_shouye_queding= (by.XPATH, "//*[@class='android.view.View'][@index='11'][@content-desc='确定']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_queding(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_queding).click()
            self.dy_cgrk_shouye_queding= 1
            print("确定按钮点击成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_queding = 2
            print("确定按钮点击失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_queding.png")

    #判断是不是已经进入了首页
    # 确定按钮（通过xpath进行定位）
    cgrk_yingyong_zancuntubiao = (by.XPATH, "//*[@class='android.view.View'][@resource-id='labelapsave'][@content-desc='暂存']")

    # 封装操作（不操作，只是进行定位）
    def noclick_cgrk_yingyong_zancuntubiao(self):
        #判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element (*self.cgrk_yingyong_zancuntubiao)
            self.dy_no_cgrk_yingyong_zancuntubiao = 1
            print("test_case,执行成功")
        #如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_no_cgrk_yingyong_zancuntubiao  = 2
            print("test_case,执行失败")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\noclick_cgrk_yingyong_zancuntubiao.png")