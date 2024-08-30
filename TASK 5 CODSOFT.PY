'''TASK 5
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction''''



class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts[name] = Contact(name, phone, email, address)
        print("Contact added successfully!")

    def view_contacts(self):
        for name, contact in self.contacts.items():
            print(f"Name: {name}, Phone: {contact.phone}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        for name, contact in self.contacts.items():
            if search_term in [name, contact.phone]:
                print(f"Name: {name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                return
        print("Contact not found!")

    def update_contact(self):
        name = input("Enter name of contact to update: ")
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            self.contacts[name].phone = phone
            self.contacts[name].email = email
            self.contacts[name].address = address
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        name = input("Enter name of contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

def main():
    manager = ContactManager()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.search_contact()
        elif choice == "4":
            manager.update_contact()
        elif choice == "5":
            manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


