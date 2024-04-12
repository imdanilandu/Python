from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def enter_value(self):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(45)

    def click_buttons(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
    
    def wait(self):
        waiter = WebDriverWait(self._driver, 50, 0.1)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15')
            )
    
    def result(self):
        screen = self._driver.find_element(By.CSS_SELECTOR, '.screen').text
        return screen