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

    @allure.step('Login')
    def login(self, login, password):
        confirm_button = self.find(self.login_locators.ENTER_LOCATOR)
        confirm_button.click()
        assert 'Для продолжения выбери удобный способ входа.' in self.driver.page_source
        confirm_button = self.find(self.login_locators.EMAIL_PASS_CONTINUE_LOCATOR)
        confirm_button.click()
        assert 'Нет аккаунта?' in self.driver.page_source
        login_input = self.find(self.login_locators.EMAIL)
        login_input.send_keys(login)
        password_input = self.find(self.login_locators.PASS)
        password_input.send_keys(password)
        confirm_button = self.find(self.login_locators.CONFIRM_ENTER)
        confirm_button.click()
        close_button = self.find(self.login_locators.CLOSE_NEW_VERSION)
        print(close_button.get_attribute('xmlns'))
        assert "http://www.w3.org/2000/svg" in self.driver.page_source
        close_button.click()
        assert 'вход / регистрация' not in self.driver.page_source

    @allure.step('Search')
    def search(self, name):
        search_input = self.find(self.main_locators.SEARCH)
        assert search_input.get_attribute('placeholder') == "Поиск..."
        search_input.send_keys(name)

    @allure.step('Get topic page by id')
    def get_topic_page_by_id(self, id):
        self.click(vk_locators.MainPageLocators.EDUCATION_BUTTON, timeout=10)
        assert '#904: Программа по веб-разработке ' in self.driver.page_source
        self.click(vk_locators.MainPageLocators.DISCIPLINE_LOCATOR(id=id), timeout=10)

    @allure.step('Get student by address')
    def get_student_by_address(self, address):
        self.click(vk_locators.MainPageLocators.STUDENT(address), timeout=10)
    
    @allure.step('Get lesson by id')
    def get_lesson_by_id(self, id):
        self.click(vk_locators.MainPageLocators.LESSON(id), timeout=10)

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

class LoginPage(BasePage):
    def login(self):
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'