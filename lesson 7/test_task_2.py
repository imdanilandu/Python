from selenium import webdriver
from pages.CalculatorPage import CalculatorPage

def test_result():
    browser = webdriver.Chrome()
    calculator_page = CalculatorPage(browser)
    calculator_page.enter_value('45')
    calculator_page.click_buttons()
    calculator_page.wait()
    assert calculator_page.result() == '15'