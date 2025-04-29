from src.contactBook import ContactBook
from src.contact import Contact

cb = ContactBook()


# Test for adding a contact
def test_add_contact():
    contact = Contact("John Doe", "1234567890", "johndoe@gmail.com", "0")
    cb.addContact(contact)


# Test for deleting a contact
def test_delete_contact():
    print(cb.deleteContact("0"))
    assert cb.deleteContact("0") == "Contact not found"


# Test for viewing all contacts
def test_view_contacs():
    assert cb.viewContacts() == {}


# Test for viewing a contact
def test_view_contact():
    assert cb.viewContact("John Doe") == "Contact not found"
