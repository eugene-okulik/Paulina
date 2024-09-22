words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def repeater(word_dict):
    for key, value in word_dict.items():
        print(key * value)


repeater(words)
