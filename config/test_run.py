import os

from . import env

PLATFORM = env.get('PLATFORM', 'WEB') #!!! set the platform before run tests

ONE_SESSION = env.get_bool('ONE_SESSION', 'False')
BROWSER_LOGS = env.get_bool('BROWSER_LOGS', 'False')

# shortcuts
IS_WEB = PLATFORM == 'WEB'
IS_MOBILE = PLATFORM in ('IOS', 'ANDROID')
IS_ANDROID = PLATFORM == 'ANDROID'
IS_IOS = PLATFORM == 'IOS'

APPIUM_SERVER = env.get('APPIUM_SERVER',
                        'http://0.0.0.0:4723/wd/hub')  # - Appium GUI server must be run! otherwise run from terminal and use 'http://localhost:4723/wd/hub'

APP_NAME = {
    'ANDROID': env.get('ANDROID_APP_NAME', 'XXX.apk'),
    'IOS': env.get('IOS_APP_NAME', 'XXX.app')
}.get(PLATFORM)

_DEFAULT_APP_PATH = str(os.path.join(os.getcwd(), fr"mobile_app/{APP_NAME}"))
MOBILE_APP = env.get('MOBILE_APP', _DEFAULT_APP_PATH) if IS_MOBILE else None

ANDROID_VERSION = env.get('ANDROID_VERSION', '11')
ANDROID_DEVICE_NAME = env.get('ANDROID_DEVICE_NAME', 'Samsung Galaxy S10')
ANDROID_DEVICE_UDID = env.get('ANDROID_DEVICE_UDID', 'XXXXX')
ANDROID_APP_ACTIVITY =env.get('ANDROID_APP_ACTIVITY', 'XXX')
ANDROID_APP_PACKAGE =env.get('ANDROID_APP_PACKAGE', 'XXX')

IOS_VERSION = env.get('IOS_VERSION', '11.4')
IOS_DEVICE_NAME = env.get('IOS_DEVICE_NAME', 'iPhone X')


ANDROID_APP_ACTIVITY = {
    'ANDROID_APP_ACTIVITY': env.get('ANDROID_APP_NAME', 'XXX.apk'),
    'ANDROID_APP_ACTIVITY': env.get('IOS_APP_NAME', 'XXX.app')
}.get(PLATFORM)