from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

button = driver.find_element(By.CSS_SELECTOR, 'button')

button.click()
button.click()
button.click()
button.click()
button.click()

elements = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')

print(len(elements))