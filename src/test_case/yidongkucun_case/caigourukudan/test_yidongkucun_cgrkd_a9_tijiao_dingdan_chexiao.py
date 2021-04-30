from src.pages.yidongkucun.caigourukudan import yidongkucun_a3_sousuo_yishenhe, yidongkucun_a2_search, \
    yidongkucun_a1_login,yidongkucun_cgrkd_a4_shouye_neirong,yidongkucun_cgrkd_a5_zancun_tijiao,\
    yidongkucun_cgrkd_a6_zancun_dingdan_tijiao,yidongkucun_cgrkd_a7_zancun_dingdan_shanchu,yidongkucun_cgrkd_a8_tijiao_dingdan_guolv,\
    yidongkucun_cgrkd_a9_tijiao_dingdan_chexiao

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
        self.login = yidongkucun_a1_login.Login_page(self.driver)

        #------------------------搜狗浏览器，进入库存查询页-------------------------
        #点击移动库存，如果不是应用首页，说明环境有问题

        # 再次点击搜狗浏览器的二次栏
        self.login.click_cq_yunzhijia_yidongkucun ()
        self.assertEqual (self.login.dy_cq_yunzhijia_yidongkucun, 1, '断言失败，进入移动库存失败')


        try:
            #输入采购入库单页面
            self.login.click_cq_yunzhijia_caigouruku()
            self.assertEqual(self.login.dy_cq_yunzhijia_caigouruku, 1, '断言失败，采购入库点击失败')
        except:
            print("请确认环境正确或账号登陆成功")

        #点击暂存下拉菜单
        self.login.click_cgrk_shouye_zancun()
        self.assertEqual(self.login.dy_cgrk_shouye_zancun, 1, '断言失败，暂存下拉菜单点击失败')

        # 引入chexiao页面元素
        self.xiao = yidongkucun_cgrkd_a8_tijiao_dingdan_guolv.guolv_page(self.driver)

        #下拉菜单中的暂存选项
        self.xiao.click_cgrk_shouye_tijiao_zancun()
        self.assertEqual(self.xiao.dy_cgrk_shouye_tijiao_zancun, 1, '断言失败，暂存选项点击失败')

        #下拉菜单中的提交选项
        self.xiao.click_cgrk_shouye_tijiao_tijiao()
        self.assertEqual(self.xiao.dy_cgrk_shouye_tijiao_tijiao, 1, '断言失败，提交选项点击失败')

        # 下拉菜单中的确定选项
        self.xiao.click_cgrk_shouye_tijiao_queding()
        self.assertEqual (self.xiao.dy_cgrk_shouye_tijiao_queding, 1, '断言失败，提交选项点击失败')

        #引入buxian的页面元素
        self.buxian = yidongkucun_a3_sousuo_yishenhe.buxian_page(self.driver)
        #点击业务日期
        self.buxian.click_cgrk_shouye_yewuriqi()
        self.assertEqual (self.buxian.dy_cgrk_shouye_yewuriqi, 1, '断言失败，不限下拉菜单点击失败')

        #点击业务日期下拉菜单的不限
        self.buxian.click_cgrk_shouye_yewuriqi_buxian()
        self.assertEqual (self.buxian.dy_cgrk_shouye_yewuriqi_buxian, 1, '断言失败，不限下拉菜单点击失败')

        #引入chexiao的页面元素
        self.chexiao = yidongkucun_cgrkd_a9_tijiao_dingdan_chexiao.chexiao_page(self.driver)

        #筛选后的订单，进入订单详情页
        self.chexiao.click_cgrk_shouye_tijiao_chexiao_dingdan()
        self.assertEqual(self.chexiao.dy_cgrk_shouye_tijiao_chexiao_dingdan, 1, '断言失败，订单详情进入失败')

        #筛选后的订单，进入订单详情页，点击撤销
        self.chexiao.click_cgrk_shouye_tijiao_chexiao_chehui()
        self.assertEqual(self.chexiao.dy_cgrk_shouye_tijiao_chexiao_chehui, 1, '断言失败，撤销点击失败')
        
        #---------判断用例是否成功---------#
        #查找暂存按钮
        self.login.noclick_cgrk_yingyong_zancuntubiao()
        #如果查找成功，判断为成功
        if self.login.dy_no_cgrk_yingyong_zancuntubiao == 1:
            print("test_case9:pass")
        #如果查询不成功，判断为失败
        else:
            self.assertEqual(self.login.dy_no_cgrk_yingyong_zancuntubiao, 1, '断言失败，test_case_9执行失败！')




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()