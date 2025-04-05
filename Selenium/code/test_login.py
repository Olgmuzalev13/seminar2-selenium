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



class TestLogin(BaseCase):
    authorize = False
    def test_login(self, request: FixtureRequest):
        login, password = request.getfixturevalue("credentials")
        self.base_page.login(login, password)
        user_bar = self.base_page.find(vk_locators.MainPageLocators.USER_MENU, timeout=10)
        assert user_bar is not None


class TestLK(BaseCase):
    authorize = True


    def test_get_seminar_info(self):
        assert 'Прямой эфир' in self.driver.page_source 
        self.base_page.get_topic_page_by_id(id="2459")
        self.base_page.click(vk_locators.MainPageLocators.LESSONS, timeout=10)
        assert 'Лекция 1' in self.driver.page_source
        self.base_page.get_lesson_by_id(id="30921")
        assert 'End-to-End тесты на Python' in self.driver.page_source

    def test_search_Ilia(self): 
        self.base_page.click(vk_locators.MainPageLocators.SEARCH_OPEN, timeout=10)
        self.base_page.search("Андриянов Илья\n")
        self.base_page.get_student_by_address(address="i.andriianov")
        assert self.driver.title =="Профиль - Илья Андриянов - VK Education"
