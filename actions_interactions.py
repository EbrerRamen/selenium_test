from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://abrar-portfolio-six.vercel.app/")

# send_keys()

name = driver.find_element(By.ID, "name")
name.send_keys("Selenium")

name.clear() # Clear before typing (recommended)
name.send_keys("Abrar", Keys.TAB)

email = driver.find_element(By.ID, "email")
email.send_keys("xyz@xyz.com")

message = driver.find_element(By.ID, "message")
message.send_keys("Testing", Keys.ENTER)

time.sleep(3)

