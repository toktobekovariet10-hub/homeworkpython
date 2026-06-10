class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        # Используем одно подчеркивание, чтобы наследники имели доступ
        self._occupation = occupation
        self._higher_education = higher_education

    def introduce(self):
        education_str = "У меня есть высшее образование." if self._higher_education else "У меня нет высшего образования."
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self._occupation}. {education_str}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        education_str = "У меня есть высшее образование." if self._higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self._occupation}. "
              f"Я учился с Ариетом в группе {self.group_name}. {education_str}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_str = "У меня есть высшее образование." if self._higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self._occupation}. "
              f"Мое хобби {self.hobby}. {education_str}")


# Проверка работы
classmate1 = Classmate("Бектур", "05.12.2000", "программист", True, "ИНС-1-23")
classmate2 = Classmate("Айдин", "14.08.2001", "аналитик", True, "ИНС-1-23")

friend1 = Friend("Алмаз", "20.03.1999", "дизайнер", False, "футбол")
friend2 = Friend("Caner", "11.11.2002", "разработчик", True, "видеоигры")

classmate1.introduce()
classmate2.introduce()
print("---")
friend1.introduce()
friend2.introduce()



