from ui.locators import vk_locators
from ui.vk_pages.base_page import BasePage


class EventsPage(BasePage):

    locators = vk_locators.EventsPageLocators()
    url = 'https://education.vk.company/'
