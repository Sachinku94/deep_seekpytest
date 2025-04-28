import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    # Setup: Initialize browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver  # This is where the test runs

    # Teardown: Close the browser after the test
    driver.quit()
