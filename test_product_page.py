import time

import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_basket_button()
    product_page.should_be_item_cost()
    product_page.should_be_item_name()

    expected_item_name = product_page.get_item_name()
    expected_item_cost = product_page.get_item_cost()

    product_page.push_item_into_basket()

    product_page.solve_quiz_and_get_code()

    confirm_page = BasketPage(browser, browser.current_url)

    confirm_page.is_confirmation_name_label_equals_to(expected_item_name)
    confirm_page.is_confirmation_cost_label_equals_to(expected_item_cost)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.push_item_into_basket()
    product_page.solve_quiz_and_get_code()

    product_page.should_item_name_is_not_present()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.push_item_into_basket()
    product_page.solve_quiz_and_get_code()

    confirm_page = BasketPage(browser, browser.current_url)
    confirm_page.should_item_name_is_not_present()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    confirm_page = BasketPage(browser, browser.current_url)
    confirm_page.should_item_name_is_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.push_item_into_basket()
    product_page.solve_quiz_and_get_code()

    confirm_page = BasketPage(browser, browser.current_url)
    confirm_page.should_item_name_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)

    login_page.should_be_login_link()
    login_page.should_be_register_form()
    login_page.should_be_login_form()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.go_to_basket()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()

    basket_page.should_be_empty_label()
    basket_page.should_be_empty_basket()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()

        password = str(time.time()) + '123456789';
        LoginPage(browser, browser.current_url).register_new_user(str(time.time()) + '@fakemail.org', password)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.should_be_authorized_user()

        confirm_page = BasketPage(browser, browser.current_url)
        confirm_page.should_item_name_is_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.should_be_authorized_user()

        product_page.should_be_basket_button()
        product_page.should_be_item_cost()
        product_page.should_be_item_name()

        expected_item_name = product_page.get_item_name()
        expected_item_cost = product_page.get_item_cost()

        product_page.push_item_into_basket()

        product_page.solve_quiz_and_get_code()

        confirm_page = BasketPage(browser, browser.current_url)

        confirm_page.is_confirmation_name_label_equals_to(expected_item_name)
        confirm_page.is_confirmation_cost_label_equals_to(expected_item_cost)
