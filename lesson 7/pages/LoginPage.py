from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    def log_in(self):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()