import pytest
from selene import have
from selene.support.shared import browser


@pytest.fixture()
def open_browser(request):
    if request.param == 'Desktop':
        browser.config.window_width = 1600
        browser.config.window_height = 1000
        browser.open('https://github.com')
    elif request.param == 'Mobile':
        browser.config.window_width = 800
        browser.config.window_height = 800
        browser.open('https://github.com')


browser_param = pytest.mark.parametrize('open_browser', ['Desktop', 'Mobile'], indirect=True)


@browser_param
def test_github_desktop(open_browser):
    if browser.config.window_width == 800 and browser.config.window_height == 800:
        pytest.skip('Этот тест для декстоп браузера')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@browser_param
def test_github_mobile(open_browser):
    if browser.config.window_width == 1600 and browser.config.window_height == 1000:
        pytest.skip('Этот тест для мобильного браузера')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
