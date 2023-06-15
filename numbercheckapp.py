import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import sys


sys.tracebacklimit = 0

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Chromedriver path
chromedriver_path = "chromedriver.exe"

# Start the Selenium driver
service = Service(chromedriver_path)


# Read numbers from the Excel file
data = pd.read_excel("yourexcelfiles.xlsx")
numbers = data["numara"].tolist()



# Open WhatsApp Web using Selenium
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com/")
input("Open WhatsApp Web and press ENTER to continue...")


# Send messages to all numbers

# Iterate through all rows
for i, number in enumerate(numbers):
    try:
        # Send message on WhatsApp
        driver.get("https://web.whatsapp.com/send?phone={}".format(number))

        message_box_xpath = (
            "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"
        )
        message_box = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, message_box_xpath))
        )

    except:
        # If the number cannot be used on WhatsApp, add the number to the list
        print("Number cannot be used on WhatsApp: {}".format(number))
    else:
        # After processing the number, update the dataframe
        data.at[i, "is_processed"] = True
        data.at[i, "processed_time"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")

        # Update the Excel file
        data.to_excel("yourexcelfilesregenerate.xlsx", index=False)

# Update the Excel file
data.to_excel("yourexcelfilesregenerate.xlsx", index=False)


# Close the driver
driver.quit()
