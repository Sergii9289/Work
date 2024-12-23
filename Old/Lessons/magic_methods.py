class Banknote:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'Banknote({self.value})'

    def __str__(self):
        return f'Банкнота номиналом в {self.value} грн'

    def __eq__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value


class Iterator:
    def __init__(self, iter_container):
        self.iter_container = iter_container
        self.index = 0

    def __next__(self):
        while 0 <= self.index < len(self.iter_container):
            value = self.iter_container[self.index]
            self.index += 1
            return value
        raise StopIteration


class Wallet:

    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __call__(self):
        return f'{sum(x.value for x in self.container)} гривень'

    def __iter__(self):
        return Iterator(self.container)

    def __getitem__(self, item: int):
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key: int, value: Banknote):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


if __name__ == '__main__':
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred, hundred)
    print(hundred in wallet)  # __contains__
    if wallet: print('Там что-то есть')  # __bool__
    print(len(wallet))  # __len__
    print(wallet())  # __call__
    for money in wallet: print(money)
    print(wallet[0])
    wallet[0] = Banknote(500)
    print(wallet)
