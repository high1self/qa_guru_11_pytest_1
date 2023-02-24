import pytest
from selene import have
from selene.support.shared import browser


@pytest.fixture(params=['Desktop', 'Mobile'], scope='function')
def open_browser(request):
    if request.param == 'Desktop':
        browser.config.window_width = 1600
        browser.config.window_height = 1000
        browser.open('https://github.com')
    elif request.param == 'Mobile':
        browser.config.window_width = 800
        browser.config.window_height = 800
        browser.open('https://github.com')


desktop = pytest.mark.parametrize('open_browser', ['Desktop'], indirect=True)
mobile = pytest.mark.parametrize('open_browser', ['Mobile'], indirect=True)


@desktop
def test_github_desktop(open_browser):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@mobile
def test_github_mobile(open_browser):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
