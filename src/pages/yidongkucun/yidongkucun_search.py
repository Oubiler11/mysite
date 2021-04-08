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
    kucun_shouye_search = (by.XPATH, "//*[@class='android.widget.EditText'][@index='0']")
    #确认搜索按钮
    kucun_shouye_truesearch = (by.XPATH, "//*[@resource-id='earchbuttonap'][@index='3']")
    #断言是否搜索成功
    kucun_shouye_duanyan_search = (by.XPATH, "//*[@class='android.widget.EditText'][@index='4']")



    #点击库存首页的搜索按钮
    def click_kucun_shouye_search(self):
        self.find_element(*self.kucun_shouye_search).click()
    #输入搜索内容
    def send_kucun_shouye_search(self,search="item"):
        self.send_keys(search, *self.kucun_shouye_search)
    #点击确认搜索按钮
    def click_kucun_shouye_truesearch(self):
        self.find_element(*self.kucun_shouye_truesearch).click()
    #断言是否搜索成功
    def click_kucun_shouye_duanyan_search(self):
        self.find_element(*self.kucun_shouye_duanyan_search).click()

