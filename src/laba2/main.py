
from abc import ABC, abstractmethod


class GameObject:
    def __init__(self, object_id, name, x, y):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getX(self):
        return self._x

    def getY(self):
        return self._y


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


class Unit(GameObject):
    def __init__(self, object_id, name, x, y, hp):
        super().__init__(object_id, name, x, y)
        self._hp = float(hp)

    def isAlive(self):
        return self._hp > 0

    def getHp(self):
        return self._hp

    def receiveDamage(self, damage):
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._hp = max(0.0, self._hp - damage)


class Archer(Unit, Attacker, Moveable):
    def attack(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError("Цель должна быть юнитом")
        if self.isAlive() and unit.isAlive():
            unit.receiveDamage(20)

    def move(self, x, y):
        if self.isAlive():
            self._x = x
            self._y = y


class Building(GameObject):
    def __init__(self, object_id, name, x, y, built=False):
        super().__init__(object_id, name, x, y)
        self._built = built

    def isBuilt(self):
        return self._built


class Fort(Building, Attacker):
    def attack(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError("Цель должна быть юнитом")
        if self.isBuilt() and unit.isAlive():
            unit.receiveDamage(30)


class MobileHouse(Building, Moveable):
    def move(self, x, y):
        self._x = x
        self._y = y


if __name__ == "__main__":
    archer1 = Archer(1, "Лучник 1", 0, 0, 100)
    archer2 = Archer(2, "Лучник 2", 5, 5, 100)
    fort = Fort(3, "Крепость", 10, 10, True)
    house = MobileHouse(4, "Передвижной дом", 2, 2, True)

    archer1.attack(archer2)
    print("Здоровье второго лучника:", archer2.getHp())

    fort.attack(archer1)
    print("Здоровье первого лучника:", archer1.getHp())

    archer1.move(3, 4)
    house.move(7, 8)

    print("Координаты первого лучника:", archer1.getX(), archer1.getY())
    print("Координаты передвижного дома:", house.getX(), house.getY())
