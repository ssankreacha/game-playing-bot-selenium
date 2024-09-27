from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# TODO - Obtain the dates and event names listed on python.org, and append them to a dictionary.

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Dictionary to store event information
event_info = {}

# Loop through the first 5 events and extract time and event details
for i in range(1, 6):  # 1 to 5
    event_dict = {}
    event_date = driver.find_element(By.XPATH,
                                     value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time').text
    event_info_text = driver.find_element(By.XPATH,
                                          value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text

    event_dict["Time"] = event_date
    event_dict["Event"] = event_info_text

    # Assign the event dictionary to the final dictionary with a numbered key
    event_info[i - 1] = event_dict

# Print the final event_info dictionary
print(event_info)

# Close the browser
driver.quit()