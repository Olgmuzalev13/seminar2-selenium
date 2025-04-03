from selenium.webdriver.common.by import By


class BasePageLocators:
    ENTER_LOCATOR = (By.NAME, 'вход / регистрация') 
    EMAIL_PASS_CONTINUE_LOCATOR = (By.NAME, 'Продолжить с помощью почты и пароля')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')

class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass
