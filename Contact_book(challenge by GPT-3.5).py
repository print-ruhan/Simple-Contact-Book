import time


#----------------------------------
def contains_alphabet(input_string):
    return bool(list(filter(str.isalpha, input_string)))


def menu():
    print("Welcome to Contact book")
    time.sleep(.3)
    print("Here you can save any contacts!")
    time.sleep(.3)
    print("press 1 if you want to add any contact")
    time.sleep(.3)
    print("press 2 if  you want to view all contact")
    time.sleep(.3)
    print("press 3 if you want to delete any contact")
    time.sleep(.3)
    print("press 4 if you want to exit!")
    time.sleep(.3)


#----------------------------------

def main():
    menu()
    contact = ""
    full_num = ""
    final_email = ""
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            adding(contact, full_num, final_email)
            break
        elif choice == '2':
            view()
            break
        elif choice == '3':
            delete()
            break
        elif choice == '4':
            print("Goodbye!")
            time.sleep(.5)
            break
        else:
            print("Enter a number from 1-4 please ")


#----------------------------------

def adding(contact, final_num, final_email):
    while True:
        time.sleep(.3)
        first_name = input("Enter the first name: ")
        if first_name.isdigit():
            print("The first name can only have letters!")
            time.sleep(.3)
        elif first_name == "":
            time.sleep(.3)
            print("You haven't entered anything!")
            time.sleep(.3)
        else:
            break
    while True:
        last_name = input("Enter the last name: ")
        time.sleep(.3)
        if last_name.isdigit():
            print("The last name can only have letters!")
            time.sleep(.3)
        elif last_name == "":
            print("You haven't entered anything!")
            time.sleep(.3)
        else:
            break
    full_name = first_name + " " + last_name
    contact = full_name
    while True:
        number = input("Enter the personal number of " + full_name + " :(enter 0 to skip) ")
        time.sleep(.3)
        if contains_alphabet(number):
            print("Pls enter numbers!")
            time.sleep(.3)
        elif number == '0':
            number = "NUMBER DIDN'T SAVED"
            break
        elif len(number) != 11:
            print("It should be eleven digits long!")
            time.sleep(.3)
        else:
            break
    final_num = number
    while True:
        email = input("Please enter the " + full_name + "'s email address :(enter 0 to skip) ")
        time.sleep(.3)
        if email == '0':
            email = "DIDN'T SAVED EMAIL"
            break
        elif len(email) == 4 or len(email) < 4:
            print("Your email must contain at least 4 characters! ")
            time.sleep(.3)
        else:
            break
    final_email = email
    save(contact, final_num, final_email)
    while True:
        menu_3 = input("press 1 if you want to go to the menu! or click 2 you want to exit: ")
        time.sleep(.3)
        if menu_3 == '1':
            main()
            break
        elif menu_3 == '2':
            break
        else:
            pass


#----------------------------------


def view():
    try:
        with open('D:\Stuff\PROJECT_OF_RUHAN\Python Projects\Simple Project\saved_contact.txt') as contact:
            print(contact.read())
    except FileNotFoundError:
        print("FILE WAS NOT FOUND :(")
        time.sleep(.3)
    while True:
        menu_2 = input("press 1 if you want to go to the menu! or click 2 you want to exit: ")
        time.sleep(.3)
        if menu_2 == '1':
            main()
            break
        elif menu_2 == '2':
            break
        else:
            pass


#----------------------------------

def delete():
    print("Are you sure you want to delete everything? ")
    time.sleep(.3)
    while True:
        delete_choice = input("Press 1 if you want to delete everything or 2 to go back to main menu: ")
        if delete_choice == '1':
            with open('D:\Stuff\PROJECT_OF_RUHAN\Python Projects\Simple Project\saved_contact.txt', 'w'):
                pass
            print("ALL CONTACT HAVE BEEN DELETED")
            time.sleep(.3)
            break
        elif delete_choice == '2':
            main()
        else:
            pass
    while True:
        print("Do you want to go back to main menu?")
        time.sleep(.3)
        menu_1 = input("press 1 if you want to go back to main menu or press 2 if you want to exit: ")
        if menu_1 == '1':
            main()
            break
        elif menu_1 == '2':
            print('Goodbye!')
            time.sleep(.5)
            break
        else:
            pass


# ----------------------------------
def save(contact, final_num, final_email):
    with open('D:\Stuff\PROJECT_OF_RUHAN\Python Projects\Simple Project\saved_contact.txt', 'a') as file:
        file.write("CONTACT: "+"\n \n")
        file.write("Name :"+contact+"\n \n")
        file.write("Number: "+final_num+"\n \n")
        file.write("Email: "+final_email+"\n \n")
    time.sleep(.3)
    print("Successfully saved contact of "+contact)
    time.sleep(.3)


#----------------------------------

if __name__ == '__main__':
    main()
