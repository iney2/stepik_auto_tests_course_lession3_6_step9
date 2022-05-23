from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_cart_button(browser):
    browser.implicitly_wait(3)
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Add to Cart button is not found"
