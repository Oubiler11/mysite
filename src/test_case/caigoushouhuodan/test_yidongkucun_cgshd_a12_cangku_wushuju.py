from src.pages.yidongkucun.caigoushouhuodan import yidongkucun_cgshd_a1_login,yidongkucun_cgshd_a2_zancun_guolv
from src.common import driver_config
from src.pages.yidongkucun.caigourukudan import yidongkucun_a3_sousuo_yishenhe, yidongkucun_a2_search, \
    yidongkucun_a1_login,yidongkucun_cgrkd_a4_shouye_neirong,yidongkucun_cgrkd_a5_zancun_tijiao,\
    yidongkucun_cgrkd_a6_zancun_dingdan_tijiao,yidongkucun_cgrkd_a7_zancun_dingdan_shanchu,yidongkucun_cgrkd_a8_tijiao_dingdan_guolv,\
    yidongkucun_cgrkd_a9_tijiao_dingdan_chexiao,yidongkucun_cgrkd_a10_tijiao_chexiao_shanchu,yidongkucun_cgrkd_a11_cangku_guolv_youshuju
# noinspection PyUnresolvedReferences
from appium.webdriver.common.touch_action import TouchAction
# noinspection PyUnresolvedReferences
import time
import unittest#引用自动化测试框架
# noinspection PyUnresolvedReferences
from appium.webdriver.webdriver import WebDriver


class TestLong12(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()



    def test_case_12(self):
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

        # 引入a2的页面元素
        self.guolv = yidongkucun_cgshd_a2_zancun_guolv.guolv(self.driver)

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

        #引入a11，cangku的页面元素
        self.cangku = yidongkucun_cgrkd_a11_cangku_guolv_youshuju.cangku_page(self.driver)

        #点击下拉菜单的仓库
        self.cangku.click_cgrk_cangku_guolv_youshuju()
        self.assertEqual(self.cangku.dy_cgrk_cangku_guolv_youshuju, 1, '断言失败，仓库下拉选项点击失败')

        #点击搜索栏
        self.cangku.click_cgrk_cangku_guolv_sousuo()
        self.assertEqual(self.cangku.dy_cgrk_cangku_guolv_sousuo, 1, '断言失败，搜索栏点击失败')

        #输入cdy
        self.cangku.send_cgrk_cangku_guolv_dianjisousuo()
        self.assertEqual(self.cangku.dy_send_cgrk_cangku_guolv_dianjisousuo, 1, '断言失败，cdy输入失败')

        #点击cdy广东
        self.cangku.click_cgrk_cangku_guolv_cdyshenzhen()
        self.assertEqual(self.cangku.dy_cgrk_cangku_guolv_cdyshenzhen, 1, '断言失败，cdy深圳点击失败')

        #点击确定
        self.cangku.click_cgrk_cangku_guolv_queding()
        self.assertEqual(self.cangku.dy_cgrk_cangku_guolv_queding, 1, '断言失败，确定按钮点击失败')






    def tearDown(self):
        self.driver.quit()










if __name__ == '__main__':
    unittest.main()