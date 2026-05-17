from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    error_msg = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def enter_username(self, username):
        element = self.wait.until(EC.element_to_be_clickable(self.username))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait.until(EC.element_to_be_clickable(self.password))
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_msg)
        ).text

    def is_error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.error_msg))
            return True
        except Exception:
            return False
