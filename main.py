print("Budget Laptop Calculator")

print("Enter Below the Specifications You Require")
print('  ')
#This section of code just prints out some text to the console
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

#This is a function that takes a prompt and a list of options as inputs, and returns the user's choice from the list.
# It loops until the user inputs a valid option, and prints a message indicating their choice or notifying them of an invalid choice.

type_list = ['gaming', 'programming', 'working', 'editing']
type_choice = get_choice("Please choose one of the following options:", type_list)

ram_list = ['4GB', '8GB', '16GB', '32GB']
ram_choice = get_choice("Please choose one of the following options:", ram_list)

storage_list = ['256GB', '512GB', '1TB']
storage_choice = get_choice("Please choose one of the following options:", storage_list)

system_list = ['windows', 'macOS']
system_choice = get_choice("Please choose one of the following options:", system_list)
#This section of code uses the get_choice() function to prompt the user to choose from lists of options
# for the type of laptop they want (e.g. gaming, programming),
# the amount of RAM they want, the amount of storage they want, and the operating system they want.
# It stores each choice in a separate variable for later use.

from selenium import webdriver

# create a new Chrome browser instance
driver = webdriver.Chrome()

# navigate to Google
driver.get("https://www.pbtech.co.nz/")

# keep the browser window open
input("Press enter to close the browser...")
driver.quit()