from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://abrar-portfolio-six.vercel.app/")

name = driver.find_element(By.ID, "name")
name.send_keys("Selenium")

name.clear() # Clear before typing (recommended)
name.send_keys("Abrar")

time.sleep(3)

