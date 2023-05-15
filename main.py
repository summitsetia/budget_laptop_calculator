from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# Set sleep_time and unit_length constants for use throughout the script
sleep_time = 3
unit_length = -2

# Welcome the user and prompt them to input their laptop specifications
print("Laptop Calculator")
print("Enter Below the Specifications You Require")
print("  ")


# This is a function that takes a prompt and a list of options as inputs, and returns the user's choice from the list.
# It loops until the user inputs a valid option,
# and prints a message indicating their choice or notifying them of an invalid choice.
def get_choice(prompt, options):
    while True:
        choice = input(prompt + " " + ", ".join(options) + " ").upper()
        if choice in options:
            print("You chose", choice)
            return choice
        else:
            print("Invalid choice. Please try again.")


# Ask the user to choose the minimum and maximum memory values from the memory_options list
memory_list = ["8GB", "16GB", "32GB", "64GB"]
while True:
    min_memory_choice = get_choice("Please choose the minimum value for one of the following memory options:",
                                   memory_list)
    max_memory_choice = get_choice("Please choose the maximum value from one of the following memory options:",
                                   memory_list)

    # Convert the choices to integers and ensure they are valid (minimum value is less than or equal to maximum value)
    memory_size_min = int(min_memory_choice[:unit_length])
    memory_size_max = int(max_memory_choice[:unit_length])

    if memory_size_min <= memory_size_max:
        break
    print("Invalid choice. The minimum value cannot be greater than the maximum value. Please try again.")

# Ask the user to choose the minimum and maximum screen size values from the screen_options list
screen_list = ["10", "12", "14", "16", "18"]
while True:
    screen_min_choice = get_choice("Please choose the minimum value for one of the following screen size options "
                                   "(inches):", screen_list)
    screen_max_choice = get_choice("Please choose the maximum value for one of the following screen size options"
                                   " (inches):", screen_list)

    # Convert the choices to integers and ensure they are valid (minimum value is less than or equal to maximum value)
    screen_size_min = int(screen_min_choice)
    screen_size_max = int(screen_max_choice)

    if screen_size_min <= screen_size_max:
        break
    print("Invalid choice. The minimum value cannot be greater than the maximum value. Please try again.")

# Ask the user to choose the minimum and maximum SSD values from the ssd_options list
ssd_list = ["32GB", "64GB", "256GB", "512GB", "1000GB"]
while True:
    ssd_min_choice = get_choice("Please choose the minimum value for one of the following SSD storage options:",
                                ssd_list)
    ssd_max_choice = get_choice("Please choose the maximum value one of the following SSD storage options:",
                                ssd_list)

    # Convert the choices to integers and ensure they are valid (minimum value is less than or equal to maximum value)
    ssd_size_min = int(ssd_min_choice[:unit_length])
    ssd_size_max = int(ssd_max_choice[:unit_length])

    if ssd_size_min <= ssd_size_max:
        break
    print("Invalid choice. The minimum value cannot be greater than the maximum value. Please try again.")

# Ask the user to choose an operating system from the system_options list
system_list = ["WINDOWS", "MACOS"]
system_choice = get_choice("Please choose one of the operating system following options:",
                           system_list)

print("now directing you to PB Technology...")

# Open a new Chrome browser instance and navigate to the PB Technology website
driver = webdriver.Chrome()
website = "https://www.pbtech.co.nz/category/computers/laptops/shop-all"
driver.get(website)
driver.maximize_window()

# Find the "maxFilters" element and click on it to show the filter dropdown
filters = driver.find_element(By.CLASS_NAME, "maxFilters")
filters.click()

# Check the system_choice and select the corresponding OS from the dropdown
if system_choice == "MACOS":
    dropdown = driver.find_elements(By.CLASS_NAME, "ui-dropdownchecklist-selector")
    dropdown[4].click()

    # Find and click the checkbox for macOS in the OS filter dropdown
    mac_checkbox_element = driver.find_element(By.ID, "ddcl-filter_22[]-i2")
    mac_checkbox_element.click()
else:
    # For non-macOS systems, click on the OS dropdown and select the "Windows" option
    dropdown = driver.find_elements(By.CLASS_NAME, "ui-dropdownchecklist-selector")
    dropdown[4].click()

    # Find and click the checkboxes for each Windows version in the "windowsIds" list
    windows_ids = ["2391", "421", "190", "477", "819", "7546", "2012", "7546", "3645", "3186", "3278", "4246", "7544",
                   "7548", "7545", "7737"]
    for windows in windows_ids:
        windows_checkbox = driver.find_element(By.CSS_SELECTOR, f'input[id*="ddcl-filter_22"][value="{windows}"]')
        windows_checkbox.click()

# This code section is used to adjust the RAM slider on the webpage
# Find the RAM slider on the webpage by its ID
memory_slider = driver.find_element(By.ID, "sf51")
# Convert the memory choice string to an integer (removing "GB" from the end of the string)
# Define a list of available memory options (in GB)
memory_size_options = [4, 8, 12, 16, 20, 24, 32, 40, 64]
memory_options_count = len(memory_size_options)
# Determine how many times to press the right arrow key to reach the desired memory size based of user input
right_arrow_memory = memory_size_options.index(memory_size_min)
# Determine how many times to press the left arrow key to reach the desired memory size based of user input
left_arrow_memory = memory_options_count - memory_size_options.index(memory_size_max) - 1
# Find the minimum handle of the RAM slider
min_handle_memory = memory_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]
# Click on the minimum handle to activate it
ActionChains(driver).click(min_handle_memory).perform()
# Use a loop to press the right arrow key the appropriate number of times to set the desired memory size
for i in range(right_arrow_memory):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
# Find the maximum handle of the RAM slider
max_handle_memory = memory_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]
# Click on the maximum handle to activate it
ActionChains(driver).click(max_handle_memory).perform()
# Use a loop to press the left arrow key the appropriate number of times to set the maximum memory size to 64 GB
for i in range(left_arrow_memory):
    ActionChains(driver).send_keys(Keys.LEFT).perform()

# This line finds an HTML element on a webpage using its ID attribute and assigns it to the SSD_slider variable
ssd_slider = driver.find_element(By.ID, "sf57")
# This is a list of SSD storage capacity options in GB
ssd_size_options = [32, 64, 128, 192, 250, 256, 300, 500, 512, 750, 1000, 1024, 1200, 1500, 2000, 2500, 4000]
ssd_options_count = len(ssd_size_options)
# This line finds the index of the SSD size option in the SSD_options list and assigns the result to variable
right_arrow_ssd = ssd_size_options.index(ssd_size_min)
# This line calculates the number of times the left arrow key should be pressed to reach the SSD size option
left_arrow_ssd = ssd_options_count - ssd_size_options.index(ssd_size_max) - 1
# This line finds the first slider handle element within the_slider element and assigns it to the minhandle_SSD variable
min_handle_ssd = ssd_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]
# This line clicks on the min_handle_ssd_memory element using the ActionChains class from the Selenium library
ActionChains(driver).click(min_handle_ssd).perform()
# This loop presses the right arrow key on keyboard right_arrow_ssd number of times using ActionChains
for i in range(right_arrow_ssd):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
# This line finds the second slider handle element within SSD_slider element and assigns it to the max_handle_ssd
max_handle_ssd = ssd_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]
# This line clicks on the max_handle_ssd element using the ActionChains class
ActionChains(driver).click(max_handle_ssd).perform()
# This loop presses the left arrow key on keyboard timeToPressLeftArrowKey_SSD amount of times using actionchain class
for i in range(left_arrow_memory):
    ActionChains(driver).send_keys(Keys.LEFT).perform()

# This code uses Selenium WebDriver to interact with a web page slider element, specifically a screen size slider.
# The first line finds the slider element using its ID and assigns it to the screen_slider variable.
screen_slider = driver.find_element(By.ID, "sf211")

# The screen_options list contains all the available screen size options in inches.
# The index of the minimum and maximum screen sizes in this list is calculated to determine how many arrow key presses
# are required to set the slider to the desired range.
screen_size_options = [10, 10.1, 11.6, 12, 12.3, 12.4, 12.5, 13, 13.3, 13.4, 13.5, 13.6, 13.9, 14, 14.1, 14.4, 14.5, 15,
                       15.1, 15.6, 16, 16.1, 17, 17.3, 18, 23]
screen_options_count = len(screen_size_options)
# The next block of code locates the slider handles and uses the ActionChains class from Selenium to perform a series
# of arrow key presses to set the slider to the desired range.
right_arrow_screen = screen_size_options.index(screen_size_min)
left_arrow_screen = screen_options_count - screen_size_options.index(screen_size_max) - 1
min_handle_screen = screen_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]
ActionChains(driver).click(min_handle_screen).perform()
for i in range(right_arrow_screen):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
max_handle_screen = screen_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]
# This code uses the ActionChains class from the Selenium WebDriver library to perform some actions on a web page.
ActionChains(driver).click(max_handle_screen).perform()

#  This code creates a loop that will run a number of times, as specified by the variable "timesToPressLeftArrowKeys".
for i in range(left_arrow_screen):
    ActionChains(driver).send_keys(Keys.LEFT).perform()

# This code finds a web element using Selenium WebDriver and clicks on it.
apply_filter = driver.find_element(
    By.XPATH, "//button[@class='orange xsmall py-2 py-md-1 right']"
)
# The next line of code clicks on the button using the click() method of the WebElement object.
apply_filter.click()
# After clicking the button, the code waits for 3 seconds using the time.sleep() function.
time.sleep(sleep_time)
page_source = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the laptops that match the user's specifications
results = soup.find(id='main_container')
laptops = results.find_all('h2', class_='np_title')
prices = results.find_all(class_='price-dollar hide-plain')

print("  ")

# Go through all the laptops and prices on the page and print them
for laptop, price in zip(laptops, prices):
    print(laptop.text, price.text)
    print()

# If the user presses enter the driver will quit
input("Press enter to close the browser...")
driver.quit()
