def test_mobile(android_app):
    android_app.search_model("6775447")

    android_app.selectFirstModel()

    android_app.checkIsVtoDisplayed()
