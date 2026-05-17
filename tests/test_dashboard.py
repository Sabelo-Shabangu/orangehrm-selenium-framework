from conftest import LOGIN_URL
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_dashboard_visible(driver):
    driver.get(LOGIN_URL)

    login = LoginPage(driver)
    login.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_visible()
