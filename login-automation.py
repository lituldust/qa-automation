import pandas as pd
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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

WebDriverWait(driver, 60)
driver.quit()