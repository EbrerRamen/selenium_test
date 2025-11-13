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

"""
element_to_be_clickable
Waits until an element is both:
1. Visible (displayed on the page), and
2. Enabled (not disabled or covered by another element)
In simple terms: 
"Wait until I can actually click this element safely."
"""

button = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
button.click()

"""
This wait up to 10 seconds for the element with ID "submit" to be ready to click.
If it doesn't become clickable -> Selenium raises a TimeoutException.
"""

"""
# title_contains("...")
Waits until the current page's title contains a given substring
Think of it as:
"Wait until the page title updates to include this text."
"""
wait.until(EC.title_contains("Dashboard"))
print("Dashboard page is loaded!")
"""
Waits up to 10 seconds for the page title to include "Dashboard".
Raises a TimeoutException if it doesn't appear in time.
"""

"""
# url_contains("...")
Waits until the current page's URL contains a specific substring.
in simple terms:
"Wait until the browser's address bar includes this text"
"""
wait.until(EC.url_contains("/dashboard"))
print("Redirected to dashboard page!")

