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

with open('message.txt', 'r') as f:
    for line in f:
        # Split each line by "="
        parts = line.split('=')
        # Remove leading and trailing whitespaces from the second part
        value = parts[1].strip()

        # Check the variable and assign it as a string
        if parts[0].strip() == 'message':
            messagedata = str(value)
        elif parts[0].strip() == 'image_path':
            image_pathdata = str(value)

# Convert messagedata from ISO-8859-9 encoding to utf-8
messagedata = messagedata.encode('ISO-8859-9').decode('utf-8')

sys.tracebacklimit = 0

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Set the path to the chromedriver
chromedriver_path = ('chromedriver.exe')

# Start the selenium driver
service = Service(chromedriver_path)

# Read numbers from the excel file
data = pd.read_excel('yourexcelfiles.xlsx')
numbers = data['numara'].tolist()

# Type your message
message = messagedata

# Open WhatsApp Web with selenium
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://web.whatsapp.com/')
input("Open WhatsApp Web and press ENTER to continue...")

# Send message to all numbers
for number in numbers:
    # Open chat
    driver.get('https://web.whatsapp.com/send?phone={}'.format(number))

    message_box_xpath = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"
    message_box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, message_box_xpath)))
    message_box.send_keys(message)

    # Add picture
    attachment_icon_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
    attachment_icon = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, attachment_icon_xpath)))
    attachment_icon.click()

    time.sleep(1)
    image_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span'
    image_box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, image_box_xpath)))
    image_box.click()

    dialog_box_xpath = '//input[@type=\'file\']'
    dialog = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, dialog_box_xpath)))
    dialog.send_keys(r"{}".format(image_pathdata))

    pyautogui.press('esc')

    # Click send button
    send_button_xpath = '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'
    send_button = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, send_button_xpath)))
    send_button.click()
    time.sleep(4)

# Close the driver
driver.quit()
