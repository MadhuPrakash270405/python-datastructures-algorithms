

def palindrome_check(word):
    return word == word[::-1]


def longest_palindrome_substring(STRING_TO_CHECK):
    if len(STRING_TO_CHECK) <= 1:
        return STRING_TO_CHECK
    for index1 in range(len(STRING_TO_CHECK)):
        for index2 in range(index1, len(STRING_TO_CHECK)):
            word_to_check = STRING_TO_CHECK[index1:index2+1]
            print(word_to_check)
            longest_substring = word_to_check if palindrome_check(
                word_to_check) and (len(longest_substring) < len(word_to_check)) else longest_substring
    print(longest_substring)
    return longest_substring


if __name__ == '__main__':
    STRING_TO_CHECK = 'bb'
    longest_substring = ''
    if STRING_TO_CHECK
