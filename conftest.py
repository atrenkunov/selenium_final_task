import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Select browser language to open')
    parser.addoption('--browser_name', action='store', default='Chrome', help='Select browser to run')


@pytest.fixture
def browser(request):
    language = request.config.getoption('--language')
    browser_name = request.config.getoption('--browser_name')

    if language is False:
        raise pytest.UsageError("You didn't select language for test!")

    if 'Chrome' == browser_name:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif 'Firefox' == browser_name:
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("Unknown browser. Chrome and Firefox only supported!")

    yield browser
    # after test
    browser.quit()
