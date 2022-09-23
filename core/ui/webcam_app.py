import allure
from selene import browser

from core.tools import file_tool
from .pages import main_page
from .pages import camera_page
from pathlib import Path
import os

main_page = main_page

URL = 'https://webcammictest.com/'


@allure.step("Open URL" + URL)
def open_app():
    browser.open_url(URL)
    main_page.loaded()


@allure.step("Press 'Test webcam'")
def test_camera():
    main_page.open_webcam()


def check_video():
    camera_page.loaded()

@allure.step("Capturing the screenshot")
def capture_screenshot(prefix):
    file_tool.capture_screenshot(prefix)

@allure.step("Get actual camera name")
def get_camera_name():
    name = camera_page.get_camera_name()
    print("Camera name = " + name)
    return name


def get_tests_dir_pat():
    root_path = str(
        Path(os.getcwd())) + "/tests"  # depends on the runner. if run from IDE - use Path(os.getcwd()).parent
    print("--> tests root_path =" + root_path)
    return root_path
