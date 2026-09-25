from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # URL of the website
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Locators - these tell Selenium where to find elements on the page
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")

    def __init__(self, driver):
        self.driver = driver
        # WebDriverWait will wait up to 10 seconds for an element to appear
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        # Navigate to the login page
        self.driver.get(self.URL)

    def enter_username(self, username):
        # Wait for username field to appear, then type the username
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        # Wait for password field to appear, then type the password
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        # Click the login button
        button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        button.click()

    def get_error_message(self):
        # Grab the error message text when login fails
        error = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error.text

    def login(self, username, password):
        # This is a helper method - does all login steps in one call
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()