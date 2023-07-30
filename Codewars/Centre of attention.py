class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h




a = Image([1, 1, 4, 4, 4, 4, 2, 2, 2, 2,
           1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
           1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
           1, 1, 1, 1, 1, 3, 2, 2, 2, 2,
           1, 1, 1, 1, 1, 3, 3, 3, 2, 2,
           1, 1, 1, 1, 1, 1, 3, 3, 3, 3], 10, 6)


def left(x):
    if x % a.width == 0:
        return [1]
    else:
        count = 1
        y = x - 1
        while a.pixels[y] == a.pixels[x]:
            count += 1
            if y % a.width == 0:
                return [count]
            else:
                y -= 1
        return [count]


def right(x):
    if (x + 1) % a.width == 0:
        return [1]
    else:
        count = 1
        y = x + 1
        while a.pixels[y] == a.pixels[x]:
            count += 1
            if (y + 1) % a.width == 0:
                return [count]
            else:
                y += 1
        return [count]


def up(x):
    if x // a.width == 0:
        return [1]
    else:
        count = 1
        y = x - a.width
        while a.pixels[y] == a.pixels[x]:
            count += 1
            if y // a.width == 0:
                return [count]
            else:
                y -= a.width
        return [count]


def down(x):
    if x // a.width == (a.height - 1):
        return [1]
    else:
        count = 1
        y = x + a.width
        while a.pixels[y] == a.pixels[x]:
            count += 1
            if y // a.width == 5:
                return [count]
            else:
                y += a.width
        return [count]


depth_list = [(left(x) + right(x) + up(x) + down(x)) for x in range(len(a.pixels))]

print(depth_list)
