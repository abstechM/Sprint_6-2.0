from selenium.webdriver.common.by import By

class OrderTwoLocators:
    RENTAL_TIME = [By.CSS_SELECTOR, "[class*='Dropdown-menu']>:nth-child(1)"]
    COLOR_BLACK = [By.ID, 'black']
    COLOR_GREY = [By.ID, 'grey']
    WHEN_DELIVERY_FIELD = [By.CSS_SELECTOR, "input[placeholder*='Когда привезти самокат']"]
    RENTAL_PERIOD_FIELD = [By.CSS_SELECTOR, "[class*='Dropdown-root']"]
    COMMENT_FILED = [By.CSS_SELECTOR, "input[placeholder*='Комментарий для курьера']"]
    ORDER_BUTTON = [By.CSS_SELECTOR, "[class*='Order_Buttons__1xGrp']>:nth-child(2)"]
    HEADER_PAGE_TWO = [By.CLASS_NAME, "Order_Header__BZXOb"]
    HEADER_OF_ORDER = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]

