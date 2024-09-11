from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.page_order import MakeOrderOne

class TestLogoSamokat:

    def test_logo_samokat(self, driver):
        logo = MakeOrderOne(driver)
        logo.get_url("https://qa-scooter.praktikum-services.ru/")
        logo.click_on_element(MainPageLocators.ORDER_BUTTON_LIT)
        logo.click_on_element(MainPageLocators.LOGO_SAMOKAT)
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
