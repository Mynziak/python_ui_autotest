import allure
from selenium.webdriver.common.by import By

from core.ui.ui_elem import UiElem

@allure.step("Search model by SKU")
def search(sku):
    search_button = UiElem((By.ID, "com.misterspex.app:id/search_button"))
    search_input = UiElem((By.ID, "com.misterspex.app:id/search_src_text"))

    search_button.locator_presence(60)

    search_button.click()

    search_input.type(sku)

@allure.step("Select first model of glasses")
def selectFirstModel():
    first_model = UiElem((By.ID, "com.misterspex.app:id/view"))
    first_model.locator_presence()
    first_model.click()


def vto_presence():
    vto = UiElem((By.XPATH, "//android.widget.Button[contains(@text,'VISIBLE')]"))
    vto.locator_presence(15)
