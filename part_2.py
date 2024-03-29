

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid input data"

def change_contact(args, contacts):
    try:
        name, phone = args
        record = contacts.get(name)
        if record: 
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid input data"
    
def phone_contact(args, contacts):
    try:
        name = args[0]
        record = contacts.get(name)
        if record: 
            return record
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid input data"
    except IndexError:
        return "You should add name of contact"
    
def show_all(contacts):
    if contacts:
        info = ''
        for name, phone in contacts.items():
            info += f'Contact {name} have phone: {phone}\n'
        return info
    else:
        return "Contact list is empty"    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()