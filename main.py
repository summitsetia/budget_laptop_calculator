print ("Budget Laptop Calculator")

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

