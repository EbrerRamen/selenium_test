from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# 5. By.LINK_TEXT
driver.find_element(By.LINK_TEXT, "Return to index").click()
driver.back()

# 6. By.PARTIAL_LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "Return").click()
time.sleep(5)
driver.back()

# 7. By.CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("css selector")

time.sleep(3)

driver.quit()