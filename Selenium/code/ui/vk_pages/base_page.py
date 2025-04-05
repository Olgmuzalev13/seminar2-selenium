import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import vk_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedException(Exception):
    pass


class BasePage(object):

    login_locators = vk_locators.LoginPageLocators()
    main_locators = vk_locators.MainPageLocators()
    url = 'https://education.vk.company/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Search')
    def search(self, query):
        elem = self.find(self.login_locators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(self.login_locators.GO_BUTTON_LOCATOR)
        go_button.click()
        self.my_assert()

    @allure.step('Enter login data')
    def login(self, login, password):
        confirm_button = self.find(self.login_locators.ENTER_LOCATOR)
        confirm_button.click()
        confirm_button = self.find(self.login_locators.EMAIL_PASS_CONTINUE_LOCATOR)
        confirm_button.click()
        login_input = self.find(self.login_locators.EMAIL)
        login_input.send_keys(login)
        password_input = self.find(self.login_locators.PASS)
        password_input.send_keys(password)
        confirm_button = self.find(self.login_locators.CONFIRM_ENTER)
        confirm_button.click()
        close_button = self.find(self.login_locators.CLOSE_NEW_VERSION)
        close_button.click()

    @allure.step('search')
    def search(self, name):
        search_input = self.find(self.main_locators.SEARCH)
        search_input.send_keys(name)

    @allure.step("Step 1")
    def my_assert(self):
        assert 1 == 1


    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
