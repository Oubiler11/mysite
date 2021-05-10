from src.pages.yidongkucun.caigoushouhuodan import yidongkucun_cgshd_a1_login,yidongkucun_cgshd_a2_zancun_guolv,yidongkucun_cgshd_a4_yishenhe_guolv,\
    yidongkucun_cgshd_a10_shenhe_xiatui
from src.common import driver_config
# noinspection PyUnresolvedReferences
from appium.webdriver.common.touch_action import TouchAction
# noinspection PyUnresolvedReferences
import time
import unittest#引用自动化测试框架
# noinspection PyUnresolvedReferences
from appium.webdriver.webdriver import WebDriver


class TestLong4(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()



    def test_case_4(self):
        #引入页面元素
        self.login = yidongkucun_cgshd_a1_login.Login_page(self.driver)
        self.yishenhe = yidongkucun_cgshd_a4_yishenhe_guolv.yishenhe(self.driver)

        #点击采购收货，如果不是应用首页，说明环境有问题
        try:
            # 点击应用图标
            self.login.click_cq_yunzhijia_yidongkucun ()
            self.assertEqual (self.login.dy_cq_yunzhijia_yidongkucun, 1, '断言失败，进入移动库存失败')


        except:
            print("请确认环境正确或账号登陆成功")

        #进入采购收单页面
        self.login.click_cgshd_yingyong_tubiao()
        self.assertEqual(self.login.dy_cgshd_yingyong_tubiao, 1, '断言失败，采购收货单点击失败')

        # 引入a2的页面元素
        self.guolv = yidongkucun_cgshd_a2_zancun_guolv.guolv(self.driver)

        #点击下拉菜单表的已提交
        self.guolv.click_cgshd_yitijiao_guolv()
        self.assertEqual(self.guolv.dy_cgshd_yitijiao_guolv, 1, '断言失败，下拉菜单-已提交，点击失败')

        #点击下拉列表的已审核
        self.yishenhe.click_cgshd_yishenhe_guolv()
        self.assertEqual(self.yishenhe.dy_cgshd_yishenhe_guolv, 1, '断言失败，下拉菜单-已审核，点击失败')

        #点击下拉列表的已提交
        self.guolv.click_cgshd_yitijiao_xialaliebiao()
        self.assertEqual(self.guolv.dy_cgshd_yitijiao_xialaliebiao, 1, '断言失败，下拉列表-已提交，点击失败')

        #点击确认按钮进行过滤
        self.guolv.click_cgshd_queding_xialaliebiao()
        self.assertEqual(self.guolv.dy_cgshd_queding_xialaliebiao, 1, '断言失败，下拉列表-确定，点击失败')

        #点击下拉菜单的本周，按时间进行过滤
        self.guolv.click_cgshd_benzhou_xialacaidan()
        self.assertEqual(self.guolv.dy_cgshd_benzhou_xialacaidan, 1, '断言失败，下拉菜单-本周，点击失败')

        #点击下拉列表的不限，按时间进行过滤
        self.guolv.click_cgshd_buxian_xialaliebiao_sj()
        self.assertEqual(self.guolv.dy_cgshd_buxian_xialaliebiao_sj, 1, '断言失败，下拉列表-不限，点击失败')

        # 引入a10的页面元素
        self.xiatui = yidongkucun_cgshd_a10_shenhe_xiatui.xiatui(self.driver)

        #点击下推订单
        self.xiatui.click_cgshd_shenhe_dingdan_liebiao_sj()
        self.assertEqual(self.xiatui.dy_cgshd_shenhe_dingdan_liebiao_sj, 1, '断言失败，下拉列表-不限，点击失败')

        #点击下推，下推订单
        self.xiatui.click_cgshd_shenhe_dingdan_xiatui()
        self.assertEqual(self.xiatui.dy_cgshd_shenhe_dingdan_xiatui, 1, '断言失败，下拉列表-不限，点击失败')

        for i in range(2):
            self.driver.keyevent(4)
            print(f"循环{i}次")




    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()