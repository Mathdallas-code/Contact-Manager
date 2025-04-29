# Modules
from .contact import Contact as cnt
import json

# Paths to the data files
contactsPath = 'data/contacts.json'
idPath = 'data/id.txt'

with open(contactsPath, "r") as f:
    contactsJson = json.load(f)

with open(idPath, "r") as f:
    id = f.read()


# Main class for functions
class ContactBook:
    def __init__(self):
        self.contacts = contactsJson

    # Add a contact
    def addContact(self, contact: cnt):
        if contact.id in self.contacts:
            return "Contact already exists"
        else:
            self.contacts[contact.id] = {
                "name": contact.name,
                "contact": contact.contact,
                "email": contact.email,
            }
            with open(contactsPath, "w") as f:
                json.dump(self.contacts, f, indent=4)
                f.close()
            return "Contact Added"

    # Deletes a contact
    def deleteContact(self, id: str):
        if id in self.contacts:
            del self.contacts[id]
            with open(contactsPath, "w") as f:
                json.dump(self.contacts, f)
                f.close()
            return "Contact deleted"
        else:
            return "Contact not found"

    # Shows all contacts
    def viewContacts(self):
        f = open(contactsPath, "r")
        entries = json.load(f)
        return entries

    # Searches for a contact
    def viewContact(self, contactName: int):
        f = open(contactsPath, "r")
        entries = json.load(f)
        for entry in entries:
            if entries[entry]["name"] == contactName:
                return entries[entry]

        return "Contact not found"
