from selenium.webdriver.common.by import By

class CheckoutStepOnePage:

    def __init__(self, driver):
        self._driver = driver

    def complete_form(self):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Данил')
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Стафейчук')
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('660074')
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()