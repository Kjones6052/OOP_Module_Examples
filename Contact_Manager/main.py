import contact_manager

def main():
    contacts = []
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            contact_manager.add_contact(contacts, name, phone, email)
        elif choice == "2":
            contact_manager.view_contacts(contacts)
        elif choice == "3":
            name = input("Enter Name: ")
            contact = contact_manager.search_contacts(contacts, name)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print("Contact not found.")
        elif choice == "4":
            name = input("Enter Name: ")
            if contact_manager.delete_contact(contacts, name) is not None:
                print("Contact deleted.")
            else:
                print("Contact not found.")
        elif choice == "5":
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()