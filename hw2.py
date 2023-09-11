class SuperHero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.fly = False

    def double_health(self):
        self.health = self.health ** 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

class AirHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage


class SpaceHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

class Villain(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, target):
        target.health = target.health ** self.damage

air_hero = AirHero("Airman", 100, 5)
space_hero = SpaceHero("Spaceman", 150, 7)
villain = Villain("Evil Villain", 200, 8)

air_hero.double_health()
space_hero.double_health()
villain.double_health()

print(air_hero.fly)
print(space_hero.fly)
print(villain.fly)

air_hero.true_phrase()
space_hero.true_phrase()
villain.true_phrase()

villain.gen_x()


villain.crit(air_hero)

print(air_hero.health)


