

class Contact:

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_number(number):
        if len(str(number)) == 10:
            return True
        else:
            return False


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        try:
            if Contact.validate_number(phone_number):
                new_contact = Contact(name, phone_number)
                cls.all_contacts.append(new_contact)
                print(f"Контакт {name} успешно добавлен.")
            else:
                raise ValueError(f"Номер {phone_number} некорректный.")
        except ValueError as e:
            print(f"Предупреждение: Контакт {name} не был добавлен. {e}")


ContactList.add_contact("Шедлетский", "9991234567")
ContactList.add_contact("Mарк Граф розвуел", "1234567890")
ContactList.add_contact("Ариет Токтобеков", "996990291110")

print("\n--- Финальный список сохраненных контактов ---")
for contact in ContactList.all_contacts:
    print(f"Имя: {contact.name} | Тел: {contact.phone_number}")