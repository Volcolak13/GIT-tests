#   Напишите программу по следующему описанию. Есть класс "Воин". От него создаются два экземпляра-юнита.
#   Каждому устанавливается здоровье в 100 очков. В случайном порядке они бьют друг друга. Тот, кто бьет,
#   здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого
#   удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья.
#   Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том,
#   кто одержал победу.

class Warrior:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    #    print(self.health, self.damage)

    # def take_damage(self, health):
    #     health = health - damage
    #     return health


Unit1 = Warrior("Unit1", 100, 20)
print("Создан юнит", Unit1.name, "здоровье:", Unit1.health, "урон:", Unit1.damage)

Unit2 = Warrior("Unit2", 100, 20)
print("Создан юнит", Unit2.name, "здоровье:", Unit2.health, "урон:", Unit2.damage)
