from selenium.webdriver.common.by import By
class OrderOneLocators:
    NAME_FILED = [By.XPATH, "//input[@placeholder ='* Имя']"]
    SECNAME_FIELD = [By.XPATH, "//input[@placeholder ='* Фамилия']"]
    ADDRES_FIELD = [By.XPATH, "//input[@placeholder ='* Адрес: куда привезти заказ']"]
    METRO_FIELD = [By.CLASS_NAME, "select-search__input"]
    NUMBER_FIELD = [By.XPATH, "//input[@placeholder ='* Телефон: на него позвонит курьер']"]
    CONT_BUTTON = [By.CSS_SELECTOR, 'button[class*=Button_Middle]']
    METRO = [By.XPATH, '//div//li/button[@value = "1"]']
