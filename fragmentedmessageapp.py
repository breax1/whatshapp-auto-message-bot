from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import pandas as pd
import pyautogui
import time
import sys

sys.tracebacklimit = 0
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Set the path to the chromedriver
chromedriver_path = ('chromedriver.exe')
# Start the selenium driver
service = Service(chromedriver_path)

message_part_1 = "message 1"
message_part_2 = "message 2"
message_part_3 = "message 3"
message_part_4 = "message 4"
message_part_5 = "message 5"

image_pathdata = r'C:\Users\enesa\Masaüstü\exceltowpbot\breax.png'
print(image_pathdata)

# Read numbers from excel file
data = pd.read_excel('yourexcelfiles.xlsx')
numbers = data['numara'].tolist()

# Open WhatsApp Web with selenium
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://web.whatsapp.com/')
input("Press ENTER")

for i, number in enumerate(numbers):
    try:
        driver.get('https://web.whatsapp.com/send?phone={}'.format(number))

        message_box_xpath = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, message_box_xpath)))
        message_box.send_keys(message_part_1)
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        message_box.send_keys(message_part_2)
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        message_box.send_keys(message_part_3)
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        message_box.send_keys(message_part_4)
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        message_box.send_keys(message_part_5)
        
        # Click send button
        send_button_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'
        send_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, send_button_xpath)))
        send_button.click()
        time.sleep(3)

    except:
        try:
            driver.get('https://web.whatsapp.com/send?phone={}'.format(number))

            message_box_xpath = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"
            message_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, message_box_xpath)))
            message_box.send_keys(message_part_1)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            message_box.send_keys(message_part_2)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            message_box.send_keys(message_part_3)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            message_box.send_keys(message_part_4)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            message_box.send_keys(message_part_5)
            
            # Click send button
            send_button_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'
            send_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, send_button_xpath)))
            send_button.click()
            time.sleep(3)
        except:
            data.at[i, "is_processed"] = False
            data.at[i, "processed_time"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Update excel file
            data.to_excel("yourexcelfilesdata.xlsx", index=False)

data.to_excel("yourexcelfilesdata.xlsx", index=False)

driver.quit()
