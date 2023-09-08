class SuperHero:

    people = 'people'


    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase


    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2


    def __str__(self):
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}"


    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Ирон Мэн", "Тони Старк", "Интеллект и броня", 100, "Я - Железный человек!")


print(f"Имя героя: {hero.get_name()}")
print(f"Здоровье героя до увеличения: {hero.health_points}")
hero.double_health()
print(f"Здоровье героя после увеличения: {hero.health_points}")
print(hero)
print(f"Длина коронной фразы героя: {len(hero)}")
