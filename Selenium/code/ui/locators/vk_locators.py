from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_LOCATOR = (By.CLASS_NAME, 'AuthButton__SAuthLink-sc-1iwc4q0-0') 
    EMAIL_PASS_CONTINUE_LOCATOR = (By.XPATH, '//button[text()="Продолжить с помощью почты и пароля"]')
    EMAIL = (By.XPATH, '//*[@id="email"]')
    PASS = (By.XPATH, '//*[@id="password"]')
    CONFIRM_ENTER = (By.XPATH, '//button[text()="Войти с паролем"]')
    CLOSE_NEW_VERSION = (By.CLASS_NAME, 'style__SCloseButton-krRQYT') 

class MainPageLocators(LoginPageLocators):
    EDUCATION_BUTTON = (By.XPATH, "//a[contains(@href, '/curriculum/program/')]") 
    EMAIL_PASS_CONTINUE_LOCATOR = (By.XPATH, "//a[contains(@href, '/curriculum/program/discipline/2459/')]") 
    LESSONS = (By.XPATH, '//a[text()="Занятия"]')
    SEMINAR2 = (By.XPATH, '//a[contains(@href, "/curriculum/program/lesson/30921/")]')

    SEARCH_OPEN = (By.XPATH, '//ul/li[@class="js-show-search"]/a[contains(@href, "#")]')
    SEARCH = (By.XPATH, '//ul/li[@class="js-search-input"]/form/input') 
    ILIA = (By.XPATH, '//a[contains(@href, "https://education.vk.company/profile/i.andriianov/")]')

