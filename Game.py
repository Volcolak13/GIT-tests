import random


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

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Воин", self.name, "получил", damage, "очков урона, остаток здоровья", self.health)
            print("\nХрабрый воин", self.name, "доблестно пал на поле брани")
            print("\nИгра окончена")
            quit()
        else:
            return print("Воин", self.name, "получил", damage, "очков урона, остаток здоровья", self.health)


Unit1 = Warrior("Воин 1", 100, 20)
print("Создан", Unit1.name, "здоровье:", Unit1.health, "урон:", Unit1.damage)

Unit2 = Warrior("Воин 2", 100, 20)
print("Создан", Unit2.name, "здоровье:", Unit2.health, "урон:", Unit2.damage)

a = 1
while a < 10:
    turn = random.randint(0, 1)
    if turn == 0:
        print("\n", Unit1.name, "атакует")
        Strike = Unit2.take_damage(Unit1.damage)
    elif turn == 1:
        print("\n", Unit2.name, "атакует")
        Strike = Unit1.take_damage(Unit2.damage)