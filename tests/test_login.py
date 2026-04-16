from pathlib import Path
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Ensure imports work when running from project root/Jenkins workspace.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.login_page import LoginPage


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
