
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name]=phone
        return f"Contact updated." 
    return f"⚠️ Контакт '{name}' не знайдено."
    

def show_phone(args, contacts):
    name = args[0]
    return f"{contacts[name]}" if contacts.get(name) else f"⚠️ Контакт '{name}' не знайдено."
    

def show_all(contacts):
    if not contacts:
        return "📭 No contacts saved yet."
    return "усі збережені контакти з номерами телефонів:\n" + \
           "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main(): # print/input тут
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                 print("Good bye!")
                 break
            elif command == "hello":
                 print("How can I help you?")
            elif command == "add":
                 print(add_contact(args, contacts))
            elif command=="change":
                 print(change_contact(args, contacts))
            elif command=="phone":
                 print(show_phone(args, contacts))
            elif command=="all":
                 print(show_all(contacts))
            else:
                 print("Invalid command.")

        except ValueError:
            print("""⚠️ Invalid input format(expected: "[command] [username] [phone]"). Please check your command and try again.""")
        except KeyError as e:
            print(f"⚠️ Contact not found: {e}")
        except Exception as e:
            print(f"💥 Oops, something went wrong: {e}")

if __name__ == "__main__":
    main()
