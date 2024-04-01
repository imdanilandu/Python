from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/login')

username = driver.find_element(By.CSS_SELECTOR, '#username')

password = driver.find_element(By.CSS_SELECTOR, '#password')

button = driver.find_element(By.CSS_SELECTOR, 'button')

username.send_keys('tomsmith')

password.send_keys('SuperSecretPassword!')

button.click()