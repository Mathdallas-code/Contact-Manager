from src.contact import Contact as cnt
from src.contactBook import ContactBook
from utils.utils import is_valid_phone_number as verify_contact
from utils.save_file import save_file

cb = ContactBook()
border = '-------------------------------------------------'
with open('data/id.txt', "r") as f:
    id = int(f.read())

print("Welcome to the contact manager!")
while True:
    print(border)
    user_input = input(
        'Choose a command - \n\t1 - View the existing contacts\n\t2 - Add a contact\n\t3 - Delete a contact\n\t4 - Exit the program\n\nEnter your command: '
    )
    if user_input == '1':
        # Print the contacks
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
        cb.addContact(contact=contact)
    elif user_input == '3':
        print(border)
        change_id = input("Enter id of contact to be deleted: ")
        print(change_id)
        cb.deleteContact(change_id)
        print("Contact deleted!")
    elif user_input == '4':
        print(border)
        print("Bye!")
        quit(0)
