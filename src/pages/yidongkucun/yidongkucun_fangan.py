'''
页面;登录页面
'''

from src.common import Base_page
from appium.webdriver.common import mobileby
import random


class search_page(Base_page.Base_page):
    by = mobileby.MobileBy ()

    # -------------方案切换页的页面元素和操作-----------
    #右上角的新增按钮(通过ID进行定位)
    fangan_kccx_xinzengan=(by.ID, "com.kdweibo.client:id/btn_popup")

    def click_fangan_kccx_xinzengan(self):
        self.find_element(*self.fangan_kccx_xinzengan).click()

    def noclick_fangan_kccx_xinzengan(self):
        self.find_element(*self.fangan_kccx_xinzengan).click()

    #右下角的新增图标（通过xpath进行定位，不建议使用这个）
    fangan_kccx_xinzengtb = (by.XPATH, "//*[@class='android.view.View'][@bounds='[655,1144][694,1183]']")

    def click_fangan_kccx_xinzengtb(self):
        self.find_element(*self.fangan_kccx_xinzengtb).click()

    # -------------新增方案页的页面元素和操作-----------
    #方案名称
    fangan_kccx_fanganminceng = (by.XPATH, "//*[@class='android.widget.EditText'][@text='请输入方案名称']")

    def click_fangan_kccx_fanganminceng(self):
        self.find_element(*self.fangan_kccx_fanganminceng).click()

    def send_fangan_kccx_fanganminceng(self,fangan=random.randint(1, 10000000000)):
        self.send_keys(fangan, *self.fangan_kccx_fanganminceng)

    def send_fangan_kccx_fanganmincenggd(self,fangan="test01"):
        self.send_keys(fangan, *self.fangan_kccx_fanganminceng)



    #进入仓库
    fangan_kccx_jinrucangku = (by.XPATH, "//*[@class='android.view.View'][@index='9']")

    def click_fangan_kccx_jinrucangku(self):
        self.find_element(*self.fangan_kccx_jinrucangku).click()


    #选择仓位
    fangan_kccx_xuanzecangku = (by.XPATH, "//*[@class='android.view.View'][@content-desc='cdy广东仓']")

    def click_fangan_kccx_xuanzecangku(self):
        self.find_element(*self.fangan_kccx_xuanzecangku).click()


    #保存仓库
    fangan_kccx_baocuncangku = (by.XPATH, "//*[@class='android.view.View'][@content-desc='确定']")

    def click_fangan_kccx_baocuncangku(self):
        self.find_element (*self.fangan_kccx_baocuncangku).click ()


    #保存按钮(通过ID进行定位)
    fangan_kccx_baocunan = (by.XPATH, "//*[@class='android.view.View'][@index='42']")

    def click_fangan_kccx_baocunan(self):
        self.find_element(*self.fangan_kccx_baocunan).click()


    #切换方案
    #随意切换
    fangan_kccx_qiehuanfangansj = (by.XPATH, "//*[@class='android.view.View'][@index='3']")

    def click_fangan_kccx_qiehuanfangansj(self):
        self.find_element(*self.fangan_kccx_qiehuanfangansj).click()

    #固定切换
    fangan_kccx_qiehuanfangangd = (by.XPATH, "//*[@class='android.view.View'][@content-desc='test01']")

    def click_fangan_kccx_qiehuanfangangd(self):
        self.find_element(*self.fangan_kccx_qiehuanfangangd).click()

    #没有库存
    fangan_kccx_meiyoukucun = (by.XPATH, "//*[@class='android.widget.EditText'][@text='共0条数据']")

    def noclick_fangan_kccx_meiyoukucun(self):
        self.find_element (*self.fangan_kccx_meiyoukucun)


    #固定切换
    fangan_kccx_shanchufangan = (by.XPATH, "//*[@class='android.view.View'][@content-desc='test003']")

    def click_fangan_kccx_shanchufangan(self):
        self.find_element(*self.fangan_kccx_shanchufangan).click()











