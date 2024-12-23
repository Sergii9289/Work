def find_it(seq):
    from collections import Counter
    return [x[1] for x in [(freq, ch) for ch, freq in Counter(seq).items()] if x[0] % 2 == 1][0]

if __name__ == '__main__':
    print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))