def spin_words(sentence):
    s_list = sentence.split()
    res = []
    for i in s_list:
        if len(i) >= 5:
            res.append(i[::-1])
        else:
            res.append(i)
    return ' '.join(res)


if __name__ == '__main__':
    print(spin_words("Hey fellow warriors"))