import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Нажать на вопрос и получить ответ")
    def click_to_question_and_get_answer_text(self, num):
        format_q = self.format_locator(MainPageLocators.QUESTION_LOCATORS, num)
        format_a = self.format_locator(MainPageLocators.ANSWER_LOCATORS, num)
        self.click_on_element(format_q)
        return self.get_text_from_element(format_a)

    @allure.step("Проверка результата")
    def check_result(self, result, expected_result):
        return result == expected_result

    @allure.step("Переход на новое окно")
    def click_switch_window(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])


    @allure.step("Нажатие на Самокат")
    def click_logo_samokat(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_LIT)
        self.click_on_element(MainPageLocators.LOGO_SAMOKAT)











