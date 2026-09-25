import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEmployee:

    # This is a helper to login before each employee test
    def login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("dashboard"))

    # Test 1: Navigate to Employee List page
    def test_navigate_to_employee_list(self, driver):
        self.login(driver)

        wait = WebDriverWait(driver, 10)

        # Click on "PIM" in the left side menu
        pim_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_menu.click()

        # Check that we landed on the Employee List page
        wait.until(EC.url_contains("viewEmployeeList"))
        assert "viewEmployeeList" in driver.current_url, "Did not navigate to Employee List"
        print("✅ Navigate to Employee List test passed!")

    # Test 2: Search for an employee by name
    def test_search_employee_by_name(self, driver):
        self.login(driver)

        wait = WebDriverWait(driver, 10)

        # Go to PIM > Employee List
        pim_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_menu.click()
        wait.until(EC.url_contains("viewEmployeeList"))

        # Type employee name in the search field
        # Note: OrangeHRM uses a custom input, so we find it by placeholder
        search_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        ))
        search_input.send_keys("Paul")

        # Click the Search button
        search_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Search']")
        ))
        search_btn.click()

        # Wait for results to load and check that table is visible
        import time
        time.sleep(2)  # small wait for results to appear

        results = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
        assert len(results) > 0, "No employee results found for 'Paul'"
        print(f"✅ Search Employee test passed! Found {len(results)} result(s)")

    # Test 3: Verify employee list table has records
    def test_employee_list_has_records(self, driver):
        self.login(driver)

        wait = WebDriverWait(driver, 10)

        # Navigate to employee list
        pim_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_menu.click()
        wait.until(EC.url_contains("viewEmployeeList"))

        # Click search without any filter to load all employees
        search_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Search']")
        ))
        search_btn.click()

        import time
        time.sleep(2)

        # Check the record count text is visible
        record_count = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Records Found')]")
        ))
        assert record_count.is_displayed(), "Record count not visible"
        print(f"✅ Employee list records test passed! {record_count.text}")