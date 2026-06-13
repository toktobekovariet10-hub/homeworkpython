class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        education_str = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}. {education_str}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        education_str = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Ариетом в группе {self.group_name}. {education_str}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_str = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. {education_str}")


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()