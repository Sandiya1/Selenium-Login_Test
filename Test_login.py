from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
folder = os.path.join(os.path.dirname(__file__), "screenshots")
if not os.path.exists(folder):
    os.makedirs(folder)

#---TestCase1:Valid Username and Password---#

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.CLASS_NAME,"btn").click()
time.sleep(5)
m=driver.find_element(By.CLASS_NAME,"post-title").text.strip()
if "Logged In Successfully" in m:
    print("Test passed!")
    driver.save_screenshot(f"{folder}/valid_login.png")
else:
    driver.save_screenshot(f"{folder}/invalid_login.png")
    print("Test Failed")

#---Test Case2:Invalid Username--#

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

driver.find_element(By.ID, "username").send_keys("student123")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.CLASS_NAME,"btn").click()
time.sleep(5)
m = driver.find_element(By.ID, "error").text
if "Your username is invalid!" in m:
    print("Invalid username")
    driver.save_screenshot(f"{folder}/invalid_username.png")
else:
    print("Test passed")

#----TestCase3:IvalidPassword---#

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Passwrd123")
driver.find_element(By.CLASS_NAME,"btn").click()
time.sleep(5)
msg = driver.find_element(By.ID, "error").text
if "Your password is invalid!" in msg:
    print("Invalid password")
    driver.save_screenshot(f"{folder}/Invalid_username.png")
else:
    print("Test Passed")
    

#---TestCase4:Blank Username--#

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys(" ")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.CLASS_NAME,"btn").click()
time.sleep(5)
m= driver.find_element(By.ID, "error").text
if "Your username is invalid!" in m:
    print("Blank fields passed")
    driver.save_screenshot(f"{folder}/blank_fields_fail.png")
else:
    print("Test passed")

driver.quit()