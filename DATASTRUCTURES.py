# Contact book manager

contact_book = {} 

def add_contact(name, number):
    contact_book[name] = number
    print(f"Contact {name} added.")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def show_contacts():
    for name, number in contact_book.items():
        print(f"{name}: {number}")

# Sample usage
add_contact("Alice", "1234567890")
add_contact("Bob", "9876543210")
delete_contact("Alice")
show_contacts()