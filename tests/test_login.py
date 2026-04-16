from pathlib import Path
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Ensure imports work when running from project root/Jenkins workspace.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()

    # CI/CD-stable Chrome configuration for Jenkins.
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Optional stability flag for some CI environments.
    options.add_argument("--remote-debugging-port=9222")

    # Prevent profile lock issues in Jenkins.
    options.add_argument("--user-data-dir=C:/temp/chrome-profile")

    service = Service()

    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()


def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 15)
    dashboard_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    assert "dashboard" in driver.current_url.lower()
    assert dashboard_header.is_displayed()
