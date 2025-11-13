from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.implicitly_wait(10) # Wait up to 10 seconds for any element

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.find_element(By.ID, "my-text-id").send_keys("Hello")

# if the element appears before 10 seconds -> continues immediately.
# if not -> throws an error after 10 seconds.