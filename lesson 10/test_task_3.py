import allure
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ShopPage import ShopPage
from pages.CartPage import CartPage
from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage

@allure.title("Интернет-магазин")
@allure.description("")
@allure.feature("CREATE")
@allure.severity("CRITICAL")
def test_cost():
    with allure.step("Открыть сайт магазина: https://www.saucedemo.com/"):
        browser = webdriver.Chrome()
        login_page = LoginPage(browser)
    with allure.step("Авторизоваться"):
        login_page.log_in('standard_user', 'secret_sauce')
    shop_page = ShopPage(browser)
    with allure.step("Добавить в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie"):
        shop_page.add_products()
    with allure.step("Перейти в корзину"):
        shop_page.go_to_cart()
    cart_page = CartPage(browser)
    with allure.step("Нажать Checkout"):
        cart_page.click_checkout()
    checkout_step_one_page = CheckoutStepOnePage(browser)
    with allure.step("Заполнить форму своими данными"):
        checkout_step_one_page.complete_form('Данил', 'Стафейчук', '660074')
    checkout_step_two_page = CheckoutStepTwoPage(browser)
    with allure.step("Прочитать со страницы итоговую стоимость"):
        total = checkout_step_two_page.read_cost()
    with allure.step("Закрыть браузер"):
        checkout_step_two_page.close_browser()
    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total == 'Total: $58.29'