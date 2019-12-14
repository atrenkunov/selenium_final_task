from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM_INPUT = (By.ID, "id_registration-password2")

    BUTTON_REGISTER = (By.CSS_SELECTOR, "button.btn[name='registration_submit']")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    ITEM_COST = (By.CSS_SELECTOR, "div.product_main p.price_color")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    CONFIRMATION_NAME_LABEL = (By.CSS_SELECTOR, "div.alert.alert-success div.alertinner strong")
    CONFIRMATION_COST_LABEL = (By.CSS_SELECTOR, "div.alert.alert-info div.alertinner p strong")
