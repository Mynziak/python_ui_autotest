from selenium.webdriver.common.by import By

from ..ui_elem import UiElem

test_button = By.XPATH, "(//button)[2]"


def loaded():
    test_cam_btn = UiElem(test_button)
    test_cam_btn.locator_presence()


def open_webcam():
    test_cam_btn = UiElem(test_button)
    test_cam_btn.click()
