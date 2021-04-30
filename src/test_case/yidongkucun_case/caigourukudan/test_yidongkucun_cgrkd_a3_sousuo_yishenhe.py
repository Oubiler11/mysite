from src.pages.yidongkucun.caigourukudan import yidongkucun_a3_sousuo_yishenhe, yidongkucun_a2_search, \
    yidongkucun_a1_login
from src.common import driver_config
# noinspection PyUnresolvedReferences
from appium.webdriver.common.touch_action import TouchAction
# noinspection PyUnresolvedReferences
import time
import unittest#引用自动化测试框架
# noinspection PyUnresolvedReferences
from appium.webdriver.webdriver import WebDriver


class TestLong3(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()


    def test_case_3(self):
        #引入页面元素
        self.login = yidongkucun_a1_login.Login_page(self.driver)

        #------------------------搜狗浏览器，进入库存查询页-------------------------
        #点击移动库存，如果不是应用首页，说明环境有问题
        try:
            # 再次点击搜狗浏览器的二次栏
            self.login.click_cq_yunzhijia_yidongkucun ()
            self.assertEqual (self.login.dy_cq_yunzhijia_yidongkucun, 1, '断言失败，进入移动库存失败')


        except:
            print("请确认环境正确或账号登陆成功")

        #输入采购入库单页面
        self.login.click_cq_yunzhijia_caigouruku()
        self.assertEqual(self.login.dy_cq_yunzhijia_caigouruku, 1, '断言失败，采购入库点击失败')



        #引入search的页面元素
        self.search = yidongkucun_a2_search.search_page(self.driver)
        self.buxian = yidongkucun_a3_sousuo_yishenhe.buxian_page(self.driver)
        # 点击暂存下拉菜单，进入采购库存页面
        self.login.click_cgrk_shouye_zancun()
        self.assertEqual (self.login.dy_cgrk_shouye_zancun, 1, '断言失败，暂存下拉菜单点击失败')

        # 选择下拉菜单中的“已审核”
        self.login.click_cgrk_shouye_xiala_yishenhe()
        self.assertEqual (self.login.dy_cgrk_shouye_xiala_yishenhe, 1, '断言失败，不限下拉菜单点击失败')

        # 选择下拉菜单中的“暂存”
        self.buxian.click_cgrk_shouye_zancun()
        self.assertEqual (self.buxian.dy_cgrk_shouye_zancun, 1, '断言失败，不限下拉菜单点击失败')

        # 点击下拉菜单中的“确定”完成过滤
        self.login.click_cgrk_shouye_queding()
        self.assertEqual (self.login.dy_cgrk_shouye_queding, 1, '断言失败，确定按钮点击失败')

        #点击业务日期
        self.buxian.click_cgrk_shouye_yewuriqi()
        self.assertEqual (self.buxian.dy_cgrk_shouye_yewuriqi, 1, '断言失败，不限下拉菜单点击失败')

        #点击业务日期下拉菜单的不限
        self.buxian.click_cgrk_shouye_yewuriqi_buxian()
        self.assertEqual (self.buxian.dy_cgrk_shouye_yewuriqi_buxian, 1, '断言失败，不限下拉菜单点击失败')

        #判断是否存在已审核
        #---------判断是否登陆成功
        #查找右上角的方案按钮
        self.buxian.noclick_cgrk_yingyong_yishenhe()
        #如果查找成功，判断为成功
        if self.buxian.dy_no_cgrk_yingyong_yishenhe == 1:
            print("test_case3:pass")
        #如果查询不成功，判断为失败
        else:
            self.assertEqual(self.buxian.dy_no_cgrk_yingyong_zancuntubiao, 1, '断言失败，test_case_3执行失败！')




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()