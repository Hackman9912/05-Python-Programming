import pickle
user_choice = 5

def main():
    global user_choice
    output_file = open('name_email.dat', 'wb+')
    end_of_file = False
    while not end_of_file:
        try:
            name_email = pickle.load(output_file)
            first_display(user_choice)
            menu(user_choice, name_email)
            pickle.dump(name_email, output_file)
        except: end_of_file = True
    output_file.close()

def first_display(user_choice):
    user_choice = 1
    print("Choose an option")
    print("Enter 1 to look up an email address, 2 to add a new name and email")
    print("3 to change an existing email and 4 to delete an existing name and email")
    print("press 5 to display all names and emails or press 0 to quit")


def menu(user_choice, name_email):
    user_choice = int(input("Enter choice: "))
    while user_choice > 0 and user_choice < 6:
        if user_choice == 1:
            search = input("Enter the name of the person you want an email for (format is First Last): ")
            if search in name_email:
                print('The email for', search, 'is ', name_email[search])
            else:
                print("The email for", search, "was not found.")
                print("If you would like to add it please choose option 2")
        elif user_choice == 2:
            name_add = input("Enter the First Lastname for the name that needs added: ")
            email_add = input(f"Enter the email for {name_add:}: ")
            name_email[name_add] = email_add
            print("You added: ", name_email[name_add])
        elif user_choice == 3:
            name_edit = input("Enter the name of the person you want to change the email for (format is First Last): ")
            if name_edit in name_email:
                email_edit = inp5ut(f'Enter the email you would like to assign for {name_edit:}: ')
                name_email[name_edit] = email_edit
                print("Here is your update: ", name_email[name_edit])
            else:
                print("The email for", name_edit, "was not found.")
                print("If you would like to add it please choose option 2")
        elif user_choice == 4:
            name_delt = input("Enter the name of the person you want to remove an email for: ")
            if name_delt in name_email:
                del name_email[name_delt]
                print("It is done")
            else:
                print("The email for", name_edit, "was not found.")
        elif user_choice == 5:
            print("Here are all of the names and emails in the record: ")
            print(name_email)
        else:
            print("oops")
            exit()
        user_choice = int(input("Press 0 to quit or make another selection from above: "))

main()

