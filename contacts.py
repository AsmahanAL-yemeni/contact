
import json

def load_cont():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

##################SAVE###############



def save_cont(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

##################ADD###############




def add_cont():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    address = input("Enter Address: ")

    new_contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }

    contacts = load_cont()
    contacts.append(new_contact)
    save_cont(contacts)
    print("Contact  successfully!")


##################DELETE###############



def delete_cont():
    name = input("Enter the name of the contact to delete: ")
    
    contacts = load_cont()
    removed = False


    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            removed = True

    if removed:
        save_cont(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


##################EDIT###############





def edit_cont():
    name = input("Enter the name of the contact to edit: ")

    contacts = load_cont()

    for contact in contacts:
        if contact["name"] == name:

            field = input("Enter the field to edit (name, email, phone, address): ")
            if field in contact:
                new_value = input(f"Enter new {field}: ")
                contact[field] = new_value
                save_cont(contacts)
                print("Contact edited successfully!")
                return
            else:
                print("Invalid field.")
                return

    print("Contact not found.")



##################SHOW################


def show_cont():
    contacts = load_cont()

    if len(contacts) > 0:

        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
            print(f"Address: {contact['address']}")
            print("------")
    else:
        print("No contacts found .")


while True:
    print("Contact Manager")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Edit Contact")
    print("4. Show Contacts")
    print("5. Exit")

    choice = input(" Please , Enter Your Choice   (1-5)  :  ")

    if choice == '1':
        add_cont()
    elif choice == '2':
        delete_cont()
    elif choice == '3':
        edit_cont()
    elif choice == '4':
        show_cont()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid . Please try again.")
