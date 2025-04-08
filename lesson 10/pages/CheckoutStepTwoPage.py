from selenium.webdriver.common.by import By

class CheckoutStepTwoPage:

    def __init__(self, driver):
        self._driver = driver

    def read_cost(self) -> str:
        """Чтение итоговой стоимости"""
        cost = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        return cost
    
    def close_browser(self):
        """Закрытие браузера"""
        self._driver.quit()