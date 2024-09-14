import allure
from selenium.webdriver import Keys

from locators.main_page_locators import MainPageLocators
from locators.make_order_page_one_locators import OrderOneLocators
from locators.make_order_page_two_locators import OrderTwoLocators
from pages.base_page import BasePage


# Класс 1-ой страницы заказа
class MakeOrderOne(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.click_logo_samokat = None

    @allure.step("Заполнение Имя")
    def set_name(self, name):
        self.set_text_to_elemet(OrderOneLocators.NAME_FILED, name)

    @allure.step("Заполнение Фамилия")
    def set_secname(self, secname):
        self.set_text_to_elemet(OrderOneLocators.SECNAME_FIELD, secname)

    @allure.step("Установка адреса")
    def set_addres(self, addres):
        self.set_text_to_elemet(OrderOneLocators.ADDRES_FIELD, addres)

    @allure.step("Усатновка метро")
    def set_metro(self):
        self.click_on_element(OrderOneLocators.METRO_FIELD)
        self.click_on_element(OrderOneLocators.METRO)

    @allure.step("Заполнение номера")
    def set_number(self, number):
        self.set_text_to_elemet(OrderOneLocators.NUMBER_FIELD, number)

    @allure.step("Нажать далее")
    def click_continiue(self):
        self.click_on_element(OrderOneLocators.CONT_BUTTON)


    @allure.step("Принять cookie")
    def accept_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)


    @allure.step("Заполнение перовй страницы заказа")
    def order_one_part(self, name, secname, addres, number):
        self.set_metro()
        self.set_name(name)
        self.set_secname(secname)
        self.set_addres(addres)
        self.set_number(number)
        self.click_continiue()

    @allure.step("Установка даты заказа")
    def set_when_delivery(self):
        self.set_text_to_elemet(OrderTwoLocators.WHEN_DELIVERY_FIELD, "09.09.2024" + Keys.ENTER)

    @allure.step("Установа периода аренды")
    def set_rent_period(self):
        self.click_on_element(OrderTwoLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderTwoLocators.RENTAL_TIME)

    @allure.step("Усатновка цвета")
    def set_color(self):
        self.click_on_element(OrderTwoLocators.COLOR_GREY)

    @allure.step("Заполнение комментарий")
    def set_comment(self, comment):
        self.set_text_to_elemet(OrderTwoLocators.COMMENT_FILED, comment)

    @allure.step("Нажать закзазать")
    def click_order_button(self):
        self.click_on_element(OrderTwoLocators.ORDER_BUTTON)

    @allure.step("Заполнение второй страницы зазказа")
    def order_two_part(self, comment):
        self.set_when_delivery()
        self.set_rent_period()
        self.set_color()
        self.set_comment(comment)
        self.click_order_button()