# Importing all modules
from src.contact import Contact as cnt
from src.contactBook import ContactBook
from utils.utils import is_valid_phone_number as verify_contact
from utils.save_file import save_file

# Defining contact manager
cb = ContactBook()
# Border for seperating commands
border = '-------------------------------------------------'
with open('data/id.txt', "r") as f:
    id = int(f.read())

print("Welcome to the contact manager!")

# Loop
while True:
    print(border)
    # Asking user input
    user_input = input(
        'Choose a command - \n\t\
    1 - View the existing contacts\n\t\
    2 - Search a contact\n\t\
    3 - Add a contact\n\t\
    4 - Delete a contact\n\t\
    5 - Exit the program\n\n\
        > '
    )

    if user_input == '1':
        # Print the contacts
        contacts = cb.viewContacts()
        if contacts == {}:
            print(border)
            print('No contacts found!')
        else:
            for i in contacts:
                print(border)
                print(f'Id: {i}')
                print(f'Name: {contacts[i]["name"]}')
                print(f'Contact: {contacts[i]["contact"]}')
                print(f'Em@il: {contacts[i]["email"]}')
    elif user_input == '2':
        # Searches the contacts and returns it
        contact_name = input("Enter contact name: ")
        contact = cb.viewContact(contactName=contact_name)
        if contact == "Contact not found":
            print("Contact not found!")
        else:
            print(border)
            print(f'Name: {contact["name"]}')
            print(f'Contact: {contact["contact"]}')
            print(f'Em@il: {contact["email"]}')
    elif user_input == '3':
        # Adds a contact
        id += 1
        save_file('data/id.txt', str(id))
        print(border)
        name = input("Enter contact name: ")

        while True:
            contact_num = input("Enter contact number: ")
            if verify_contact(contact_num):
                break
            else:
                print(f"Invalid contact number! Please try again. ({contact_num})")
        email = input("Enter contact em@il: ")
        contact = cnt(name=name, contact=contact_num, email=email, id=id)
        print(cb.addContact(contact=contact))
        with open("data/id.txt", "w") as f:
            f.write(str(id))
            f.close()
    elif user_input == '4':
        # Deletes a contact
        print(border)
        change_id = input("Enter id of contact to be deleted: ")
        print(change_id)
        cb.deleteContact(change_id)
        print("Contact deleted!")
    elif user_input == '5':
        # Quits
        print(border)
        print("Bye!")
        quit()
