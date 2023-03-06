def get_choice(prompt, options):
    while True:
        choice = input(prompt + " " + ", ".join(options) + " ")
        if choice in options:
            print("You chose", choice)
            return choice
        else:
            print("Invalid choice. Please try again.")

type_list = ['gaming', 'programming', 'working', 'editing']
type_choice = get_choice("Please choose one of the following options:", type_list)

ram_list = ['4GB', '8GB', '16GB', '32GB']
ram_choice = get_choice("Please choose one of the following options:", ram_list)

storage_list = ['256GB', '512GB', '1TB']
storage_choice = get_choice("Please choose one of the following options:", storage_list)

system_list = ['windows', 'macOS']
system_choice = get_choice("Please choose one of the following options:", system_list)