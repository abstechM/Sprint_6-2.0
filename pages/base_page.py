import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Старт Драйвер")
    def get_url(self, URL):
        self.driver.get(URL)

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Нажать на элемент")
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step("Получить текст с элемента")
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step("Установить текст")
    def set_text_to_elemet(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step("Преобразовать локатор")
    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)


