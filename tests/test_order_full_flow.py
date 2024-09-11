import pytest
from conftest import driver
from locators.main_page_locators import MainPageLocators
from locators.make_order_page_two_locators import OrderTwoLocators
from pages.page_order import MakeOrderOne

class TestMakeOrdersOne:

    @pytest.mark.parametrize("method", [MainPageLocators.ORDER_BUTTON_BIG, MainPageLocators.ORDER_BUTTON_LIT])
    def test_make_oder_one_page(self, method, driver):
        order = MakeOrderOne(driver)
        order.get_url("https://qa-scooter.praktikum-services.ru/")
        order.click_on_element(MainPageLocators.COOKIE_BUTTON)
        order.click_on_element(method)
        order.order_one_part("Александр", "Дмитриев", "Санкт-Петербург", "89260235883")
        order.order_two_part("Быстрее")
        assert order.find_element_with_wait(OrderTwoLocators.HEADER_OF_ORDER)





