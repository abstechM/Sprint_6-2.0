from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_LIT = [By.CLASS_NAME, 'Button_Button__ra12g']
    ORDER_BUTTON_BIG = [By.CSS_SELECTOR, "[class*='Button_Middle']"]
    QUESTION_LOCATORS = [By.XPATH, "//*[@id = 'accordion__heading-{}']"]
    QUESTION_LOCATORS_FIND = [By.XPATH, "//*[@id = 'accordion__heading-7']"]
    ANSWER_LOCATORS = [By.XPATH, "//div[@id = 'accordion__panel-{}']/p"]
    LOGO_SAMOKAT = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    LOGO_YANDEX = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
