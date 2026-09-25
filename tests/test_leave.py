import time
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLeave:

    # Helper method to login before each test
    def login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("dashboard"))

    # Test 1: Navigate to Leave module
    def test_navigate_to_leave(self, driver):
        self.login(driver)

        wait = WebDriverWait(driver, 10)

        # Click on "Leave" in the left side menu
        leave_menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Leave']")
        ))
        leave_menu.click()

        # Verify we landed on the Leave List page
        wait.until(EC.url_contains("leaveList"))
        assert "leaveList" in driver.current_url, "Did not navigate to Leave page"
        print("✅ Navigate to Leave module test passed!")

    # Test 2: Verify Leave List page has loaded properly
    def test_leave_list_page_loads(self, driver):
        self.login(driver)

        wait = WebDriverWait(driver, 10)

        # Navigate to Leave
        leave_menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Leave']")
        ))
        leave_menu.click()
        wait.until(EC.url_contains("leaveList"))

        # Check that the page heading is visible
        heading = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h5[text()='Leave List']")
        ))
        assert heading.is_displayed(), "Leave List heading not visible"
        print("✅ Leave List page load test passed!")

    # Test 3: Search leave records by clicking Search without any filter
    def test_search_leave_records(self, driver):
        self.login(driver)

        wait = WebDriverWait(driver, 10)

        # Navigate to Leave
        leave_menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Leave']")
        ))
        leave_menu.click()
        wait.until(EC.url_contains("leaveList"))

        # Click the Search button without applying any filter
        search_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Search']")
        ))
        search_btn.click()

        time.sleep(2)  # wait for results to load

        # Check that records are shown in the table
        record_count = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Records Found')]")
        ))
        assert record_count.is_displayed(), "No records found on leave list"
        print(f"✅ Leave search test passed! {record_count.text}")