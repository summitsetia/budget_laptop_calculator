from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

sleep = 3
remove_unit = -2

print("Laptop Calculator")
print("Enter Below the Specifications You Require")
print("  ")

# This section of code just prints out some text to the console
# welcoming the user to the laptop calculator and asking them to input their desired specifications.
# trial reading information from an existing csv file locally store
# trial reading a file that gets updated remotely online
# trial using an API with this information  - example Google Map API, chatGPT API
# webscraping using BeautifulSoup library in Python - select a website, store information in a file
# add .upper() make it lowercase


def get_choice(prompt, options):
    while True:
        choice = input(prompt + " " + ", ".join(options) + " ").upper()
        if choice in options:
            print("You chose", choice)
            return choice
        else:
            print("Invalid choice. Please try again.")

# This is a function that takes a prompt and a list of options as inputs, and returns the user's choice from the list.
# It loops until the user inputs a valid option,
# and prints a message indicating their choice or notifying them of an invalid choice.


memory_list = ["8GB", "16GB", "32GB", "64GB"]
memory_min_choice = get_choice(
    "Please choose the minimum value for one of the following memory options:", memory_list
)
memory_max_choice = get_choice(
    "Please choose the maximum value from one of the following memory options:", memory_list
)

screen_list = ["10", "12", "14", "16", "18"]
screen_min_choice = get_choice(
    "Please choose the minimum value for one of the following screen size options (inches):", screen_list
)
screen_max_choice = get_choice(
    "Please choose the maximum value for one of the following screen size options (inches):", screen_list
)


SSD_list = ["32GB", "64GB", "256GB", "512GB", "1000GB"]
SSD_min_choice = get_choice(
    "Please choose the minimum value for one of the following SSD storage options:", SSD_list
)
SSD_max_choice = get_choice(
    "Please choose the maximum value one of the following SSD storage options:", SSD_list
)

system_list = ["WINDOWS", "MACOS"]
system_choice = get_choice(
    "Please choose one of the operating system following options:", system_list
)

print("now directing you to PB Technology...")

# This section of code uses the get_choice() function to prompt the user to choose from lists of options
# for the type of laptop they want (e.g. gaming, programming),
# the amount of RAM they want, the amount of storage they want, and the operating system they want.
# It stores each choice in a separate variable for later use.


# create a new Chrome browser instance
driver = webdriver.Chrome()

# navigate to Google
website = "https://www.pbtech.co.nz/category/computers/laptops/shop-all"
driver.get(website)

driver.maximize_window()
# find the element by its id

# Find the "maxFilters" element and click on it to show the filter dropdown
filters = driver.find_element(By.CLASS_NAME, "maxFilters")
filters.click()

# Check the system choice and select the corresponding OS from the dropdown
if system_choice == "MACOS":
    dropdown = driver.find_elements(By.CLASS_NAME, "ui-dropdownchecklist-selector")
    dropdown[4].click()

    # Find and click the checkbox for macOS
    mac_checkbox = driver.find_element(By.ID, "ddcl-filter_22[]-i2")
    mac_checkbox.click()
else:
    # For non-macOS systems, click on the OS dropdown and select the "Windows" option
    dropdown = driver.find_elements(By.CLASS_NAME, "ui-dropdownchecklist-selector")
    dropdown[4].click()

    # Find and click the checkboxes for each Windows version in the "windowsIds" list
    windowsIds = ["2391", "421", "190", "477", "819", "7546", "2012", "7546", "3645", "3186", "3278", "4246", "7544",
                  "7548", "7545", "7737"]
    for windows in windowsIds:
        windows_checkbox = driver.find_element(By.CSS_SELECTOR, f'input[id*="ddcl-filter_22"][value="{windows}"]')
        windows_checkbox.click()

# This code section is used to adjust the RAM slider on the webpage
# Find the RAM slider on the webpage by its ID
memory_slider = driver.find_element(By.ID, "sf51")

# Convert the memory choice string to an integer (removing "GB" from the end of the string)
memory_size_min = int(memory_min_choice[:remove_unit])
memory_size_max = int(memory_max_choice[:remove_unit])

# Define a list of available memory options (in GB)
memory_options = [4, 8, 12, 16, 20, 24, 32, 40, 64]

# Determine how many times to press the right arrow key to reach the desired memory size
timesToPressRightArrowKey_memory = memory_options.index(memory_size_min)

# Determine how many times to press the left arrow key to set the maximum memory size to 64 G
timesToPressLeftArrowKey_memory = 8 - memory_options.index(memory_size_max)

# Find the minimum handle of the RAM slider
minhandle_memory = memory_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]
# Click on the minimum handle to activate it
ActionChains(driver).click(minhandle_memory).perform()

# Use a loop to press the right arrow key the appropriate number of times to set the desired memory size
for i in range(timesToPressRightArrowKey_memory):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()

    # Find the maximum handle of the RAM slider
maxhandle_memory = memory_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]

# Click on the maximum handle to activate it
ActionChains(driver).click(maxhandle_memory).perform()

# Use a loop to press the left arrow key the appropriate number of times to set the maximum memory size to 64 GB
for i in range(timesToPressLeftArrowKey_memory):
    ActionChains(driver).send_keys(Keys.LEFT).perform()

# This line finds an HTML element on a webpage using its ID attribute and assigns it to the SSD_slider variable
SSD_slider = driver.find_element(By.ID, "sf57")

# this line converts the last two characters of a string  to an integer and assigns it to the SSD_size variable
SSD_size_min = int(SSD_min_choice[:remove_unit])
SSD_size_max = int(SSD_max_choice[:remove_unit])

# This is a list of SSD storage capacity options in GB
SSD_options = [
    32,
    64,
    128,
    192,
    250,
    256,
    300,
    500,
    512,
    750,
    1000,
    1024,
    1200,
    1500,
    2000,
    2500,
    4000,
]
# This line finds the index of the SSD size option in the SSD_options list and assigns the result to variable
timesToPressRightArrowKey_SSD = SSD_options.index(SSD_size_min)

# This line calculates the number of times the left arrow key should be pressed to reach the SSD size option
timesToPressLeftArrowKey_SSD = 16 - SSD_options.index(SSD_size_max)

# This line finds the first slider handle element within the_slider element and assigns it to the minhandle_SSD variable
minhandle_SSD = SSD_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]

# This line clicks on the minhandle_SSD_memory element using the ActionChains class from the Selenium library
ActionChains(driver).click(minhandle_SSD).perform()

# This loop presses the right arrow key on keyboard timesToPressRightArrowKey_SSD number of times using ActionChains
for i in range(timesToPressRightArrowKey_SSD):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()

# This line finds the second slider handle element within SSD_slider element and assigns it to the maxhandle_SSD
maxhandle_SSD = SSD_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]
# This line clicks on the maxhandle_SSD element using the ActionChains class
ActionChains(driver).click(maxhandle_SSD).perform()
# This loop presses the left arrow key on keyboard timeToPressLeftArrowKey_SSD amount of times using actionchain class
for i in range(timesToPressLeftArrowKey_SSD):
    ActionChains(driver).send_keys(Keys.LEFT).perform()

# This code uses Selenium WebDriver to interact with a web page slider element, specifically a screen size slider.
# The first line finds the slider element using its ID and assigns it to the screen_slider variable.
screen_slider = driver.find_element(By.ID, "sf211")

# The next two lines extract the min and max screen sizes from the user's input,stored in the screen_choice variable.
min_screen_size = int(screen_min_choice)
max_screen_size = int(screen_max_choice)

# The screen_options list contains all the available screen size options in inches.
# The index of the minimum and maximum screen sizes in this list is calculated to determine how many arrow key presses
# are required to set the slider to the desired range.
screen_options = [
    10,
    10.1,
    11.6,
    12,
    12.3,
    12.4,
    12.5,
    13,
    13.3,
    13.4,
    13.5,
    13.6,
    13.9,
    14,
    14.1,
    14.4,
    15,
    15.1,
    15.6,
    16,
    16.1,
    17,
    17.3,
    18,
]
# The next block of code locates the slider handles and uses the ActionChains class from Selenium to perform a series
# of arrow key presses to set the slider to the desired range.
timesToPressRightArrowKey_size = screen_options.index(min_screen_size)
timesToPressLeftArrowKey_size = 23 - screen_options.index(max_screen_size)
minhandle_size = screen_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]
ActionChains(driver).click(minhandle_size).perform()
for i in range(timesToPressRightArrowKey_size):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
maxhandle_size = screen_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]
# This code uses the ActionChains class from the Selenium WebDriver library to perform some actions on a web page.
ActionChains(driver).click(maxhandle_size).perform()

#  This code creates a loop that will run a number of times, as specified by the variable "timesToPressLeftArrowKeys".
for i in range(timesToPressLeftArrowKey_size):
    ActionChains(driver).send_keys(Keys.LEFT).perform()

# This code finds a web element using Selenium WebDriver and clicks on it.
apply_filter = driver.find_element(
    By.XPATH, "//button[@class='orange xsmall py-2 py-md-1 right']"
)
# The next line of code clicks on the button using the click() method of the WebElement object.
apply_filter.click()
# After clicking the button, the code waits for 3 seconds using the time.sleep() function.
time.sleep(sleep)
page_source = driver.page_source


# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the laptops that match the user's specifications
results = soup.find(id='main_container')
laptops = results.find_all('h2', class_='np_title')

# Print the laptop names
for laptop in laptops:
    print(laptop.text)

input("Press enter to close the browser...")
driver.quit()

