from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

print("Budget Laptop Calculator")

print("Enter Below the Specifications You Require")
print('  ')

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


memory_list = ['8GB', '16GB', '32GB', '64GB']
memory_choice = get_choice("Please choose one of the following memory options:", memory_list)

screen_list = ['10', '12', '14', '16', '18']
screen_choice = get_choice("Please choose one of the following screen size options (inches):", screen_list)

SSD_list = ['32GB', '64GB', '256GB', '512GB', '1000GB']
SSD_choice = get_choice("Please choose one of the following SSD storage options:", SSD_list)

system_list = ['windows', 'macOS']
system_choice = get_choice("Please choose one of the operating system following options:", system_list)


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

if system_choice == 'macOS':
    dropdown = driver.find_elements(By.CLASS_NAME, "ui-dropdownchecklist-selector")
    dropdown[4].click()

    mac_checkbox = driver.find_element(By.ID, "ddcl-filter_22[]-i2")
    mac_checkbox.click()
else:
    dropdown = driver.find_elements(By.CLASS_NAME, "ui-dropdownchecklist-selector")
    dropdown[4].click()

    windows_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[id*="ddcl-filter_22"][value="2391"]')
    windows_checkbox.click()



ram_slider = driver.find_element(By.ID, "sf51")
memory_size = int(memory_choice[:-2])
memory_options = [4, 8, 12, 16, 20, 24, 32, 40, 64]
timesToPressRightArrowKey = memory_options.index(memory_size)
timesToPressLeftArrowKey = 8 - memory_options.index(memory_size)
minhandle = ram_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]
ActionChains(driver).click(minhandle).perform()
for i in range(timesToPressRightArrowKey):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
maxhandle = ram_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]
ActionChains(driver).click(maxhandle).perform()
for i in range(timesToPressLeftArrowKey):
    ActionChains(driver).send_keys(Keys.LEFT).perform()


SSD_slider = driver.find_element(By.ID, "sf57")
SSD_size = int(SSD_choice[:-2])
SSD_options = [32, 64, 128, 192, 250, 256, 300, 500, 512, 750, 1000, 1024, 1200, 1500, 2000, 2500, 4000]
timesToPressRightArrowKeym = SSD_options.index(SSD_size)
timesToPressLeftArrowKeym = 16 - SSD_options.index(SSD_size)
minhandlem = SSD_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]
ActionChains(driver).click(minhandlem).perform()
for i in range(timesToPressRightArrowKeym):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
maxhandlem = SSD_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]
ActionChains(driver).click(maxhandlem).perform()
for i in range(timesToPressLeftArrowKeym):
    ActionChains(driver).send_keys(Keys.LEFT).perform()

screen_slider = driver.find_element(By.ID, "sf211")
screen_size = int(screen_choice)
screen_options = [10, 10.1, 11.6, 12, 12.3, 12.4, 12.5, 13, 13.3, 13.4, 13.5, 13.6, 13.9, 14, 14.1, 14.4, 15, 15.1, 15.6, 16, 16.1, 17, 17.3, 18]
timesToPressRightArrowKeys = screen_options.index(screen_size)
timesToPressLeftArrowKeys = 23 - screen_options.index(screen_size)
minhandles = screen_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[0]
ActionChains(driver).click(minhandles).perform()
for i in range(timesToPressRightArrowKeys):
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
maxhandles = screen_slider.find_elements(By.CLASS_NAME, "ui-slider-handle")[1]
ActionChains(driver).click(maxhandles).perform()
for i in range(timesToPressLeftArrowKeys):
    ActionChains(driver).send_keys(Keys.LEFT).perform()

input("Press enter to close the browser...")
driver.quit()
