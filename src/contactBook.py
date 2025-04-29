from .contact import Contact as cnt
import json

contactsPath = 'data/contacts.json'
idPath = 'data/id.txt'

with open(contactsPath, "r") as f:
    contactsJson = json.load(f)

with open(idPath, "r") as f:
    id = f.read()


class ContactBook:
    def __init__(self):
        self.contacts = contactsJson

    def addContact(self, contact: cnt):
        self.contacts[contact.id] = {
            "name": contact.name,
            "contact": contact.contact,
            "email": contact.email,
        }

        with open(contactsPath, "w") as f:
            json.dump(self.contacts, f, indent=4)
            f.close()

    def deleteContact(self, id: str):
        with open(contactsPath, "w") as f:
            json.dump(self.contacts, f)
            f.close()
        del self.contacts[id]
        with open(contactsPath, "w") as f:
            json.dump(self.contacts, f)
            f.close()

    def viewContacts(self):
        f = open(contactsPath, "r")
        entries = json.load(f)
        return entries
