from selenium.webdriver.common.by import By

class ShopPage:

    def __init__(self, driver):
        self._driver = driver  
    
    def add_products(self):
        """Добавление товаров в корзину"""
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        
    def go_to_cart(self):
        """Переход в корзину"""
        self._driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()