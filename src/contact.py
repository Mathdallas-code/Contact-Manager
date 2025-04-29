class Contact:
    """
    Represents a contact with basic information.

    Attributes:
        name (str): The name of the contact.
        contact (str): The phone number or other contact information.
        email (str): The email address of the contact.
        id (int): A unique identifier for the contact.

    Args:
        name (str): The name of the contact.
        contact (str): The phone number or other contact information.
        email (str): The email address of the contact.
        id (int): A unique identifier for the contact.
    """

    def __init__(self, name: str, contact: str, email: str, id: int):
        self.name = name
        self.contact = contact
        self.email = email
        self.id = id
