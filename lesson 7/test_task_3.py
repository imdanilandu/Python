from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ShopPage import ShopPage
from pages.CartPage import CartPage
from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage

def test_cost():
    browser = webdriver.Chrome()
    login_page = LoginPage(browser)
    login_page.log_in()
    shop_page = ShopPage(browser)
    shop_page.add_products()
    shop_page.go_to_cart()
    cart_page = CartPage(browser)
    cart_page.click_checkout()
    checkout_step_one_page = CheckoutStepOnePage(browser)
    checkout_step_one_page.complete_form()
    checkout_step_two_page = CheckoutStepTwoPage(browser)
    total = checkout_step_two_page.read_cost()
    checkout_step_two_page.close_browser()
    assert total == 'Total: $58.29'