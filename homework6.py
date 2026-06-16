class Backpack:
    def __init__(self, owner: str, items: list, max_items: int):
        self.owner = owner
        self.items = list(items)
        self.max_items = max_items

    def __str__(self):
        return f"<Backpack owner: {self.owner}, items: {len(self.items)}/{self.max_items}>"

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __bool__(self):
        return len(self.items) > 0

    def add_item(self, item):
        if len(self.items) < self.max_items:
            self.items.append(item)
            print(f"Предмет '{item}' успешно добавлен в рюкзак.")
        else:
            print(f"Не удалось добавить '{item}': в рюкзаке нет свободного места! (Максимум: {self.max_items})")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Предмет '{item}' удален из рюкзака.")
        else:
            print(f"Предмета '{item}' нет в рюкзаке, удалить невозможно.")


if __name__ == "__main__":
    backpack = Backpack("Ariet", ["ручка", "тетрадь"], 5)

    print(backpack)
    print(f"Количество предметов: {len(backpack)}")

    backpack.add_item("книга")
    backpack.add_item("телефон")
    print(backpack)

    backpack.add_item("ноутбук")
    backpack.add_item("линейка")

    print(f"Есть ли книга в рюкзаке? {'книга' in backpack}")
    print(f"Есть ли линейка в рюкзаке? {'линейка' in backpack}")

    backpack.remove_item("ручка")
    print(backpack)

    if backpack:
        print("Рюкзак не пустой")
    else:
        print("Рюкзак пустой")