from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# TODO - Create an automation bot for the Cookie Clicker Game.

"""
1. Initialise the bot
2. Retrieve Cookie, Upgrade costs and buttons
3. Check whether upgrades can be bought and click them
4. Leave the bot running for 5 minutes
5. After 5 minutes, the game should show a message and close the browser.

"""

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the page to load
time.sleep(5)

# Find the cookie element by ID
cookie = driver.find_element(By.ID, "bigCookie")

# Track the start time
start_time = time.time()

# Click the cookie repeatedly and check for upgrades
while True:
    # Click the cookie
    cookie.click()

    # Check for upgrades every 5 seconds
    if time.time() - start_time >= 5:
        cookies_earned = int(driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split(" ")[0].replace(",", ""))
        upgrade_1_cost = int(driver.find_element(By.XPATH, '//*[@id="productPrice0"]').text.replace(",", ""))
        upgrade_2_cost = int(driver.find_element(By.XPATH, '//*[@id="productPrice1"]').text.replace(",", ""))
        upgrade_3_cost = int(driver.find_element(By.XPATH, '//*[@id="productPrice2"]').text.replace(",", ""))

        # Check which upgrade can be afforded
        if cookies_earned >= upgrade_3_cost:
            driver.find_element(By.XPATH, '//*[@id="product2"]').click()
        elif cookies_earned >= upgrade_2_cost:
            driver.find_element(By.XPATH, '//*[@id="product1"]').click()
        elif cookies_earned >= upgrade_1_cost:
            driver.find_element(By.XPATH, '//*[@id="product0"]').click()

        # Reset the timer
        # start_time = time.time()

    # After 5 minutes, display the message and quit
    if time.time() - start_time >= 300:  # 300 seconds = 5 minutes
        comment_section = driver.find_element(By.XPATH, '//*[@id="commentsText1"]')
        driver.execute_script('arguments[0].innerText = "You are the Cookie King!";', comment_section)
        time.sleep(5)  # Give a few seconds to show the message
        break

driver.quit()  # Close the browser
