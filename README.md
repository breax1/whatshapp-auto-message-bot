# whatshapp-auto-message-bot
Whatsapp Auto Message Bot is an automated messaging on WhatsApp. With features like bulk messages, it simplifies communication and saves time.

WhatsApp Bot for Sending Bulk Automated Messages using Excel Data

This project is a WhatsApp bot designed to send bulk automated messages to contacts using data extracted from an Excel file. It utilizes the WhatsApp API and Python programming language to automate the process of sending messages.

Prerequisites
Python 3.6 or higher
Selenium library
ChromeDriver
Setup
Clone this repository to your local machine.

Install the required Python packages using the following command:
pip install selenium

Download the appropriate ChromeDriver version for your Chrome browser from the official ChromeDriver website (https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to place the ChromeDriver executable in the same directory as the bot script.

Prepare your Excel data file with the phone numbers and corresponding messages. The file should be in .xlsx format, with the phone numbers in one column and the messages in another.

Update the config.py file with your WhatsApp account credentials and the path to your Excel data file.

Run the bot script using the following command:
python whatsapp_bot.py

The bot will launch a Chrome browser and prompt you to scan the QR code with your WhatsApp account. Once authenticated, it will start sending automated messages to the contacts listed in the Excel file.

Sit back and let the bot do the work! It will automatically send messages one by one to the specified contacts.

Important Note
Please ensure that you use this bot responsibly and in compliance with WhatsApp's terms of service. Misuse or spamming can lead to your account being banned by WhatsApp.
