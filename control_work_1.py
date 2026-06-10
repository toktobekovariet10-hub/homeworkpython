class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def introduce(self):
        education_str = "есть высшее образование" if self.higher_education else "высшего образования нет"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, {education_str}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я из группы {self.group_name}. Я родился {self.birth_date} и работаю как {self.occupation}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, Моё хобби — {self.hobby}. Кстати, я родился {self.birth_date} и сейчас я {self.occupation}.")


classmate1 = Classmate("Бектур", "05.12.2000", "программист", True, "ИНС-1-23")
classmate2 = Classmate("Айдин", "14.08.2001", "аналитик", True, "ИНС-1-23")

friend1 = Friend("Алмаз", "20.03.1999", "дизайнер", False, "футбол")
friend2 = Friend(" caner ", "11.11.2002", "разработчик", True, "видеоигры")

classmate1.introduce()# Привет, меня зовут Бектур. Моя профессия программист. Я учился с Ариетом в группе ИНС-1-23. У меня есть высшее образование.
classmate2.introduce()# Привет, меня зовут Айдин. Моя профессия аналитик. Я учился с Ариетом в группе ИНС-1-23. У меня есть высшее образование.

friend1.introduce() # Привет, меня зовут Айбек. Моя профессия дизайнер. Мое хобби футбол. У меня нет высшего образования.
friend2.introduce() # Привет, меня зовут Айбек. Моя профессия разработчик. Мое хобби видеоигры. У меня есть высшее образование.





