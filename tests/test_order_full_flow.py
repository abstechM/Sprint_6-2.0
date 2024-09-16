import allure
import pytest
from conftest import driver
from constants import Constants
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.page_order import MakeOrderOne

class TestMakeOrdersOne:
    @allure.title("Весь флоу через: {method}")
    @pytest.mark.parametrize("method", [MainPageLocators.ORDER_BUTTON_BIG, MainPageLocators.ORDER_BUTTON_LIT])
    def test_make_oder_one_page(self, method, driver):
        main = MainPage(driver)
        main.get_url(Constants.URL)
        main.accept_cookie()
        order = MakeOrderOne(driver)
        order.click_on_element(method)
        order.order_one_part("Александр", "Дмитриев", "Санкт-Петербург", "89260235883")
        order.order_two_part("Быстрее")
        order.check_end_order()





