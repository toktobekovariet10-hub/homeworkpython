class Contact:

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_number(number):
        phone_number = str(number).strip()
        return len(phone_number) == 10 and phone_number.isdigit()


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_number(phone_number):
            raise ValueError(f"Номер {phone_number} некорректный. Должно быть ровно 10 цифр.")

        new_contact = Contact(name, phone_number)
        cls.all_contacts.append(new_contact)
        print(f"Контакт {name} успешно добавлен.")


try:
    ContactList.add_contact("Шедлетский", "9991034567")
    ContactList.add_contact("Mарк Граф розвуел", "1234567890")
    ContactList.add_contact("Ариет Токтобеков", "996990291110")
except ValueError as e:
    print(f"\n[Ошибка перехвачена снаружи]: {e}")

print("\n--- Финальный список сохраненных контактов ---")
for contact in ContactList.all_contacts:
    print(f"Имя: {contact.name} | Тел: {contact.phone_number}")