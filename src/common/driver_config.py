#封装appium的driver
from appium import webdriver

class Driver_Config():
    def get_driver(self):
        try:
            # 定义一个desired_caps字典来保存启动APP所需的那5个参数
            # 如何通过adb获取appActivity（adb shell dumpsys window w|findstr \/|findstr name=）
            self.desired_caps = {
                # 手机参数
                'platformName': 'Android',  # 平台名称
                'platformVersion': '6',  # 平台版本
                'deviceName': '127.0.0.1:7555',  # （模拟器设备名称，通过adb来链接模拟器，adb connect 127.0.0.1:7555）
                # 应用参数
                'appPackage': 'com.kdweibo.client',  # 包名（用的是云之家）
                'appActivity': 'com.kdweibo.android.ui.fragment.HomeMainFragmentActivity',  # APP打开的界面
                'noReset': True,  # 是否重置
                'newCommandTimeout': 6000,
                'unicodeKeyboard': True,  # 解决输入中文问题
                'resetKeyboard': True  # 解决输入中文问题
            }
            # 通过appium的webdriver包下面的Remote方法打开App
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

            return self.driver
        except Exception as e:
            raise e
