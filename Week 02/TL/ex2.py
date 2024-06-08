word = 'happiness'

def count_chars(word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

print(count_chars(word))