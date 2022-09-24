# UI tests automation for Web and mobile (Android, iOS) apps with a Python

Repository contains the project with automation of UI Tests by Python, Pytest, Appium and Selenium WebDriver.
 - Implemented sample test for [web cam web app](https://webcammictest.com/): mockup the web camera, capture screenshot and compare the camera name

 - Implemented sample tests for *private Android app* - **restricted**

**Inspired by** https://github.com/ibalagurov/heisenbug_piter_2018_example

  # Prerequisites:
**OS:** Mac OS

**Setup on your running machine:**
* Appium GUI server
* Android SDK

**Install:**
* pytest: `pipenv install pytest --dev`
* selene: `pip install selene`
* appium client for python: `pip install Appium-Python-Client`
* Allure test report:  `pip install allure-pytest`

   # Configure environment:
1. Specify  platform in [configure](config/test_run.py) : `PLATFORM='WEB'` or `IOS` or `ANDROID`
2. Specify devices, collecting browser logs and etc 
(through ANDROID_VERSION, ANDROID_DEVICE_NAME, ANDROID_DEVICE_UDID, ANDROID_APP_ACTIVITY, IOS_VERSION, IOS_DEVICE_NAME variables)
3.  Run Appium GUI server for iOS or Android platform

   # Run tests:
1. - Web: `python3 -m pytest --alluredir=allure-report/ tests/ui/web`
   - Android: `python3 -m pytest --alluredir=allure-report/ tests/ui/android`

2. Generate test-report: `allure serve allure-report/`

   # Useful links:
- [Appium-python documentation](https://github.com/appium/python-client)
- [Selene](https://github.com/yashaka/selene)
- [Pytest](https://docs.pytest.org/en/latest/)
