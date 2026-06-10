class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_str = "есть высшее образование" if self.higher_education else "высшего образования нет"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, {education_str}.")

person1 = Person("Ариет", "15.05.1995", "программист", True)
person2 = Person("Мерали", "22.10.1998", "дизайнер", True)
person3 = Person("Максим", "03.02.2001", "водитель", False)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

person1.introduce()
person2.introduce()
person3.introduce()
