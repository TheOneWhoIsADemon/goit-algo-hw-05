def input_error(func):
    """
    Декоратор для обробки помилок і надання зручних повідомлень.
    Обробляє KeyError, ValueError та IndexError.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "Invalid input. Please provide the required arguments."
    return inner

@input_error
def parse_input(user_input):
    """Розбиває введений рядок на команду та її аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Приведення до нижнього регістру
    return cmd, args

@input_error
def add_contact(args, contacts):
    """Додає новий контакт у словник."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError

@input_error
def show_phone(args, contacts):
    """Виводить номер телефону за ім'ям."""
    name, = args

    return f"{name}'s phone number: {contacts[name]}"


@input_error
def show_all(contacts):
    """Виводить всі контакти та номери телефонів."""
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return "No contacts saved."

def main():
    contacts = {}  # Словник для збереження контактів
    print("Welcome to the assistant bot!")


    while True:
        user_input = input("Enter a command: ").strip()
        try:
        # Розбір введених користувачем команди та аргументи
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                # Завершення програми
                print("Good bye!")
                break
            elif command == "hello":

                print("How can I help you?")
            elif command == "add":

                print(add_contact(args, contacts))
            elif command == "change":

                print(change_contact(args, contacts))
            elif command == "phone":

                print(show_phone(args, contacts))
            elif command == "all":

                print(show_all(contacts))
            else:

                print("Invalid command.")
        except Exception as e:
            # Ловить будь-які непередбачувані помилки та виводьте повідомлення
            print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
