from selenium import webdriver
from pages.FormPage import FormPage

def test_color():
    browser = webdriver.Chrome()
    form_page = FormPage(browser)
    form_page.complete_form()
    form_page.click_button()
    assert form_page.define_first_name_color() == form_page.define_last_name_color() == form_page.define_address_color() == form_page.define_e_mail_color() == form_page.define_phone_color() == form_page.define_city_color() == form_page.define_country_color() == form_page.define_job_position_color() == form_page.define_company_color() == 'rgba(209, 231, 221, 1)'
    assert form_page.define_zip_code_color() == 'rgba(248, 215, 218, 1)'