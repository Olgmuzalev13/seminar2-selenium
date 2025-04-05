import pytest
from ui.locators import vk_locators
from _pytest.fixtures import FixtureRequest
import time
from ui.vk_pages.base_page import BasePage


class BaseCase:
    authorize = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = (request.getfixturevalue('vk_base_page'))
        if self.authorize:
            login, password = request.getfixturevalue("credentials")
            self.base_page.login(login, password)


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self):
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = False
    def test_login(self):
        assert 'Настоящие знания' in self.driver.page_source
        assert 'education' in self.driver.page_source


class TestLK(BaseCase):
    authorize = True

    def test_get_seminar_info(self):
        assert 'Прямой эфир' in self.driver.page_source 
        self.base_page.click(vk_locators.MainPageLocators.EDUCATION_BUTTON, timeout=10)
        assert '#904: Программа по веб-разработке ' in self.driver.page_source
        self.base_page.click(vk_locators.MainPageLocators.EMAIL_PASS_CONTINUE_LOCATOR, timeout=10)
        self.base_page.click(vk_locators.MainPageLocators.LESSONS, timeout=10)
        assert 'Лекция 1' in self.driver.page_source  
        self.base_page.click(vk_locators.MainPageLocators.SEMINAR2, timeout=10) 
        assert 'End-to-End тесты на Python' in self.driver.page_source

    def test_search_Ilia(self): 
        self.base_page.click(vk_locators.MainPageLocators.SEARCH_OPEN, timeout=10)
        self.base_page.search("Андриянов Илья\n")
        assert 'Прямой эфир' not in self.driver.page_source  
        self.base_page.click(vk_locators.MainPageLocators.ILIA, timeout=10)
        assert 'Хорошо, договорились' in self.driver.page_source  
