from .screens import android_catalog

main_page = android_catalog


def search_model(sku_number):
    main_page.search(sku_number)


def selectFirstModel():
    main_page.selectFirstModel()


def checkIsVtoDisplayed():
    main_page.vto_presence()
