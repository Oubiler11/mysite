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

    # -------------库存首页-方案的页面元素和操作-----------
    #右上角的方案图标
    kucun_fangan_button = (by.XPATH, "//*[@class='android.view.View'][@index='3']")
    #右下角的新增按钮
    fangan_xinzeng_button = (by.XPATH, "//*[@class='android.view.View'][@bounds='[655,1144][694,1183]']")
    #输入方案按钮
    fangan_mingcheng_button = (by.XPATH, "//*[@class='android.widget.EditText'][@bounds='[159,135][702,163]']")
    #方案框按钮
    fangan_kuang_button = (by.XPATH, "//*[@class='android.view.View'][@bounds='[655,1144][694,1183]']")
    #保存按钮
    fangan_baocun_button = (by.XPATH, "//*[@class='android.view.View'][@content-desc='保存']")






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

    #方案具体操作进行封装
    def click_kucun_fangan_button(self):
        self.find_element(*self.kucun_fangan_button).click()

    def click_fangan_xinzeng_button(self):
        self.find_element(*self.fangan_xinzeng_button).click()

    i = random.randint (1, 10000000000)
    def click_fangan_mingcheng_button(self):
        self.find_element(*self.fangan_mingcheng_button).click()

    def send_fangan_mingcheng_button(self,fangan = random.randint (1, 10000000000)):
        self.send_keys(fangan, *self.fangan_mingcheng_button)

    def click_fangan_baocun_button(self):
        self.find_element(*self.fangan_baocun_button).click()
