import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:

    # Test 1: Valid login - should land on dashboard
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard = DashboardPage(driver)

        # Check that we actually landed on the dashboard
        assert dashboard.is_loaded(), "Dashboard did not load after valid login"
        print("✅ Valid login test passed!")

    # Test 2: Invalid login - should show error message
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("wronguser", "wrongpassword")

        error_msg = login_page.get_error_message()

        # Check that the error message contains expected text
        assert "Invalid credentials" in error_msg, f"Unexpected error message: {error_msg}"
        print("✅ Invalid login test passed!")

    # Test 3: Blank credentials - should show error message
    def test_blank_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_login()  # clicking login without entering anything

        # Both fields should show 'Required' error
        # We check the page source as a simple approach
        assert "Required" in driver.page_source, "Required validation message not shown"
        print("✅ Blank login test passed!")

    # Test 4: Logout after valid login
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard = DashboardPage(driver)
        assert dashboard.is_loaded(), "Login failed, can't test logout"

        dashboard.logout()

        # After logout, we should be back on login page
        assert "login" in driver.current_url, "Did not redirect to login page after logout"
        print("✅ Logout test passed!")