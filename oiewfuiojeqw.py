from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


print("Budget Laptop Calculator")

print("Enter Below the Specifications You Require")
print("  ")

# This section of code just prints out some text to the console
# welcoming the user to the budget laptop calculator and asking them to input their desired specifications.

# trial reading information from an existing csv file locally store
# trial reading a file that gets updated remotely online
# trial using an API with this information  - example Google Map API, chatGPT API
# webscraping using BeautifulSoup library in Python - select a website, store information in a file


def get_choice(prompt, options):
    while True:
        choice = input(prompt + " " + ", ".join(options) + " ")
        if choice in options:
            print("You chose", choice)
            return choice
        else:
            print("Invalid choice. Please try again.")


# This is a function that takes a prompt and a list of options as inputs, and returns the user's choice from the list.
# It loops until the user inputs a valid option,
# and prints a message indicating their choice or notifying them of an invalid choice.


memory_list = ["8GB", "16GB", "32GB", "64GB"]
memory_choice = get_choice(
    "Please choose one of the following memory options:", memory_list
)

screen_list = ["10", "12", "14", "16", "18"]
screen_choice = get_choice(
#     "Please choose one of the following screen size options (inches):", screen_list
# )

# SSD_list = ["32GB", "64GB", "256GB", "512GB", "1TB"]
# SSD_choice = get_choice(
#     "Please choose one of the following SSD storage options:", SSD_list
# )

# system_list = ["windows", "macOS"]
# system_choice = get_choice(
#     "Please choose one of the operating system following options:", system_list
# )

# memory_choice = "8GB"
screen_choice = "14"
SSD_choice = "256GB"
system_choice = "macOS"


# This section of code uses the get_choice() function to prompt the user to choose from lists of options
# for the type of laptop they want (e.g. gaming, programming),
# the amount of RAM they want, the amount of storage they want, and the operating system they want.
# It stores each choice in a separate variable for later use.


# create a new Chrome browser instance
driver = webdriver.Chrome()

# navigate to Google
driver.get("https://www.pbtech.co.nz/category/computers/laptops/shop-all")

driver.maximize_window()
# find the element by its id

filters = driver.find_element(By.CLASS_NAME, "maxFilters")
filters.click()

# Select operating system

if system_choice == "macOS":
    dropdown = driver.find_elements(By.CLASS_NAME, "ui-dropdownchecklist-selector")
    dropdown[4].click()

    mac_checkbox = driver.find_element(By.ID, "ddcl-filter_22[]-i2")
    mac_checkbox.click()
else:
    dropdown = driver.find_elements(By.CLASS_NAME, "ui-dropdownchecklist-selector")
    dropdown[4].click()

    windows_checkbox = driver.find_element(
        By.CSS_SELECTOR, 'input[id*="ddcl-filter_22"][value="2391"]'
    )
    windows_checkbox.click()

## Select ram
slider = driver.find_element(By.ID, "sf51")

# Figures out how many times left/right arrow key will need to be pressed
# Converts chosen memory into integer
memory_size = int(memory_choice[:-2])
memory_options = [4, 8, 12, 16, 20, 24, 32, 40, 64]
timesToPressRightArrowKey = memory_options.index(memory_size)
timesToPressLeftArrowKey = 8 - memory_options.index(memory_size)

# Slecting lowerbound
minhandle = slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]

# Click on the slider handle to activate it
ActionChains(driver).click(minhandle).perform()

# Press the right arrow key 5 times
for i in range(timesToPressRightArrowKey):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()

# Selecting upperbound
maxhandle = slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]

# Click on the slider handle to activate it
ActionChains(driver).click(maxhandle).perform()

# Press the right arrow key 5 times
for i in range(timesToPressLeftArrowKey):
    ActionChains(driver).send_keys(Keys.LEFT).perform()


# keep the browser window open
input("Press enter to close the browser...")

