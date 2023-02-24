import pytest
from selene import have
from selene.support.shared import browser


@pytest.fixture()
def open_desktop_browser():
    browser.config.window_width = 1600
    browser.config.window_height = 1000
    browser.open('https://github.com')


@pytest.fixture()
def open_mobile_browser():
    browser.config.window_width = 800
    browser.config.window_height = 800
    browser.open('https://github.com')


def test_github_desktop(open_desktop_browser):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(open_mobile_browser):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
