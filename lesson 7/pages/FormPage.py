from selenium.webdriver.common.by import By

class FormPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    def complete_form(self):
        self._driver.find_element(By.CSS_SELECTOR, '[name=first-name]').send_keys('Иван')
        self._driver.find_element(By.CSS_SELECTOR, '[name=last-name]').send_keys('Петров')
        self._driver.find_element(By.CSS_SELECTOR, '[name=address]').send_keys('Ленина, 55-3')
        self._driver.find_element(By.CSS_SELECTOR, '[name=e-mail]').send_keys('test@skypro.com')
        self._driver.find_element(By.CSS_SELECTOR, '[name=phone]').send_keys('+7985899998787')
        self._driver.find_element(By.CSS_SELECTOR, '[name=city]').send_keys('Москва')
        self._driver.find_element(By.CSS_SELECTOR, '[name=country]').send_keys('Россия')
        self._driver.find_element(By.CSS_SELECTOR, '[name=job-position]').send_keys('QA')
        self._driver.find_element(By.CSS_SELECTOR, '[name=company]').send_keys('SkyPro')
    
    def click_button(self):
        self._driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()

    def define_first_name_color(self):
        first_name = self._driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
        return first_name

    def define_last_name_color(self):
        last_name = self._driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
        return last_name
    
    def define_address_color(self):
        address = self._driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
        return address    

    def define_e_mail_color(self):
        e_mail = self._driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
        return e_mail

    def define_phone_color(self):
        phone = self._driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
        return phone

    def define_zip_code_color(self):
        zip_code = self._driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
        return zip_code

    def define_city_color(self):
        city = self._driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
        return city

    def define_country_color(self):
        country = self._driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
        return country

    def define_job_position_color(self):
        job_position = self._driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
        return job_position

    def define_company_color(self):
        company = self._driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')
        return company