import csv
CONTACTS_FILE = "contacts.csv"

def read_contacts():
    try:
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def write_contact(name, phone, email):
    with open(CONTACTS_FILE, mode='a', newline='') as file:
        fieldnames = ['name', 'phone', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({'name': name, 'phone': phone, 'email': email})

def delete_contact(name):
    contacts = read_contacts()
    contacts = [contact for contact in contacts if contact['name'] != name]
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        fieldnames = ['name', 'phone', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def main():
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            write_contact(name, phone, email)
            print('Added Successfully')
        elif choice == '2':
            contacts = read_contacts()
            for contact in contacts:
                print(f"{contact['name']} - {contact['phone']} - {contact['email']}")
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name)
            print('Deleted Successfully')
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

main()
