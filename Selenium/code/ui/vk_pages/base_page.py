import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import vk_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

    @allure.step('Login')
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
        assert 'вход / регистрация' not in self.driver.page_source
        # enter_login_button = self.find(self.login_locators.ENTER_LOCATOR)
        # enter_login_button.click()
        # choose_way_to_enter_button = self.find(self.login_locators.EMAIL_PASS_CONTINUE_LOCATOR)
        # choose_way_to_enter_button.click()
        # login_input = self.find(self.login_locators.EMAIL)
        # login_input.send_keys(login)
        # password_input = self.find(self.login_locators.PASS)
        # password_input.send_keys(password)
        # confirm_button = self.find(self.login_locators.CONFIRM_ENTER)
        # confirm_button.click()
        # close_button = self.find(self.login_locators.CLOSE_NEW_VERSION)
        # close_button.click()
        # assert 'вход / регистрация' not in self.driver.page_source

    @allure.step('Search')
    def search(self, name):
        search_input = self.find(self.main_locators.SEARCH)
        assert search_input.get_attribute('placeholder') == "Поиск..."
        search_input.send_keys(name)

    @allure.step('Get topic page by id')
    def get_topic_page_by_id(self, id):
        self.click(vk_locators.MainPageLocators.EDUCATION_BUTTON, timeout=10)
        assert '#904: Программа по веб-разработке ' in self.driver.page_source
        self.click(self.DISCIPLINE_LOCATOR(id=id), timeout=10)

    @allure.step('Get student by address')
    def get_student_by_address(self, address):
        self.click(self.STUDENT(address), timeout=10)
    
    @allure.step('Get lesson by id')
    def get_lesson_by_id(self, id):
        self.click(self.LESSON(id), timeout=10)

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @staticmethod
    def STUDENT(address):
        return By.XPATH, f'//a[contains(@href, "https://education.vk.company/profile/{address}/")]'

    @staticmethod
    def DISCIPLINE_LOCATOR(id):
        return By.XPATH, f"//a[contains(@href, '/curriculum/program/discipline/{id}/')]"

    @staticmethod
    def LESSON(id):
        return By.XPATH, f'//a[contains(@href, "/curriculum/program/lesson/{id}/")]'

class LoginPage(BasePage):
    def login(self):
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'