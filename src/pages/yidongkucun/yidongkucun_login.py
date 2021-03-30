'''
页面;登录页面
'''

from src.common import Base_page
from appium.webdriver.common import mobileby
import time

class Login_page (Base_page.Base_page):
    by = mobileby.MobileBy ()

    #-------------搜狗首页到库存首页的页面元素组件-----------
    # 搜狗首页的网址按钮定位（通过ID定位）
    sougou_website_button = (by.XPATH, "//*[@resource-id='sogou.mobile.explorer:id/aff']")
    # 搜狗网址页，网址栏定位
    sougou_website_column = (by.XPATH, "//*[@resource-id='sogou.mobile.explorer:id/yv']")
    #前往按钮
    sougou_website_qianwang = (by.XPATH, "//*[@resource-id='sogou.mobile.explorer:id/aj4']")
    #输入用户名
    land_username = (by.XPATH, "//*[@class='android.widget.EditText'][@index='2']")
    #输入密码
    land_password = (by.XPATH, "//*[@class='android.widget.EditText'][@index='5']")
    #登录页-登陆按钮
    land_denglu = (by.XPATH, "//*[@class='android.view.View'][@index='8']")

    # 点击搜狗首页-网址栏
    def click_sougou_website_button(self):
        self.find_element(*self.sougou_website_button).click()
    #点击网址栏
    def click_sougou_website_column(self):
        self.find_element(*self.sougou_website_column).click()
    #输入网址
    def send_sougou_website_column(self, pwd="https://feature.kingdee.com:2024/baseline_a/mobile.html#/form/im_mobinvquery"):
        self.send_keys (pwd, *self.sougou_website_column)
    #点击前往
    def click_sougou_website_qianwang(self):
        self.find_element(*self.sougou_website_qianwang).click()
    #点击用户名
    def click_land_username(self):
        self.find_element(*self.land_username).click()
    #输入用户名
    def send_land_username(self, username="17299999999"):
        self.send_keys (username, *self.land_username)
    # 点击密码
    def click_land_password(self):
        self.find_element(*self.land_password).click ()
    # 输入密码
    def send_land_password(self,password="1234567"):
        self.send_keys(password, *self.land_password)

    def click_land_denglu(self):
        self.find_element(*self.land_denglu).click ()

    def test_land_denglu(self):
        self.driver.press_keycode(3)
        time.sleep(10)

