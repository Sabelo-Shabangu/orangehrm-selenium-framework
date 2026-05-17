from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DashboardPage:

    header = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_dashboard_visible(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.header)
        )
        return element.is_displayed()
