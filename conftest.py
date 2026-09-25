import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# This fixture runs before and after each test automatically
# It opens the browser, gives it to the test, then closes it
@pytest.fixture()
def driver():
    print("\nOpening Chrome browser...")

    # Setting up some basic Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # open browser in full screen

    # Starting the Chrome browser
    driver = webdriver.Chrome(options=chrome_options)

    # This 'yield' gives the driver to the test that needs it
    yield driver

    # After the test is done, this runs automatically to close the browser
    print("\nClosing Chrome browser...")
    driver.quit()


# This hook runs automatically after every test
# If a test fails, it takes a screenshot and saves it
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Only take screenshot if the test has failed
    if result.when == "call" and result.failed:

        # Get the driver from the test's fixtures
        driver = item.funcargs.get("driver")

        if driver:
            # Create screenshots folder if it doesn't exist
            screenshots_dir = "screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            # Save screenshot with the test name
            test_name = item.name
            screenshot_path = os.path.join(screenshots_dir, f"{test_name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Screenshot saved: {screenshot_path}")