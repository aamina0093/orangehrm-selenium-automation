from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    # Locators
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    USER_DROPDOWN = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_OPTION = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        # Check if Dashboard header is visible - confirms successful login
        try:
            self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER))
            return True
        except:
            return False

    def get_current_url(self):
        # Returns the current URL - useful to verify we are on the right page
        return self.driver.current_url

    def logout(self):
        # Click on user dropdown and then click Logout
        self.wait.until(EC.element_to_be_clickable(self.USER_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_OPTION)).click()