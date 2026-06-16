class Streamer:

    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:

    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:

    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):

    def ultimate_content(self):
        return (
            f"Ультимативный контент: {self.superpower()} "
            f"и параллельно читаю чат. {self.earn()}!"
        )


class ViralCyborg(TikToker, Mutant):

    def ultimate_content(self):
        return (
            f"Ультимативный контент: {self.viral()} "
            f"Потому что в кадре я {self.superpower()}!"
        )


class DonateMage(Streamer, TikToker):

    def ultimate_content(self):
        return (
            f"Ультимативный контент: {self.live()} "
            f"А в перерывах {self.viral()} Всего за день: {self.earn()}!"
        )


glow = GlowStreamer()
cyborg = ViralCyborg()
mage = DonateMage()

print("=== 1. GlowStreamer ===")
print("MRO:", GlowStreamer.mro())
print("Вызов live():", glow.live())
print(glow.ultimate_content())
print(
    "Объяснение live(): Сработал метод класса Streamer, так как при поиске "
    "методов слева направо (MRO) Streamer указан первым в списке наследования."
)
print("-" * 50)

print("=== 2. ViralCyborg ===")
print("MRO:", ViralCyborg.mro())
print("Вызов live():", cyborg.live())
print(cyborg.ultimate_content())
print(
    "Объяснение live(): Сработал метод класса TikToker, так как он идет первым "
    "родителем в объявлении класса и перехватывает вызов раньше, чем Mutant."
)
print("-" * 50)

print("=== 3. DonateMage ===")
print("MRO:", DonateMage.mro())
print("Вызов live():", mage.live())
print(mage.ultimate_content())
print(
    "Объяснение live(): Сработал метод класса Streamer, потому что он стоит "
    "левее класса TikToker. До тиктоковского live() очередь поиска просто не дошла."
)
print("-" * 50)