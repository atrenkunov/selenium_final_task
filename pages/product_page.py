from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Current page doesn't contain add to basket button"

    def push_item_into_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "Current page doesn't contain item name"

    def should_be_item_cost(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_COST), "Current page doesn't contain item cost"

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_item_cost(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_COST).text
