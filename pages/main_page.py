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




