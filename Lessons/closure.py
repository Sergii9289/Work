def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


def pow_(base):
    return lambda value: value ** base


if __name__ == '__main__':
    boys = names()
    girls = names()
    print(boys('Vasya'))
    print(boys('Petya'))
    print(boys('Dima'))
    print(boys)
    print(girls('Olya'))
    print(girls('Sveta'))
    print(girls('Lena'))
    print(girls.__closure__[0].cell_contents)


