'''
页面;登录页面
'''

from src.common import Base_page
from appium.webdriver.common import mobileby
import random


class search_page(Base_page.Base_page):
    by = mobileby.MobileBy ()

    #-------------库存首页-搜索页面元素和操作-----------
    #库存首页的搜索按钮
    fangan_qiehuan_button = (by.XPATH, "//*[@class='android.view.View'][@index='3']")
    #确认搜索按钮
    fangan_qiehuan_land = (by.XPATH, "//*[@class='android.view.View'][@bounds='[60,120][622,162]']")

    #点击右上角的方案按钮
    def click_fangan_qiehuan_button(self):
        self.find_element(*self.fangan_qiehuan_button).click()

    #点击第一个方案进行切换
    def click_fangan_qiehuan_land(self):
        self.find_element(*self.fangan_qiehuan_land).click()









