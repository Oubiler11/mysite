from src.pages.yidongkucun.caigoushouhuodan import yidongkucun_cgshd_a1_login,yidongkucun_cgshd_a2_zancun_guolv,yidongkucun_cgshd_a5_zancun_shanchu,\
    yidongkucun_cgshd_a6_zancun_baocun,yidongkucun_cgshd_a7_zancun_tijiao,yidongkucun_cgshd_a9_tijiao_shenhe
from src.common import driver_config
# noinspection PyUnresolvedReferences
from appium.webdriver.common.touch_action import TouchAction
# noinspection PyUnresolvedReferences
import time
import unittest#引用自动化测试框架
# noinspection PyUnresolvedReferences
from appium.webdriver.webdriver import WebDriver


class TestLong9(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()



    def test_case_9(self):
        #引入页面元素
        self.login = yidongkucun_cgshd_a1_login.Login_page(self.driver)

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

        # 引入a2和a7的页面元素
        self.guolv = yidongkucun_cgshd_a2_zancun_guolv.guolv(self.driver)
        self.tijiao = yidongkucun_cgshd_a7_zancun_tijiao.tijiao(self.driver)

        #点击下拉菜单表的已提交
        self.guolv.click_cgshd_yitijiao_guolv()
        self.assertEqual(self.guolv.dy_cgshd_yitijiao_guolv, 1, '断言失败，下拉菜单-已提交，点击失败')


        #点击确认按钮进行过滤
        self.guolv.click_cgshd_queding_xialaliebiao()
        self.assertEqual(self.guolv.dy_cgshd_queding_xialaliebiao, 1, '断言失败，下拉列表-确定，点击失败')

        #点击下拉菜单的本周，按时间进行过滤
        self.guolv.click_cgshd_benzhou_xialacaidan()
        self.assertEqual(self.guolv.dy_cgshd_benzhou_xialacaidan, 1, '断言失败，下拉菜单-本周，点击失败')

        #点击下拉列表的不限，按时间进行过滤
        self.guolv.click_cgshd_buxian_xialaliebiao_sj()
        self.assertEqual(self.guolv.dy_cgshd_buxian_xialaliebiao_sj, 1, '断言失败，下拉列表-不限，点击失败')

        #点击已提交订单
        self.tijiao.click_cgshd_tijiao_dingdan_liebiao_sj()
        self.assertEqual(self.tijiao.dy_cgshd_tijiao_dingdan_liebiao_sj, 1, '断言失败，提交订单列表，点击失败')

        #引入a9页面的数据
        self.shenhe = yidongkucun_cgshd_a9_tijiao_shenhe.shenhe (self.driver)
        #点击已提交订单
        self.shenhe.click_cgshd_zancun_dingdan_shenhe()
        self.assertEqual(self.shenhe.dy_cgshd_zancun_dingdan_shenhe, 1, '断言失败，审核按钮，点击失败')




        for i in range(2):
            self.driver.keyevent(4)
            print(f"循环{i}次")





    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()