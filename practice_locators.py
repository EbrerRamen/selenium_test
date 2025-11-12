from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 1. By.ID
driver.find_element(By.ID, "my-text-id").send_keys("Using ID")

# 2. By.NAME
driver.find_element(By.NAME, "my-password").send_keys("Password")

# 3. By.CLASS_NAME
driver.find_element(By.CLASS_NAME, "form-control").send_keys(" This goes to the first field that has classname of form-control")

# 4. By.TAG_NAME
print(driver.find_element(By.TAG_NAME, "h1").text)

time.sleep(5)