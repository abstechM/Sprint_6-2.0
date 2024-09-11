from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.page_order import MakeOrderOne


class TestLogoYandex:

    def test_logo_yandex(self, driver):
        yandex = MakeOrderOne(driver)
        yandex.get_url("https://qa-scooter.praktikum-services.ru/")
        yandex.click_on_element(MainPageLocators.LOGO_YANDEX)
        assert not (driver.current_url == 'https://dzen.ru/?yredirect=true')
