import allure
from conftest import driver
from constants import Constants
from pages.main_page import MainPage

class TestLogoSamokat:
    @allure.title("Тестирование логотипа самокат")
    def test_logo_samokat(self, driver):
        logo = MainPage(driver)
        logo.get_url(Constants.URL)
        logo.click_logo_samokat()
        assert logo.check_url(Constants.URL)

