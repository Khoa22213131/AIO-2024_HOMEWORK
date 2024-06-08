def count_chars(word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

if __name__ == '__main__':
    word = 'happiness'
    print(count_chars(word))