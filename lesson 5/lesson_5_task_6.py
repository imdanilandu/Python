from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/entry_ad')

button_restart = driver.find_element(By.CSS_SELECTOR, '#restart-ad')

button_restart.click()

button_close = driver.find_element(By.XPATH, '//p[text()="Close"]')

button_close.click()