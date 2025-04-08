import allure
from selenium import webdriver
from pages.FormPage import FormPage

@allure.title("Заполнение формы")
@allure.description("")
@allure.feature("CREATE")
@allure.severity("CRITICAL")
def test_color():
    with allure.step("Открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html"):
        browser = webdriver.Chrome()
        form_page = FormPage(browser)
    with allure.step("Заполнить форму значениями, кроме поля Zip code"):
        form_page.complete_form('Иван', 'Петров', 'Ленина, 55-3', 'test@skypro.com', '+7985899998787', 'Москва', 'Россия', 'QA', 'SkyPro')
    with allure.step("Нажать кнопку Submit"):
        form_page.click_button()
    with allure.step("Проверить, что поле Zip code подсвечено красным"):
        assert form_page.define_zip_code_color() == 'rgba(248, 215, 218, 1)'
    with allure.step("Проверить, что остальные поля подсвечены зеленым"):
        assert form_page.define_first_name_color() == form_page.define_last_name_color() == form_page.define_address_color() == form_page.define_e_mail_color() == form_page.define_phone_color() == form_page.define_city_color() == form_page.define_country_color() == form_page.define_job_position_color() == form_page.define_company_color() == 'rgba(209, 231, 221, 1)'
    