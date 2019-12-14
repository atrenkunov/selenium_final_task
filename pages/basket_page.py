from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Current url doesn't contain substring basket"

    def should_be_confirmation_name_label(self):
        assert self.is_element_present(
            *BasketPageLocators.CONFIRMATION_NAME_LABEL), "Current page doesn't contain name label"

    def should_be_confirmation_cost_label(self):
        assert self.is_element_present(
            *BasketPageLocators.CONFIRMATION_COST_LABEL), "Current page doesn't contain cost label"

    def is_confirmation_name_label_equals_to(self, text):
        actual_item_name = self.browser.find_element(*BasketPageLocators.CONFIRMATION_NAME_LABEL).text
        assert text == actual_item_name, f"Item name {actual_item_name} didn't equals with origin name {text}"

    def is_confirmation_cost_label_equals_to(self, text):
        actual_item_cost = self.browser.find_element(*BasketPageLocators.CONFIRMATION_COST_LABEL).text
        assert text == actual_item_cost, f"Item cost {actual_item_cost} didn't equals with origin cost {text}"

    def should_item_name_is_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.CONFIRMATION_NAME_LABEL), 'Element is visible'

    def should_item_name_is_disappeared(self):
        assert self.is_disappeared(*BasketPageLocators.CONFIRMATION_NAME_LABEL), "Element didn't disappear"

    def should_be_empty_label(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text with empty basket didn't appear"

    def should_be_empty_basket(self):
        empty_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert empty_text, "Basket is not empty"
