'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def textile(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, c_type, size):
        self.type = c_type
        self.size = int(size)

    @property
    def textile(self):
        if self.type == 'Suit':
            return 2 * self.size + 0.3
        if self.type == 'Coat':
            return self.size / 6.5 + 0.5


my_suit = Clothes('Coat', 48)
print(my_suit.textile)

