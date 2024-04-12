from selenium.webdriver.common.by import By

class CheckoutStepTwoPage:

    def __init__(self, driver):
        self._driver = driver

    def read_cost(self):
        total = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        return total
    
    def close_browser(self):
        self._driver.quit()