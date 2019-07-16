def MergeStrings(strings):
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    counter = {}

    for char in valid_chars:
        counter[char] = 0
    for string in strings:
        for char in string:
            if char in valid_chars:
                counter[char] += 1

    str_list = []
    for char in valid_chars:
        str_list.append(char * counter[char])

    return "".join(str_list)


# strings = ['abc', 'def']
# strings = ['green eggs and ham', 'ham', 'sam', 'i', 'am']
strings = ['green', '']

print(MergeStrings(strings))
