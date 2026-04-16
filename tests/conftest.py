import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    options = Options()

    # CI/CD stable configuration (Jenkins safe)
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # FIX for DevToolsActivePort error
    options.add_argument("--remote-debugging-port=0")

    # Prevent session/profile lock issues
    options.add_argument("--user-data-dir=C:/temp/chrome-profile")

    # Stability improvements
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")

    service = Service()

    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()
