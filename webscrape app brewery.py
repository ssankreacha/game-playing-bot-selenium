from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# TODO - Use Selenium to fill out a form

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

# Input details into fields
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("S")

second_name = driver.find_element(By.NAME, value="lName")
second_name.send_keys("S")

email = driver.find_element(By.NAME, value="email")
email.send_keys("s@gmail.com")

# Click sign up button
button = driver.find_element(By.CLASS_NAME, value="btn")
button.send_keys(Keys.ENTER)

# driver.close()
# driver.quit()
