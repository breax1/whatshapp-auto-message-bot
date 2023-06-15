WhatsApp Automation Scripts
These scripts automate the process of sending messages and images to multiple WhatsApp numbers using Selenium and Python.

Requirements
Python 3.x
Selenium library
pandas library
pyautogui library
Chrome web browser
Chromedriver
Installation
Clone the repository or download the files to your local machine.
Install the required Python libraries using pip:
Copy code
pip install selenium pandas pyautogui
Download the appropriate Chromedriver version for your Chrome browser from here. Make sure to place the Chromedriver executable in the same directory as the scripts.
Usage
AutomatedMessageApp.py
Create an Excel file named yourexcelfiles.xlsx with a column named "numara" containing the phone numbers you want to send messages to.
Open message.txt and provide the message content in the following format:
css
Copy code
message=Your message content here.
image_path=Path/to/your/image.png
Replace Your message content here with your actual message and Path/to/your/image.png with the path to the image you want to send (optional).
Run the script automatedmessageapp.py using the following command:
Copy code
python automatedmessageapp.py
Follow the instructions in the terminal to open WhatsApp Web and press ENTER to start sending messages.
The script will iterate through the phone numbers, send the message, and update the Excel file with the processing status and time.
NumberCheckApp.py
Create an Excel file named yourexcelfiles.xlsx with a column named "numara" containing the phone numbers you want to check on WhatsApp.
Run the script numbercheckapp.py using the following command:
Copy code
python numbercheckapp.py
Follow the instructions in the terminal to open WhatsApp Web and press ENTER to start checking numbers.
The script will iterate through the phone numbers, check if they can be used on WhatsApp, and update the Excel file with the processing status and time.
FragmentedMessageApp.py
Create an Excel file named yourexcelfiles.xlsx with a column named "numara" containing the phone numbers you want to send messages to.
Modify the message parts (e.g., message_part_1, message_part_2, etc.) and the image path (e.g., image_pathdata) in the script according to your requirements.
Run the script fragmentedmessageapp.py using the following command:
Copy code
python fragmentedmessageapp.py
Follow the instructions in the terminal to open WhatsApp Web and press ENTER to start sending fragmented messages.
The script will iterate through the phone numbers, send the fragmented message, and update the Excel file with the processing status and time.
Notes
Make sure to have a stable internet connection while running the scripts.
The scripts are provided as examples and may require modifications based on your specific use case.
Feel free to modify and customize the scripts according to your needs. Happy automating!

Note: Remember to update the README file with any additional instructions or changes specific to your programs.
