import pytest
from ui.locators import vk_locators
from _pytest.fixtures import FixtureRequest
import time
from ui.vk_pages.base_page import BasePage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = (request.getfixturevalue('vk_base_page')) 
        self.base_page.login("razrushitelyvselennoy@mail.ru", "gamilton13")
        #self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
        pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    login_locators = vk_locators.LoginPageLocators()
    main_locators = vk_locators.MainPageLocators()
    url = 'https://education.vk.company/'

    def login(self, user, password):
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        pass


class TestLK(BaseCase):

    @pytest.mark.skip('skip')
    def test_lk1(self):
        self.base_page.click(vk_locators.MainPageLocators.EDUCATION_BUTTON, timeout=10)
        self.base_page.click(vk_locators.MainPageLocators.EMAIL_PASS_CONTINUE_LOCATOR, timeout=10)
        self.base_page.click(vk_locators.MainPageLocators.LESSONS, timeout=10)
        self.base_page.click(vk_locators.MainPageLocators.SEMINAR2, timeout=10)

    def test_lk2(self):
        
        self.base_page.click(vk_locators.MainPageLocators.SEARCH_OPEN, timeout=10)
        self.base_page.search("Андриянов Илья\n")
        self.base_page.click(vk_locators.MainPageLocators.ILIA, timeout=10)
        time.sleep(5)


    def test_lk3(self):
        pass
