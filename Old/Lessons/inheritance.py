class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}, salary={self.salary}, bonus={self.bonus}%, ' \
               f'total bonus={self.calculate_total_bonus()} grn'


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)

    def calculate_total_bonus(self):
        return 75_000


if __name__ == '__main__':
    masha = Cleaner('Maria Ivanivna')
    print(masha)
    grisha = Manager('Grigoriy Petrovich')
    print(grisha)
    ivan_palych = CEO('Ivan Pavlovich')
    print(ivan_palych)
