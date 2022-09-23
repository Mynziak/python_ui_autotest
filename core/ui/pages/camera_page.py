import selenium.webdriver.support.ui as UI
from selenium.webdriver.common.by import By

from ..ui_elem import UiElem


def loaded():
    video_area = UiElem((By.CSS_SELECTOR, ".CamTestVideoContainer"))
    video_area.locator_presence(60)


def get_camera_name():
    camera_dropdown = UiElem((By.ID, "CamTestSettingsDevicesSelect-videoinput"))
    camera_dropdown.locator_presence()

    drop_down_elem= camera_dropdown.find_elem()
    select = UI.Select(drop_down_elem)
    for option in select.options:
        print("RESULT : " + option.text)

    return select.options[0].text
