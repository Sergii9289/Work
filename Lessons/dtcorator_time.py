from datetime import datetime


def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)

    return wrapper


@timeit
def one():
    l = []
    for i in range(10 ** 5):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit
def two():
    return [x for x in range(10 ** 5) if x % 2 == 0]


if __name__ == '__main__':
    one()
    two()
