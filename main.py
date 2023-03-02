print ("Budget Laptop Calculator")

type_list = ['gaming', 'programming', 'working', 'editing']
while True:
    user_choice = input("Please choose one of the following options: " + ", ".join(type_list) + '  ')
    if user_choice in type_list:
        break
    else:
        print("Invalid choice. Please try again.")

print("You chose", user_choice)

ram_list = ['4GB', '8GB', '16GB', '32GB']
while true:
