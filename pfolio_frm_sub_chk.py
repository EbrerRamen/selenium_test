from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://abrar-portfolio-six.vercel.app/")

name = driver.find_element(By.ID, "name")
name.send_keys("Selenium")

email = driver.find_element(By.ID, "email")
email.send_keys("selenium@xyz.com")

message = driver.find_element(By.ID, "message")
message.send_keys("Hi! This is Selenium")

submit_btn = driver.find_element(By.CSS_SELECTOR, "button")
submit_btn.click()

time.sleep(10)
driver.quit()