from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 1. By.ID
driver.find_element(By.ID, "my-text-id").send_keys("Using ID")

# 2. By.NAME

driver.find_element(By.NAME, "my-password").send_keys("Password")

time.sleep(5)