import allure
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage

@allure.title("Калькулятор")
@allure.description("")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_result():
    with allure.step("Открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"):
        browser = webdriver.Chrome()
        calculator_page = CalculatorPage(browser)
    with allure.step("В поле ввода ввести значение"):
        calculator_page.enter_value('45')
    with allure.step("Нажать на кнопки: 7, +, 8, ="):
        calculator_page.click_buttons()
    with allure.step("Подождать введенное значение секунд"):
        calculator_page.wait()
    with allure.step("Проверить, что в окне отобразится результат 15 через введенное значение секунд"):
        assert calculator_page.result() == '15'