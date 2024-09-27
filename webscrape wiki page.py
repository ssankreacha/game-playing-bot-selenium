from selenium import webdriver
from selenium.webdriver.common.by import By

# TODO - Obtain the number of visits from a wikipedia page.

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

event_date = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
print(event_date)

driver.close()
driver.quit()
