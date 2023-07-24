class CoonCat:
    breed = 'Maine Coon'
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        CoonCat.increment_coutn()
        self.names.append(name)

    def meow(self):
        print(f'{self.name} of {self.breed} says: Meow!')

    @classmethod
    def increment_coutn(cls):
        cls.count += 1

    @classmethod
    def make_cat(cls, name):
        if name == 'Tom':
            return CoonCat('Tom', 2)
        elif name == 'Angela':
            return cls('Angela', 1)
        return cls('Ginger', 1)

    @staticmethod
    def get_human_age(age):
        return age * 8


if __name__ == '__main__':
    tom = CoonCat('Tom', 2)
    angela = CoonCat.make_cat('Angela')
    tom.meow()
    angela.meow()
    print(CoonCat.get_human_age(angela.age))
