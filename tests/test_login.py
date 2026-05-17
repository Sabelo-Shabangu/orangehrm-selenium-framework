from pathlib import Path

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import LOGIN_URL
from pages.login_page import LoginPage
from utils.csv_reader import read_csv

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "login_data.csv"


def _login_test_data():
    return [
        (row["username"], row["password"], row["expected"])
        for row in read_csv(DATA_FILE)
    ]


@pytest.mark.parametrize("username,password,expected", _login_test_data())
def test_login(driver, username, password, expected):
    driver.get(LOGIN_URL)

    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    if expected == "success":
        WebDriverWait(driver, 15).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url.lower()
    else:
        assert login.is_error_displayed()
        assert login.get_error_message().strip() != ""
