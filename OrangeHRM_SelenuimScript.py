from selenium import webdriver
from selenium.webdriver.common.by import By
import time   

driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.NAME , "username").send_keys("Admin")
driver.find_element(By.NAME , "password").send_keys("Admin123")
driver.find_element(By.CSS_SELECTOR , "button[type = 'submit']").click()

time.sleep(3)


driver.quit()
