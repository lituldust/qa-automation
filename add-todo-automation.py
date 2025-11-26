import pandas as pd
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import random

# Web URL
url = "https://todo-list-six-umber-66.vercel.app/"

# Open the web using chrome driver
service = ChromeService('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(url)
driver.maximize_window()

# Check if the web is opened and go to login page
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Go to Login →"))
    )
    print("Can go to login page")
except Exception as e:
    print(f"Can't go to login page: {e}")
    driver.quit()
    exit()

login_page = driver.find_element(By.LINK_TEXT, "Go to Login →")
login_page.click() 

# login
email = "test@gmail.com"
password = "TestPassword123"

# Fill the login form
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    print("Can fill the login form")
except Exception as e:
    print(f"Can't fill the login form: {e}")
    driver.quit()
    exit()

driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

# Submit the login form
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
submit_button.click()

# Check if the login is successful
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@class='text-lg sm:text-xl md:text-2xl font-semibold py-4']"))
    )
    print("Login successful")
except Exception as e:
    print(f"Login failed: {e}")
    driver.quit()
    exit()

# Go to todo page
todo_page = driver.find_element(By.XPATH, "//a[@href='/todo']")
todo_page.click()

# Add todo
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Add New Task']]"))
    )
    print("Can add todo")
except Exception as e:
    print(f"Can't add todo: {e}")
    driver.quit()
    exit()

add_todo_button = driver.find_element(By.XPATH, "//button[.//span[text()='Add New Task']]")
add_todo_button.click()

# Insert detail information for todo
task_name = "Test"
task_description = "Test"
date_value = "2025-06-20" 
time_value = "23:59"

# Name, Desc
driver.find_element(By.XPATH, "//input[@id='taskName']").send_keys(task_name)
driver.find_element(By.XPATH, "//textarea[@id='taskDescription']").send_keys(task_description)

# Deadline, Time
date_input = driver.find_element(By.XPATH, "//input[@id='taskDeadline']")
time_input = driver.find_element(By.XPATH, "//input[@id='taskDeadlineTime']")

driver.execute_script("arguments[0].value = arguments[1];", date_input, date_value)
driver.execute_script("arguments[0].value = arguments[1];", time_input, time_value)

# Tag
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='taskTag']"))
dropdown.select_by_visible_text("Personal")

# Submit
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(10)
driver.quit()