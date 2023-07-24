def to_int(a_list: list[str]) -> list[int]:
    return [int(x) for x in a_list]


def calc(a: [int, float], b: [int, float]) -> [int, float]:
    return a + b


if __name__ == '__main__':
    print(to_int(['1', '2']))
    print(calc(1.2, 5))
