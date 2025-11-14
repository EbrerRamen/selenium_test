# 🚀 Selenium Python Learning Journey  
*A complete step-by-step guide documenting everything learned so far.*

This repository contains code examples and notes from my journey to becoming job-ready in **Selenium with Python**.  
It covers concepts from absolute basics → intermediate topics → real-world automation skills.

---

# 📌 Contents Covered So Far

## ✅ Stage 1 — Selenium Setup & Basics
- Installing Python & pip
- Installing Selenium
- Installing a WebDriver (ChromeDriver)
- First automation script:
  ```python
  from selenium import webdriver
  driver = webdriver.Chrome()
  driver.get("https://example.com")
  ```
- Understanding WebDriver, WebElement, and browser actions (open, close, quit)

---

## ✅ Stage 2 — Locators & Web Elements  
### Locating elements using By
- By.ID
- By.NAME
- By.CLASS_NAME
- By.TAG_NAME
- By.LINK_TEXT
- By.PARTIAL_LINK_TEXT
- By.XPATH
- By.CSS_SELECTOR
### XPath Techniques
- Basic tag selection: //tag
- Attribute-based: //input[@name='email']
- Text-based: //li[text()='IBangladesh']
- Contains: //button[contains(text(),'Login')]
- Class chaining in CSS: div.class1.class2
- Handling multiple elements using find_elements

---

## ✅ Stage 3 — Waits & Timing
### Implicit Wait
  ```python
  driver.implicitly_wait(10)
  ```
### Explicit Wait + Expected Conditions
- presence_of_element_located
- visibility_of_element_located
- element_to_be_clickable
- title_contains
- url_contains
- alert_is_present
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  
  element = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, "username"))
  )
  ```

---

## ✅ Stage 4 — Actions & Interactions
### ✔ 4.1 Typing Into Fields (send_keys)
- Typing text
- Clearing input fields
- Using keyboard keys (ENTER, TAB, etc.)
### 4.2 Clicking Elements
- Normal click
- Element click vs JS click
  ```python
  driver.execute_script("arguments[0].click();", element)
  ```
- Why arguments[0]? → Passed as first function argument to the JS script
### ✔ 4.3 Scrolling
- driver.execute_script("window.scrollBy(...)")
- Scroll to element
- Scroll to bottom/top
### 4.4 Handling Dropdowns (Select)
- select_by_visible_text
- select_by_value
- select_by_index
- Handling non-<select> custom dropdowns (click + option click)
### 4.5 Handling Checkboxes & Radio Buttons
- .click()
- .is_selected()
- Looping through groups
- Selecting based on label text
### 4.6 Advanced Mouse Actions — ActionChains
- Hover (move_to_element)
- Right click (context_click)
- Double click
- Click and hold
- Move by offset
- Drag & Drop (simple & manual)
- Chaining multiple actions

---















  
