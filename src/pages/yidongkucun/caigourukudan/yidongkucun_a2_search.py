'''
页面;登录页面
'''

from src.common import Base_page
from appium.webdriver.common import mobileby
import random


class search_page(Base_page.Base_page):
    by = mobileby.MobileBy ()

    #-------------采购入库-搜索框-----------
    # 搜索框（通过xpath进行定位）
    cgrk_shouye_sousuo = (by.XPATH, "//*[@class='android.widget.EditText'][@text='请搜索供应商名称/库管员/单据编号']")

    # 封装操作（点击操作）
    def click_cgrk_shouye_sousuo(self):
        # 判断能否进行点击操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.find_element(*self.cgrk_shouye_sousuo).click ()
            self.dy_cgrk_shouye_sousuo = 1
            print ("搜索框点击成功")
        # 如果不能进行点击操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_cgrk_shouye_sousuo = 2
            print ("搜索框点击失败，输出当前截图")
            self.driver.get_screenshot_as_file (
                "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\click_cgrk_shouye_sousuo.png")

    def send_cgrk_shouye_sousuo(self,sousuo="1"):
        #判断能否进行输入操作，如果能够点击操作，赋值1，同时输出点击成功的提示
        try:
            self.send_keys(sousuo, *self.cgrk_shouye_sousuo)
            self.dy_send_cgrk_shouye_sousuo= 1
            print("搜索内容输入成功")
        #如果不能进行输入操作，赋值2，同时输出点击不成功的提示，并且输出当前页的截图
        except:
            self.dy_send_cgrk_shouye_sousuo = 2
            print("搜索内容输入失败，输出当前截图")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\cgrk_shouye_sousuo.png")





