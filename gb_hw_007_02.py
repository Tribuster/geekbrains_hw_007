#   2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
#   Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
#   К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#   размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#   Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#   для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
#   Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
#   реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, value):
        self.value = value

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {(self.value / 6.5 + 0.5) + (2 * self.value + 0.3) :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Smth vary abstract'


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.value / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Smth vary abstract second'


class Suit(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.value + 0.3 :.2f} ткани'

    def abstract(self):
        pass

class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return f'Всего нужно: {(self.a / 6.5 + 0.5) + (2 * self.b + 0.3) : .2f} ткани'

a = 54  #   размер пальто
b = 155  #   размер костюма

size_coat = Coat(a)
size_suit = Suit(b)
total = Total(a,b)

print(size_coat.consumption())
print(size_suit.consumption())
print(total.sum())
