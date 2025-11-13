from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

wait = WebDriverWait(driver, 10)
"""
presence_of_element_located
Waits until an element is present in the DOM, even if it's not visible yet on the page.
"Has this element been loaded into the HTML yet?"
It does not matter whether it's hidden (e.g. display: none) or off-screen.
"""
element = wait.until(EC.presence_of_element_located((By.ID, "my-text-id")))
"""
If the element if found in the DOM before 10 seconds, it returns it immediately.
if not found within 10 seconds -> TimeoutException.
"""
element.send_keys("Abrar")

"""
#visibility_of_element_located
Waits until the element is:
1. Present in the DOM, and
2. Visible (i.e. displayed on the page, not hidden by CSS or off-screen)
"""
element = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)
"""
Selenium keeps checking every few milliseconds until the element in visible.
Once it is, the condition passes and returns the element.
if it doesn't appear within 10 seconds -> TimeoutException.
"""