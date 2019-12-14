import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Select browser language to open')


@pytest.fixture
def browser(request):
    language = request.config.getoption('--language')

    if language is False:
        raise pytest.UsageError("You didn't select language for test!")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    # after test
    browser.quit()
