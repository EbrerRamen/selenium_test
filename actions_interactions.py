from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://abrar-portfolio-six.vercel.app/")

# Typing Into Input Fields (send_keys)

name = driver.find_element(By.ID, "name")
name.send_keys("Selenium")

name.clear() # Clear before typing (recommended)
name.send_keys("Abrar", Keys.TAB)

email = driver.find_element(By.ID, "email")
email.send_keys("xyz@xyz.com")

message = driver.find_element(By.ID, "message")
message.send_keys("Testing", Keys.ENTER)

# Clicking (All Types)

# Normal click
submit_btn = driver.find_element(By.CSS_SELECTOR, "button")
submit_btn.click()

"""
Best practice:
Use waits before clicking

button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
button.click()
"""

# Double Click
from selenium.webdriver import ActionChains

element = driver.find_element(By.ID, "box")
ActionChains(driver).double_click(element).perform()

# Right Click (Context Click)
element = driver.find_element(By.ID, "box")
ActionChains(driver).context_click(element).perform()

# Click Using JavaScript (When Normal Click Fails)
"""
Sometimes .click() doesn't work because:
- The element is hidden behind another element
- The site uses fancy JavaScript frameworks (React, Vue, Angular)
- The click is intercepted
"""
element = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", element)
"""
This is the go-to solution when:
ElementClickInterceptedException
keep happening.
"""

"""
Clicking by Coordinate (Rare but Useful)
Used when an element is not selectable
"""
ActionChains(driver).move_by_offset(200, 300).click().perform()

# 1. Scroll by Pixel Amount
driver.execute_script("window.scrollBy(0, 300);")
# This scrolls down by 300 pixels.

# Scroll up by pixels
driver.execute_script("window.scrollBy(0, -300);")

"""
Format:
window.scrollBy(x-axis, y-axis)
x = horizontal 
y = vertical
"""

# 2. Scroll to the Bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
"""
Useful for: 
- Infinite scroll pages
- Twitter-like feeds
- Lazy-loaded pages
"""

#  3. Scroll to the Top
driver.execute_script("window.scrollTo(0, 0);")

# 4. Scroll Until an Element Is Visible (Most Important)
element = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
"""
Why it's so good?
- Brings element into view
- Works even if the element is far down
- Prevents "element not clickable" errors
- It scrolls EXACTLY to the element
"""

# Scroll element is centered
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

# 5. Scroll Inside a Specific DIV (Not Whole Page)

# Sometimes the scrollable area is not the page but a container
scroll_box = driver.find_element(By.CSS_SELECTOR, ".scroll-container")

driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
# This scrolls inside the box, not the page.

# Scroll horizontally 
driver.execute_script("arguments[0].scrollLeft += 300;", scroll_box)

# Selenium has no native scrolling method. Everything is done using JS.

# Handling Dropdowns
# Selenium dropdowns are handled in two main ways

# Type 1: HTML <select> Dropdown (Standard Dropdown)
"""
These are the real dropdowns that use the <select> tag.
<select id="country">
  <option value="bd">Bangladesh</option>
  <option value="in">India</option>
  <option value="pk">Pakistan</option>
</select>
"""

from selenium.webdriver.support.ui import Select

select = Select(driver.find_element(By.ID, "country"))
select.select_by_visible_text("Bangladesh")
# or select.select_by_value("bd")
# or select.select_by_index(2)

# Type 2: Custom Dropdown (Non-Select Dropdown)
"""
Many modern websites do NOT use <select>.
Example: React, Bootstrap, Tailwind, Material UI dropdowns.
They look like dropdowns but are just <div>, <li>, <button>
<div class="dropdown">
  <div class="menu-btn">Choose Country</div>
  <ul class="menu">
    <li>Bangladesh</li>
    <li>India</li>
    <li>Pakistan</li>
  </ul>
</div>
"""

# How to handle?

# 1. Click dropdown
driver.find_element(By.CLASS_NAME, "menu-btn").click()

# 2. Click option
driver.find_element(By.XPATH, "//li[text()='Bangladesh']").click()

# Handling Checkboxes
"""
A checkbox is usually like:
<input type="checkbox" id="subscribe">
"""

# 1. Selecting a Checkbox
checkbox = driver.find_element(By.ID, "subscribe")
checkbox.click()

# 2. Checking if Checkbox is Selected
checkbox.is_selected() # returns True or False

# 3. Avoid Clicking if Already Selected (best practice)
if not checkbox.is_selected():
    checkbox.click()
# This prevents unnecessary clicks.

# 4. Selecting Multiple Checkboxes
"""
Example HTML:
<input type="checkbox" value="python">
<input type="checkbox" value="java">
<input type="checkbox" value="csharp">
"""
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for box in checkboxes:
    box.click()
time.sleep(3)


