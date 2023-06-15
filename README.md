<h1>WhatsApp Automation Scripts</h1>

<p>These scripts automate the process of sending messages and images to multiple WhatsApp numbers using Selenium and Python.</p>

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>Selenium library</li>
  <li>pandas library</li>
  <li>pyautogui library</li>
  <li>Chrome web browser</li>
  <li>Chromedriver</li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone the repository or download the files to your local machine.</li>
  <li>Install the required Python libraries using pip:</li>
</ol>

<pre><code>pip install selenium pandas pyautogui
</code></pre>

<ol start="3">
  <li>Download the appropriate Chromedriver version for your Chrome browser from <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">here</a>. Make sure to place the Chromedriver executable in the same directory as the scripts.</li>
</ol>

<h2>Usage</h2>

<h3>AutomatedMessageApp.py</h3>

<ol>
  <li>Create an Excel file named <code>yourexcelfiles.xlsx</code> with a column named "numara" containing the phone numbers you want to send messages to.</li>
  <li>Open <code>message.txt</code> and provide the message content in the following format:</li>
</ol>

<pre><code>message=Your message content here.
image_path=Path/to/your/image.png
</code></pre>

<p>Replace <code>Your message content here</code> with your actual message and <code>Path/to/your/image.png</code> with the path to the image you want to send (optional).</p>

<ol start="3">
  <li>Run the script <code>automatedmessageapp.py</code> using the following command:</li>
</ol>

<pre><code>python automatedmessageapp.py
</code></pre>

<ol start="4">
  <li>Follow the instructions in the terminal to open WhatsApp Web and press ENTER to start sending messages.</li>
  <li>The script will iterate through the phone numbers, send the message, and update the Excel file with the processing status and time.</li>
</ol>

<h3>NumberCheckApp.py</h3>

<ol>
  <li>Create an Excel file named <code>yourexcelfiles.xlsx</code> with a column named "numara" containing the phone numbers you want to check on WhatsApp.</li>
  <li>Run the script <code>numbercheckapp.py</code> using the following command:</li>
</ol>

<pre><code>python numbercheckapp.py
</code></pre>

<ol start="3">
  <li>Follow the instructions in the terminal to open WhatsApp Web and press ENTER to start checking numbers.</li>
  <li>The script will iterate through the phone numbers, check if they can be used on WhatsApp, and update the Excel file with the processing status and time.</li>
</ol>

<h3>FragmentedMessageApp.py</h3>

<ol>
  <li>Create an Excel file named <code>yourexcelfiles.xlsx</code> with a column named "numara" containing the phone numbers you want to send messages to.</li>
  <li>Modify the message parts (e.g., <code>message_part_1</code>, <code>message_part_2</code>, etc.) and the image path (e.g., <code>image_pathdata</code>) in the script according to your requirements.</li>
  <li>Run the script <code>fragmentedmessageapp.py</code> using the following command:</li>
</ol>

<pre><code>python fragmentedmessageapp.py
</code></pre>

<ol start="4">
  <li>Follow the instructions in the terminal to open WhatsApp Web and press ENTER to start sending fragmented messages.</li>
  <li>The script will iterate through the phone numbers, send the fragmented message, and update the Excel file with the processing status and time.</li>
</ol>

<h2>Notes</h2>

<ul>
  <li>Make sure to have a stable internet connection while running the scripts.</li>
  <li>The scripts are provided as examples and may require modifications based on your specific use case.</li>
</ul>

<p>Feel free to modify and customize the scripts according to your needs. Happy automating!</p>

<p><strong>Note:</strong> Remember to update the README file with any additional instructions or changes specific to your programs.</p>
