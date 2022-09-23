import config
import pytest

from selene import factory
from core.ui import driver, webcam_app, android_vto_app


@pytest.fixture(scope='session' if config.test_run.ONE_SESSION else 'function')
def app():
    ui_driver = driver.get()
    factory.set_shared_driver(ui_driver)

    yield webcam_app

    driver.close(ui_driver)  # quit browser

@pytest.fixture(scope='session' if config.test_run.ONE_SESSION else 'function')
def android_app():
    ui_driver = driver.get()
    factory.set_shared_driver(ui_driver)

    yield android_vto_app

    driver.close(ui_driver)  # quit browser