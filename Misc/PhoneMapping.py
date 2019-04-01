def letterCombinations(digits):
    cache = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    result = [""]
    for num in digits:
        new_result = []
        for letter in cache[num]:
            for word in result:
                new_result.append(word + letter)
        result = new_result

    if len(result) == 1:
        return []
    return result


print(letterCombinations("342"))
print(letterCombinations(""))
print(letterCombinations("444"))
print(letterCombinations("99"))
