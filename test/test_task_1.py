from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
driver.find_element(By.CSS_SELECTOR, '[name=first-name]').send_keys('Иван')
driver.find_element(By.CSS_SELECTOR, '[name=last-name]').send_keys('Петров')
driver.find_element(By.CSS_SELECTOR, '[name=address]').send_keys('Ленина, 55-3')
driver.find_element(By.CSS_SELECTOR, '[name=e-mail]').send_keys('test@skypro.com')
driver.find_element(By.CSS_SELECTOR, '[name=phone]').send_keys('+7985899998787')
driver.find_element(By.CSS_SELECTOR, '[name=city]').send_keys('Москва')
driver.find_element(By.CSS_SELECTOR, '[name=country]').send_keys('Россия')
driver.find_element(By.CSS_SELECTOR, '[name=job-position]').send_keys('QA')
driver.find_element(By.CSS_SELECTOR, '[name=company]').send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
    
first_name = driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
last_name = driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
address = driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
e_mail = driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
phone = driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
city = driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
country = driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
job_position = driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
company = driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')

def test_zip_code():
    assert zip_code == 'rgba(248, 215, 218, 1)'

def test_other_fields():
    assert first_name == last_name == address == e_mail == phone == city == country == job_position == company == 'rgba(209, 231, 221, 1)'