import pandas as pd
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import random

# Set random seed
random.seed(101)

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

# Go to Sign-up page
signup_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/signup']")))
signup_page.click() 

# Sign-up
rand_num = random.randint(1000, 9999)
email = f"test{rand_num}@gmail.com"
print(email)
password = "TestPassword123"

# Fill the sign-up form
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    print("Can fill the sign-up form")
except Exception as e:
    print(f"Can't fill the sign-up form: {e}")
    driver.quit()
    exit()

driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
driver.find_element(By.XPATH, "//input[@id='confirm']").send_keys(password)

# Submit the sign-up form
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
submit_button.click()

# Check if the sign-up is successful
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@class='text-lg sm:text-xl md:text-2xl font-semibold py-4']"))
    )
    print("Sign-up successful")
except Exception as e:
    print(f"Sign-up failed: {e}")
    driver.quit()
    exit()

WebDriverWait(driver, 60)
driver.quit()