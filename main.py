print ("Budget Laptop Calculator")


# trial reading information from an existing csv file locally store
# trial reading a file that gets updated remotely online
# trial using an API with this information  - example Google Map API, chatGPT API
# webscraping using BeautifulSoup library in Python - select a website, store information in a file

type_list = ['gaming', 'programming', 'working', 'editing']
while True:
    type_choice = input("Please choose one of the following options: " + ", ".join(type_list) + '  ')
    if type_choice in type_list:
        print("You chose", type_choice)
        break
    else:
        print("Invalid choice. Please try again.")


ram_list = ['4GB', '8GB', '16GB', '32GB']
while True:
    ram_choice = input("Please choose one of the following options:" + ", ".join(ram_list) + ' ')
    if ram_choice in ram_list:
        print("You chose", ram_choice)
        break
    else:
        print("Invalid choice. Please try again.")

storage_list = ['256GB', '512GB', '1TB']
while True:
    storage_choice = input("Please choose one of the following options:" + ", ".join(storage_list) + ' ')
    if storage_choice in storage_list:
        print("You chose", storage_choice)
        break
    else:
        print("Invalid choice. Please try again.")

