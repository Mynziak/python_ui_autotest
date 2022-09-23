from appium import webdriver as appium_driver
from selenium import webdriver as selenium_driver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import config

_capabilities = {
    'IOS': {
        'version': '1.8.0',
        'platformName': 'iOS',
        'platformVersion': config.test_run.IOS_VERSION,
        'deviceName': config.test_run.IOS_DEVICE_NAME,
        'app': config.test_run.MOBILE_APP,
        'noReset': False,
        'fullReset': False
    },
    'ANDROID': {
        "platformName": 'Android',
        "deviceName": config.test_run.ANDROID_DEVICE_NAME,
        'udid':  config.test_run.ANDROID_DEVICE_UDID,
        'platformVersion': config.test_run.ANDROID_VERSION,
        # "version": config_device.platform_version,
        'appPackage': config.test_run.ANDROID_APP_PACKAGE,
        'appActivity': config.test_run.ANDROID_APP_ACTIVITY,
        'automationName': 'UiAutomator2',
        'browserName': '',
        'clearDeviceLogsOnStart': 'true',
        'appWaitActivity': '*',
        'autoGrantPermissions': 'true',
        'adbExecTimeout': 50000,
        'uiautomator2ServerLaunchTimeout': 50000
    },

    'WEB': {
        **DesiredCapabilities.CHROME,
        'loggingPrefs': {'browser': 'ALL'}
    }
}


def get():
    caps = _capabilities[config.test_run.PLATFORM]
    if config.test_run.IS_MOBILE:
        return appium_driver.Remote(
            command_executor=config.test_run.APPIUM_SERVER,
            desired_capabilities=caps
        )

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--test-type")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-plugins")

    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")

    options.add_argument(
        "--use-file-for-fake-video-capture=/Users/mynziak/Documents/python_prjs/python_ui_autotests/tests/resources/"
        "dmytro_69_video.Y4M")
    return selenium_driver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def close(driver):
    driver.close_app() if config.test_run.IS_MOBILE else driver.quit()
